import json
import numpy as np


def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    try:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Hi {first_name} {last_name} ",
            }),
        }
    except:
        return f'error in input {first_name} or {last_name}'

