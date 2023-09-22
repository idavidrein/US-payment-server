import json
import os
from pprint import pprint

import upwork
from dotenv import load_dotenv
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError
from upwork.routers.hr import engagements

load_dotenv()


def create_client():
    with open('token.json', 'r') as f:
        token_string = f.read()
        token = json.loads(token_string)

    config = upwork.Config({
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "token": token
    })
    client = upwork.Client(config)
    return client


def main():
    client = create_client()
    try:
        engagement_list = engagements.Api(client).get_list(params={
            "created_time_from": "2023-04-01T00:00:01",
            "status": "active",
            "page": "page=0;100"
        })['engagements']['engagement']

    except InvalidClientIdError:
        authorization_url, state = client.get_authorization_url()
        authz_code = input("Please enter the full callback URL you get "
                           "following this link:\n{0}\n\n> ".format(authorization_url))

        print("Retrieving access and refresh tokens.... ")
        token = client.get_access_token(authz_code)
        token_str = json.dumps(token)
        with open('token.json', 'w') as f:
            f.write(token_str)
        client = create_client()  # recreate client with new token
        engagement_list = engagements.Api(client).get_list(params={
            "created_time_from": "2023-04-01T00:00:01",
            "status": "active",
            "page": "page=0;100"
        })['engagements']['engagement']

    with open('engagement_list.csv', 'w') as f:
        f.write("portrait_url,reference,provider__reference\n")
        for e in engagement_list:
            f.write(f"{e['portrait_url']}, {e['reference']}, {e['provider__reference']}\n")

    return engagement_list


if __name__ == '__main__':
    main()
