import requests
import schedule
import time

def delete_webhook():
    bot_token = "6416227615:AAG6WpsPt0GgZzzlxIFOj2m9T0aBZ0NTb0I"
    api_url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"

    response = requests.post(api_url)

    if response.status_code == 200:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")

schedule.every(1).second.do(delete_webhook)

while True:
    schedule.run_pending()
    time.sleep(1)
