from pyrogram import Client
api_id   = int(input("API_ID: "))
api_hash =     input("API_HASH: ")
phone    =     input("Phone (+countrycode...): ")

# New v2 syntax: pass in_memory=True so no *.session file is left behind
with Client(":memory:", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
    app.send_code(phone)                           # Telegram sends you a code
    code = input("Code: ")
    try:
        app.sign_in(phone, code)                  # Handles 2-FA automatically
    except Exception as e:
        if "SESSION_PASSWORD_NEEDED" in str(e):
            app.check_password(input("2FA Password: "))
        else:
            raise

    s = app.export_session_string()               # ✨ Your fresh session
    print("\n=== COPY THIS SESSION STRING ===\n")
    print(s)
    print("\nPaste it into Heroku → Settings → Config Vars → SESSION_STRING\n")
