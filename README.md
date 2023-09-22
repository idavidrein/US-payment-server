# Overview
There are two components necessary: the server itself, and ngrok, which is used to expose the server to the internet (this is is necessary because Airtable does not support sending API requests to localhost).

# Installation and Setup

1. After cloning the repository, create a virtual environment (e.g. `conda create -n payment-server`) and activate it (e.g. `conda activate payment-server`).
2. Install the requirements: `pip install -r requirements.txt`
3. Create and populate `token.json` and `.env` files with the Upwork auth tokens and API keys. 
4. To start the server, run `gunicorn app:app` (optional flag `--reload` if you want to restart the server on code changes)
5. Follow the instructions [here](https://ngrok.com/docs/getting-started/) to install and run ngrok (you'll need to create an account)
6. Run `ngrok http 8000` to expose the server to the internet (or whatever port gunicorn is running on)
7. Copy the ngrok URL (e.g. `https://12345678.ngrok-free.app`) and paste it into the Airtable payment script (see below)

To add the ngrok URL to the Airtable payment script, open the "Extensions" panel, and click the "<> Edit code" button in the bottom. Then, paste the ngrok URL in line 20 to replace the existing URL. **Make sure to keep the "/payBonus" at the end of the URL**.
<img width="932" alt="Screenshot 2023-09-22 at 3 13 03 PM" src="https://github.com/idavidrein/US-payment-server/assets/26013403/4681a51f-0c7c-4d78-9f9a-7fc136ce035b">
<img width="711" alt="Screenshot 2023-09-22 at 3 13 30 PM" src="https://github.com/idavidrein/US-payment-server/assets/26013403/769f41c6-8c38-4c33-8a55-8d8de15b2e02">
