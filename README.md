# Overview
There are two components necessary: the server itself, and ngrok, which is used to expose the server to the internet (this is is necessary because Airtable does not support sending API requests to localhost).

# Installation and Setup

1. After cloning the repository, create a virtual environment (e.g. `conda create -n payment-server`) and activate it (e.g. `conda activate payment-server`).
2. Install the requirements: `pip install -r requirements.txt`
3. To start the server, run `gunicorn app:app` (optional flag `--reload` if you want to restart the server on code changes)
4. Follow the instructions [here](https://ngrok.com/docs/getting-started/) to install and run ngrok (you'll need to create an account)
5. Run `ngrok http 8000` to expose the server to the internet (or whatever port gunicorn is running on)
6. Copy the ngrok URL (e.g. `https://12345678.ngrok-free.app`) and paste it into the Airtable payment script (see below)

To add the ngrok URL to the Airtable payment script, open the "Extensions" panel, and click the "<> Edit code" button in the bottom. Then, paste the ngrok URL in line 20 to replace the existing URL. **Make sure to keep the "/payBonus" at the end of the URL**.