import json
import boto3

res = {
	'statusCode': 400,
	'body': json.dumps('Bad Request'),
	'headers': {
    	'Access-Control-Allow-Headers': 'Content-Type',
    	'Access-Control-Allow-Origin': '*',
    	'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
	},
}

def lambda_handler(event, context):
    # Parse the email address from the POST request body
    request_body = json.loads(event['body'])
    email = request_body.get('email', '')
    
    res['statusCode'] = 200
    res['body'] = json.dumps({'message': 'Email successfully subscirbed', 'email': email})

    # # Initialize the AWS SDK for SNS
    # sns = boto3.client('sns')

    # # SNS Topic ARN to which the user will be subscribed
    # topic_arn = 'arn:aws:sns:your_region:your_account_id:your_topic_name'

    # try:
    #     # Subscribe the user to the SNS topic
    #     response = sns.subscribe(
    #         Protocol='email',
    #         TopicArn=topic_arn,
    #         Endpoint=email
    #     )

    #     # Publish a welcome message to the SNS topic
    #     sns.publish(
    #         TopicArn=topic_arn,
    #         Message=f'Welcome, {email}! You are now subscribed to our notifications.',
    #         Subject='Subscription Confirmation'
    #     )

    #     # Response when subscription and message publication are successful
    #     response = {
    #         'statusCode': 200,
    #         'body': json.dumps({'message': 'Subscription successful and message published'})
    #     }
    # except Exception as e:
    #     # Response when subscription or message publication fails
    #     response = {
    #         'statusCode': 500,
    #         'body': json.dumps({'message': 'Subscription or message publication failed', 'error': str(e)})
    #     }

    return res