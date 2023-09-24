import psutil
import time
import requests
import os
from dotenv import load_dotenv


load_dotenv()

WEBHOOK = os.getenv("WEBHOOK")


def get_disk_usage():
    #Gets the disk usage on the persistent storage.
    root_partition = "/var/lib/data"
    usage = psutil.disk_usage(root_partition)

    total_disk_space = usage.total
    
    return {
	"total": usage.total / (1024 ** 3),
	"used": usage.used / (1024 ** 3),
	"free": usage.free / (1024 ** 3)
  }

def send_slack_alert(message):
  #Sends an alert to Slack via a webhook.
  requests.post(WEBHOOK, json={"text": message})

def main():
    #The main function. 
    threshold = 70
    while True:
        disk_usage = get_disk_usage()
        free_space = disk_usage["free"]
        if free_space < threshold:
            message = "Warning: Free disk space is less than {} GB".format(threshold)
            send_slack_alert(message)

        time.sleep(60)

if __name__ == "__main__":
  main()

