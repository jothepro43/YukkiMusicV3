#!/usr/bin/env python3
from pyrogram import Client, errors
import os

# Ask for user input for credentials
api_id = int(input("Enter your API_ID: ").strip())
api_hash = input("Enter your API_HASH: ").strip()
phone_number = input("Enter your phone number (with country code): ").strip()

# Use a temporary session name/file. Remove it if it exists to avoid any msg_id issues on reuse [oai_citation:3‡stackoverflow.com](https://stackoverflow.com/questions/77726848/pyrogram-telegram-server-synchronization-error#:~:text=i%20built%20a%20telegram%20bot,i%20got%20the%20same%20issue) [oai_citation:4‡github.com](https://github.com/Dineshkarthik/telegram_media_downloader/discussions/445#:~:text=Same%20issue%20here,different%20servers%20and%20problem%20persists).
session_name = "gen_string_session"
session_file = f"{session_name}.session"
if os.path.exists(session_file):
    try:
        os.remove(session_file)
    except Exception as e:
        print(f"Warning: could not remove existing session file: {e}")

# Initialize Pyrogram Client (Pyrogram 1.4.16 syntax)
app = Client(session_name, api_id=api_id, api_hash=api_hash)

# Start the client and prompt for login if not already authorized
print("\nLogging in to Telegram...")
app.connect()  # Connect to Telegram servers (synchronous call)
if not app.is_connected:  # Double-check connection (should be True if no exception)
    raise RuntimeError("Failed to connect to Telegram. Please check your internet connection.")

# If the session is new (not authorized), send the login code
if not app.is_authenticated:  # Pyrogram v1.x uses is_authenticated for logged-in check
    try:
        sent_code = app.send_code(phone_number)  # Send OTP code to the phone
    except errors.RPCError as e:
        app.disconnect()
        raise RuntimeError(f"Failed to send code: {e}")  # Likely invalid phone or flood error

    # Prompt for the code that was sent to the user's Telegram (or SMS)
    code = input("Enter the confirmation code you received: ").strip()

    try:
        # Sign in with phone number, code hash, and the code [oai_citation:5‡stackoverflow.com](https://stackoverflow.com/questions/75574099/how-to-log-in-to-telegram-using-pyrogram#:~:text=Here%20is%20example%20to%20login,with%20pyrogram)
        app.sign_in(phone_number, sent_code.phone_code_hash, code)
    except errors.SessionPasswordNeeded:
        # Two-factor auth enabled, ask for password
        password = input("Enter your 2FA password: ").strip()
        try:
            app.check_password(password=password)
        except errors.RPCError as e:
            app.disconnect()
            raise RuntimeError(f"Unable to verify 2FA password: {e}")

# We are now logged in. Export the session string.
try:
    session_string = app.export_session_string()
except Exception as e:
    app.disconnect()
    raise RuntimeError(f"Failed to export session string: {e}")

# Display the session string to the user
print("\n**Your Pyrogram session string (keep it secret!)**:\n")
print(session_string)  # Printed on console for user to copy
print("\n✅ Session string generated successfully. Copy the above string for use in your Heroku bot config.")
print("IMPORTANT: Treat this string like a password – do NOT share it with anyone.\n")

# Clean up and disconnect
app.disconnect()
