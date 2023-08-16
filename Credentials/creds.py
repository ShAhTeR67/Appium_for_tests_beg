import json


def creds_from_json(user_name: str) -> list:
    with open('../Credentials/creds.json', 'r') as file:
        creds = json.loads(file.read())
    return list(creds[user_name].values())
