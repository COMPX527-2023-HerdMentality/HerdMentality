import boto3
import random 
import json


table_name = "Questions"  

# Create the client
dynamodb = boto3.client('dynamodb', region_name="us-east-1")

def handler(event, context):
    if event['httpMethod'] == 'GET':
        try:
            # Use the scan operation to retrieve all items in the table
            response = dynamodb.scan(TableName=table_name)

            # Extract the values from the DynamoDB items
            items = response.get('Items', [])

            # Extract the values from the DynamoDB items
            questions = []
            for item in items:
                question = {}
                for key, value in item.items():
                    # Extract the actual value from the DynamoDB structure
                    question[key] = list(value.values())[0]
                questions.append(question)

            # Shuffle the questions to make the selection random
            random.shuffle(questions)

            # Limit to 20 questions
            questions = questions[:20]

            # Return the questions as a JSON response
            return {
                'statusCode': 200,
                'body': json.dumps(questions, default=str) 
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(str(e))
            }
            
    elif event['httpMethod'] == 'POST':
        try:
            # Parse the request body JSON
            request_body = json.loads(event['body'])
            question_id = request_body.get('question_id')
            vote_type = request_body.get('vote_type')
            
            print(request_body)
    
            # Check if both 'question_id' and 'vote_type' are provided
            if not question_id or vote_type not in ('Votes1', 'Votes2'): 
                return {
                    'statusCode': 400,
                    'body': json.dumps('Invalid request body format')
                }
    
            # Increment the vote count based on 'vote_type' (Votes1 or Votes2)
            response = dynamodb.update_item(
                TableName=table_name,
                Key={'ID': {'N': question_id}},
                UpdateExpression=f"SET {vote_type} = {vote_type} + :incr", 
                ExpressionAttributeValues={':incr': {'N': '1'}},
                ReturnValues='UPDATED_NEW'
            )
    
            # Get the updated vote count
            updated_vote_count = response['Attributes'][vote_type]
    
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Vote counted successfully', 'updated_vote_count': updated_vote_count})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(str(e))
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request')
        }
