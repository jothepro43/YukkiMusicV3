# genstring.py
import asyncio
from getpass import getpass
from pyrogram import Client

async def main():
    # 1) Prompt for your credentials
    api_id   = int(input("Enter your API_ID: ").strip())
    api_hash = input("Enter your API_HASH: ").strip()
    phone    = input("Enter your phone number (+<country><number>): ").strip()

    # 2) Create an in-memory client (no .session file)
    app = Client(
        ":memory:",    #Positional Session Name
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True    #Keep Session only in RAM
    )
    # 3) Connect only (no ping)
    await app.connect()

    # 4) Send and receive the login code
    code   = await app.send_code(phone)
    otp    = input("Enter the login code you received: ").strip()

    # 5) Complete authorization; handle 2FA if required
    try:
        await app.sign_in(
            phone_number=phone,
            phone_code=otp,
            phone_code_hash=code.phone_code_hash
        )
    except Exception as e:
        if "SESSION_PASSWORD_NEEDED" in str(e):
            pw = getpass("Two-step enabled. Enter your password: ")
            await app.check_password(password=pw)
        else:
            raise

    # 6) Export and display the session string
    session = await app.export_session_string()
    print("\n=== YOUR NEW SESSION STRING ===\n")
    print(session)
    print("\nCopy this entire string into your SESSION_STRING Config Var.\n")

    # 7) Cleanly disconnect
    await app.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
