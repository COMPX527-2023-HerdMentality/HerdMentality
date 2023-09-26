import json
def handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'headers': {
            'Set-Cookie': 'access_token='+event['queryStringParameters']['access_token']+"; HttpOnly; Secure",
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Allow-Credentials': 'true'
        }
    }

