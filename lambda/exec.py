def lambda_handler(event, context):
    print("In lambda handler")
    import boto3
    import botocore
    import random
    import json
    from boto3.dynamodb.conditions import Key, Attr
   

    userid = (random.randint(1,15))
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('luckydraw')

    response = table.get_item(
        Key={
            'user_id': userid
        }
    )
    
    json_string = json.dumps(response)
    resp_dict=json.loads(json_string)
    user=json.dumps(resp_dict['Item'])
    user_dict=json.loads(user)

    resp = {
         "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(user_dict['user_id'])
    }

    return resp
    
