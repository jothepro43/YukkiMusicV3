import os
from pyrogram import Client

if __name__ == "__main__":
    print("📲 **Pyrogram String Session Generator** for Yukki Music Bot\n")
    # Get your Telegram API credentials (from my.telegram.org)
    api_id = int(input("Enter your **API ID**: ").strip())
    api_hash = input("Enter your **API HASH**: ").strip()

    # Use in-memory session (no .session file) for a clean login
    with Client(\"gen_session\", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
        # If not logged in, Pyrogram will prompt for phone and code here
        session_string = app.export_session_string()
        try:
            # Try to send the session string to your own Saved Messages for convenience
            app.send_message(\"me\", f\"**Yukki Music Bot String Session**\\n`{session_string}`\\n\\n⚠️ **Keep this secret!**\")
            print(\"\\n✅ Generated Pyrogram string session and sent it to your Telegram Saved Messages.\")
        except Exception as send_err:
            print(\"\\n✅ Generated Pyrogram string session:\") 
            print(session_string)
            print(\"\\n(Unable to send it as a message, copy the string above now.)\")

    print(\"\\n**Done.** Remember to add this string to your Heroku config vars (e.g. STRING_SESSION).\\n\")
