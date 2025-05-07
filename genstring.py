#!/usr/bin/env python3
import os
from pyrogram import Client, errors

# 1) Clean out any old session file
SESSION_NAME = "gen_session"
SESSION_FILE = f"{SESSION_NAME}.session"
if os.path.exists(SESSION_FILE):
    try:
        os.remove(SESSION_FILE)
    except:
        pass

# 2) Prompt for your Telegram API credentials
api_id   = int(input("Enter your API_ID: ").strip())
api_hash =    input("Enter your API_HASH: ").strip()
phone    =    input("Enter your phone number (+<country><number>): ").strip()

# 3) Initialize Pyrogram client (v1.4.16 style)
app = Client(SESSION_NAME, api_id=api_id, api_hash=api_hash)

print("\n📡 Connecting to Telegram…")
app.start()  # this will connect + prompt for code if needed

# 4) Send code + sign in
print("📨 Sending login code to", phone)
sent = app.send_code(phone)

code = input("📥 Enter the code you received: ").strip()
try:
    app.sign_in(phone, sent.phone_code_hash, code)
except errors.SessionPasswordNeeded:
    pw = input("🔒 Enter your 2FA password: ").strip()
    app.check_password(pw)

# 5) Export and show the session string
session_str = app.export_session_string()
print("\n🔑 **YOUR NEW SESSION STRING** 🔑\n")
print(session_str)
print("\n––––––––––––––––––––––––––––––––––––––––––––")
print("⚠️  Copy that ENTIRE string and set it as your")
print("   SESSION_STRING config var in Heroku.")
print("––––––––––––––––––––––––––––––––––––––––––––\n")

# 6) Clean up
app.stop()
