import requests
import schedule
import time

def delete_webhook():
    bot_token = "5835400119:AAG05VIHGiaNvefr3DKF4yd8bTAcZLSyxx4"
    api_url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"

    response = requests.post(api_url)

    if response.status_code == 200:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")

schedule.every(12).hours.do(delete_webhook)

while True:
    schedule.run_pending()
    time.sleep(1)
