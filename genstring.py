#!/usr/bin/env python3
from pyrogram import Client, errors

api_id   = int(input("API_ID: ").strip())
api_hash =     input("API_HASH: ").strip()
phone    =     input("Phone (+countrycode…): ").strip()

# use an in-memory session so no .session file is saved
with Client(":memory:", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
    sent = app.send_code(phone)                          # Telegram sends you a code
    code = input("Code: ").strip()

    try:
        # *** pass BOTH hash + code ***
        app.sign_in(phone_number=phone,
                    phone_code_hash=sent.phone_code_hash,
                    phone_code=code)
    except errors.SessionPasswordNeeded:
        pw = input("2-FA Password: ").strip()
        app.check_password(pw)

    s = app.export_session_string()
    print("\n=== COPY THIS SESSION STRING ===\n")
    print(s)
    print("\nPaste it into Heroku → Settings → Config Vars → SESSION_STRING\n")
