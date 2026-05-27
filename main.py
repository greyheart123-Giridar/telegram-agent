from telethon import TelegramClient, events
import re
import requests
import os
from telethon import TelegramClient, events

# =========================
# TELEGRAM API
# =========================

api_id = 36130331
api_hash = '92017a437038fca56df62091e2e468b7'
phone = '+918125728924'

# =========================
# BOT TOKEN
# =========================

bot_token = '8649361573:AAHKZeqFm1HKUoXWS2zJtsLL0cPAKaz1XMU'

# =========================
# YOUR CHANNEL USERNAME
# =========================

channel_username = '@SGShoppingtricks'

# =========================
# GROUP USERNAMES
# =========================

groups = [
    'iamprasadtech',
    'telugutechtuts',
    'deals',
    'FreePromos'
]
# Store already posted messages
posted_messages = set()



# GET VALUES FROM RENDER ENVIRONMENT VARIABLES
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")

# CHECK VARIABLES
if not api_id or not api_hash or not phone:
    raise Exception("Missing API_ID, API_HASH, or PHONE environment variables")

# CREATE CLIENT
client = TelegramClient("session", int(api_id), api_hash)
# =========================
# CREATE CLIENT
# =========================

client = TelegramClient('session', api_id, api_hash)

# =========================
# NEW MESSAGE EVENT
# =========================
import re

amazon_affiliate = "https://amzn.to/4a9GtqF"
flipkart_affiliate = "https://fktr.in/f0ZWi23"
myntra_affiliate = "https://myntr.it/BMVu9hJ"
ajio_affiliate = "https://ajiio.in/lGNscdU"

def replace_links(message):

    # Detect all URLs
    urls = re.findall(r'https?://\S+', message)

    for url in urls:

        # Amazon
        if "amazon" in url:
            message = message.replace(url, amazon_affiliate)

        # Flipkart
        elif "flipkart" in url:
            message = message.replace(url, flipkart_affiliate)

        # Myntra
        elif "myntra" in url:
            message = message.replace(url, myntra_affiliate)
        
        # Ajio
        elif "ajio" in url:
            message = message.replace(url, ajio_affiliate)    

    return message


    # Amazon links
    amazon_pattern = r'https?://[^\s]*amazon[^\s]*'

    # Flipkart links
    flipkart_pattern = r'https?://[^\s]*flipkart[^\s]*'

    # Myntra links
    myntra_pattern = r'https?://[^\s]*myntra[^\s]*'

    # Replace Amazon links
    amazon_links = re.findall(amazon_pattern, message)

    for link in amazon_links:
        message = message.replace(
            link,
            "https://amzn.to/4a7K8VU"
        )

    # Replace Flipkart links
    flipkart_links = re.findall(flipkart_pattern, message)

    for link in flipkart_links:
        message = message.replace(
            link,
            "https://fktr.in/zluvj1I"
        )

    # Replace Myntra links
    myntra_links = re.findall(myntra_pattern, message)

    for link in myntra_links:
        message = message.replace(
            link,
            "https://myntr.it/w3fjqAa"
        )

    return message
    
def get_hashtags(message):

    hashtags = "#Deals #Discount"

    # Amazon
    if "amazon" in message.lower():
        hashtags += " #AmazonDeals"

    # Flipkart
    if "flipkart" in message.lower():
        hashtags += " #FlipkartDeals"

    # Myntra
    if "myntra" in message.lower():
        hashtags += " #MyntraDeals"

    return hashtags


@client.on(events.NewMessage(chats=groups))
async def handler(event):

    message = event.message.message
    message = replace_links(message)
    
    # Check duplicate messages
    if message in posted_messages:
        print("Duplicate message ignored")
        return

    # Save message in memory
    posted_messages.add(message)


    # Ignore empty messages
    if not message:
        return
    print(message)
    
    message = replace_links(message)
    # Ignore very short messages
    if len(message) < 15:
        return

    # Ignore messages without price symbol
    if "₹" not in message and "Rs" not in message:
        return

    print("\nNEW MESSAGE:")
    print(message)


    # Simple formatting
    hashtags = get_hashtags(message)
    formatted_message = f"""
🔥 DEAL ALERT 🔥

━━━━━━━━━━━━━━━

{message}

━━━━━━━━━━━━━━━
{hashtags}

🛒 Grab The Offer Fast
⚡ Limited Time Deal
"""

    # Telegram API URL
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = {
        "chat_id": channel_username,
        "text": formatted_message
    }

    requests.post(url, data=data)

    print("Posted Successfully")

# =========================
# START
# =========================

client.start()

print("Listening for new messages...")

client.run_until_disconnected()