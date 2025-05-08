#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client

import config

from config import (
    API_ID,
    API_HASH,
    MUSIC_BOT_NAME,
    STRING1,    # ← primary session (env: STRING_SESSION)
    STRING2,
    STRING3,
    STRING4,
    STRING5,
)

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        if STRING1:
            self.one = Client(
                name=f"{MUSIC_BOT_NAME}_1",            # unique v2 “name”
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=StringSession(STRING1),  # NEW: in-memory string session
                workers=8,
                plugins={"root": "YukkiMusic.plugins"},
            )
        # -- Secondary ASSISTANTS 
        if STRING2:
            self.two = Client(
                name=f"{MUSIC_BOT_NAME}_2",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=StringSession(STRING2),
                workers=8,
                no_updates=True,
        )
        if STRING3:
            self.three = Client(
                name=f"{MUSIC_BOT_NAME}_3",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=StringSession(STRING3),
                workers=8,
                no_updates=True,
        )
        if STRING4:
            name=f"{MUSIC_BOT_NAME}_4",
                api_id=API_ID,
            api_hash=API_HASH,
            session_string=StringSession(STRING4),
            workers=8,
            no_updates=True,
        ) 
        if STRING5:
            self.five = Client(
                name=f"{MUSIC_BOT_NAME}_5",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=StringSession(STRING5),
                workers=8,
                no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients")
        if STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Lunatic0de")
                await self.one.join_chat("SharingUserbot")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
        if STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("Lunatic0de")
                await self.one.join_chat("SharingUserbot")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if STRING3:
            await self.three.start()
            try:
                await self.one.join_chat("Lunatic0de")
                await self.one.join_chat("SharingUserbot")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if STRING4:
            await self.four.start()
            try:
                await self.one.join_chat("Lunatic0de")
                await self.one.join_chat("SharingUserbot")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if STRING5:
            await self.five.start()
            try:
                await self.one.join_chat("Lunatic0de")
                await self.one.join_chat("SharingUserbot")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, "Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
