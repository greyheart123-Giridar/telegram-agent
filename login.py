from telethon.sync import TelegramClient

api_id = 36130331
api_hash = "92017a437038fca56df62091e2e468b7"
phone = "+918125728924"

client = TelegramClient("session", api_id, api_hash)

client.start(phone=phone)

print("Login successful!")