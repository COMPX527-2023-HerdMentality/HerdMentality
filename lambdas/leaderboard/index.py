import boto3
from boto3.dynamodb.conditions import Key  # Add this import
import json

# Define the DynamoDB table that Lambda will connect to
table_name = "Leaderboard"

# Create the DynamoDB resource
leaderboard_table = boto3.resource('dynamodb').Table(table_name)


res = {
	'statusCode': 400,
	'body': json.dumps('Bad Request'),
	'headers': {
    	'Access-Control-Allow-Headers': 'Content-Type',
    	'Access-Control-Allow-Origin': '*',
    	'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
	},
}

def handler(event, context):
 
    # If we are getting the leaderboard with just /leaderboard and no body
    if event['httpMethod'] == 'GET':
        # Use the scan operation to retrieve all items in the table
        response = leaderboard_table.scan()
        
        # Get all items and sort them by score in descending order
        items = response['Items']
        print(items)
        items.sort(key=lambda x: x['Score'], reverse=True)

        # Convert Decimal values to float for JSON serialization
        leaderboard = []
        for item in items[:10]:  # Get the top 10 scores
            user_id = item['UserID']
            score = float(item['Score'])  # Convert Decimal to float
            leaderboard.append({'UserId': user_id, 'Score': score})

        res['statusCode'] = 200
        res['body'] = json.dumps(leaderboard)
    
    # If the request is a POST then extract the body with the new score and update the leaderboard
    elif event['httpMethod'] == 'POST':
        try:
            request_body = json.loads(event['body'])
            name = event['requestContext']['authorizer']['claims']['username']
            score = request_body['score']
            currentHighScore = 0
            
            # Get the current highscore
            try:
                response = leaderboard_table.get_item(Key={'UserID': name})
                currentHighScore = response['Item']['Score']
                
                if currentHighScore < score:
                    # Add the new entry to the leaderboard
                    leaderboard_table.put_item(
                        Item={
                            'UserID': name,
                            'Score': score
                        }
                    )
            
                    res['statusCode'] = 201
                    res['body'] = json.dumps('New entry added to the leaderboard')
                else:
                    print("Not a new high score")
                    res['body'] = json.dumps("Score is not a high score")
                    return res
                
            except ClientError as err:
                print(err.response['Error']['Message'])
                
        except:
            res['body'] = json.dumps("No body in request")
	
	# return the created response
    return res


