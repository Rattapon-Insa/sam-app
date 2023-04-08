import json
import uuid

GET_RAW_PATH = '/getPerson'
CREAT_RAW_PATH = '/createPerson'


def lambda_handler(event, context):
    if event['rawPath'] == GET_RAW_PATH:
        # do something
        print("this is get path")
        personId = event['queryStringParameters']['personId']
        print("Recieve rquest for person id = ", personId)
        return {
            "personId" : str(personId),
            "firstName" : "Rattapon",
            "lastName" : "Ins"
        }
    elif event['rawPath'] == CREAT_RAW_PATH:
        print("this is create path")
        decodeEvent = json.loads(event['body'])
        firstName = decodeEvent['firstName']
        lastName = decodeEvent['lastName']
        return {
                "personId" : str(uuid.uuid1()),
                "firstName" : firstName,
                "lastName" : lastName,
                "status" : "created"
                }

