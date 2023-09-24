import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("WEBHOOK")

def send_slack_alert(message):
  #Sends an alert to Slack via a webhook.
  requests.post(WEBHOOK,json={"text": message})

# Send a test message to the Slack webhook.
response = requests.post(WEBHOOK, json={"text": "This is a test message."})

# Check the response status code.
if response.status_code == 200:
  print("Test message sent successfully!")
else:
  print("Error sending test message:", response.content)



