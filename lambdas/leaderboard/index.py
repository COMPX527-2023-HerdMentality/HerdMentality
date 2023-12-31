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
        
        if event['queryStringParameters'] is not None:
            if event['queryStringParameters']['user_id'] is not None:
                userId = event['queryStringParameters']['user_id']
                response = leaderboard_table.get_item(Key={'UserID': userId})
                if not 'Item' in response:
                    data = {'Score':-1}
                    res['body'] = json.dumps(data)
                    return res
                currentHighScore = response['Item']['Score']
                data = {'Score': float(currentHighScore)}
                res['body'] = json.dumps(data)
                return res

        # Use the scan operation to retrieve all items in the table
        response = leaderboard_table.scan()
        
        # Get all items and sort them by score in descending order
        items = response['Items']
        items.sort(key=lambda x: x['Score'], reverse=True)

        # Convert Decimal values to float for JSON serialization
        leaderboard = []
        for item in items[:10]:  # Get the top 10 scores
            Username = item['Username']
            score = float(item['Score'])  # Convert Decimal to float
            leaderboard.append({'Username': Username, 'Score': score})

        res['statusCode'] = 200
        res['body'] = json.dumps(leaderboard)
    
    # If the request is a POST then extract the body with the new score and update the leaderboard
    elif event['httpMethod'] == 'POST':
        try:
            request_body = json.loads(event['body'])
            userId = event['requestContext']['authorizer']['claims']['username']
            score = request_body['score']
            username = ''
            if 'username' in request_body:
                username = request_body['username']
            currentHighScore = 0
            
            print("About to get highscore...")
            
            # Get the current highscore
            try:
                print("Inside try block!")
                response = leaderboard_table.get_item(Key={'UserID': userId})
                print(event)
                currentHighScore = -1
                if 'Item' in response:
                    currentHighScore = response['Item']['Score']
                    username = response['Item']['Username']
                
                if currentHighScore < score:
                    # Add the new entry to the leaderboard
                    leaderboard_table.put_item(
                        Item={
                            'UserID': userId,
                            'Username': username,
                            'Score': score
                        }
                    )
            
                    res['statusCode'] = 201
                    res['body'] = json.dumps('New entry added to the leaderboard')
                else:
                    res['body'] = json.dumps("Score is not a high score")
                    return res
                
            except ClientError as err:
                print(err.response['Error']['Message'])
                
        except:
            res['body'] = json.dumps("No body in request")
	
	# return the created response
    return res


