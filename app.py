import random
import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '6028447687:AAGJtVpsUDL6KAzDzcm6LPT5nYN9rjQwTuQ'

# List of allowed video extensions
allowed_extensions = ['.mp4', '.mov']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send /reel to get a random video!")

def reel(update: Update, context: CallbackContext) -> None:
    # List of video URLs
    video_urls = [
        "https://cdn.discordapp.com/attachments/1101163334692245546/1101164269845889.mp4",
        "https://cdn.discordapp.com/attachments/1101163334692245546/1101164241156841.mp4",
        "https://cdn.discordapp.com/attachments/1101163334692245546/1101164052413165.mp4",
        "https://cdn.discordapp.com/attachments/1101163334692245546/1101164246101925.mp4",
    ]

    # Filter video URLs by allowed extensions
    valid_video_urls = [url for url in video_urls if any(url.endswith(ext) for ext in allowed_extensions)]

    if valid_video_urls:
        random_video_url = random.choice(valid_video_urls)

        # Download video
        response = requests.get(random_video_url)
        if response.status_code == 200:
            with open("downloaded_video.mp4", "wb") as f:
                f.write(response.content)

            # Send video to bot
            with open("downloaded_video.mp4", "rb") as video_file:
                update.message.reply_video(video_file)

            # Delete downloaded video
            os.remove("downloaded_video.mp4")

        else:
            update.message.reply_text("Failed to download video.")
    else:
        update.message.reply_text("No valid videos available.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reel", reel))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()