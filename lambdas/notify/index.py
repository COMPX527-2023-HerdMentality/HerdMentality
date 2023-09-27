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

def handler(event, context):
    # Parse the email address from the POST request body
    request_body = json.loads(event['body'])
    email = request_body.get('email')

    # Initialize the AWS SDK for SNS
    sns = boto3.client('sns')

    # SNS Topic ARN to which the user will be subscribed
    topic_arn = 'arn:aws:sns:us-east-1:760360511766:leaderboard_notifier'

    try:

        # Publish a welcome message to the SNS topic
        sns.publish(
            TopicArn=topic_arn,
            Message=f'Someone has just entered the leaderboard, jump back in now to secure your position!',
            Subject='Herd Mentality Leaderboard'
        )
    
        # Subscribe the user to the SNS topic
        response = sns.subscribe(
            Protocol='email',
            TopicArn=topic_arn,
            Endpoint=email
        )

        # Response when subscription and message publication are successful
        res['statusCode'] = 200
        res['body'] = json.dumps({'message': 'Subscription successful and message published'})
    
    except Exception as e:
        # Response when subscription or message publication fails
        res['statusCode'] = 500
        res['body'] = json.dumps({'message': 'Subscription or message publication failed', 'error': str(e)})

    return res