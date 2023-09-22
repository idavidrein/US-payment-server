import json
import os

import upwork
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError
from upwork.routers import auth, payments

app = Flask(__name__)
CORS(app)

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


@app.route('/callback', methods=['POST'])
def auth_callback():
    return


@app.route('/payBonus', methods=['POST'])
def pay_bonus():
    client = create_client()
    data = request.json
    params = {
        'engagement__reference': data['engagement__reference'],
        'comments': data['description'],
        'charge_amount': round(data['payment'], 2)
    }
    print(params)
    try:
        response = payments.Api(client).submit_bonus(data['team__reference'], params)
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
        response = payments.Api(client).submit_bonus(data['team__reference'], params)

    print(response)
    return response


if __name__ == '__main__':
    app.run(port=5001)
