import boto3
from boto3.dynamodb.conditions import Key  # Add this import
import json

# Define the DynamoDB table that Lambda will connect to
table_name = "Leaderboard"

# Create the DynamoDB resource
leaderboard_table = boto3.resource('dynamodb').Table(table_name)

def handler(event, context):
 
    # If we are getting the leaderboard with just /leaderboard and no body
    if event['httpMethod'] == 'GET':
        # Use the query operation to retrieve the top 10 scores in descending order
        response = leaderboard_table.query(
            KeyConditionExpression=Key('Score').gte(0),
            ScanIndexForward=False,  # Sort in descending order
            Limit=10  # Limit the result to the top 10 scores
        )
        
        # Create a list to store the leaderboard data
        leaderboard = []
        
        # Append each user's data to the leaderboard list
        for item in response['Items']:
            user_id = item['UserId']
            score = item['Score']  # Replace with your score attribute name
            leaderboard.append({'UserId': user_id, 'Score': score})
 
        # Return the leaderboard as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps(leaderboard)
        }
    
    # If the request is a POST then extract the body with the new score and update the leaderboard
    elif event['httpMethod'] == 'POST':
        # Parse the request body JSON
        try:
            request_body = json.loads(event['body'])
            name = request_body['name']
            score = request_body['score']
        # Account for bad data format 
        except KeyError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid request body format')
            }
        
        # Add the new entry to the leaderboard
        leaderboard_table.put_item(
            Item={
                'UserId': name, 
                'Score': score
            }
        )
        
        return {
            'statusCode': 201,
            'body': json.dumps('New entry added to the leaderboard')
        }
    
    # Otherwise a bad request has occured 
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request')
        }