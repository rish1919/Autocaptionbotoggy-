from pyrogram import Client, filters
from pyrogram.types import Message
import random
import json
import os

API_ID = 25863650
API_HASH = "fde095aa1f406d52cb80a7bccaebb721"
BOT_TOKEN = "8193538818:AAE-2gwr2U7zTFCHDxBoEzXweNSwSIqTfTk"
OWNER_ID = 5122052972

app = Client("AutoCaptionBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

CAPTIONS = [
    "𝗛𝗮𝗮𝘁𝗵 𝗹𝗮𝗴𝗮𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝘀𝗶𝗿𝗳 𝗱𝗲𝗸𝗵 𝗸𝗲 𝗵𝗶 𝘁𝗿𝗶𝗽 𝗵𝗼 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😜💦",
    "𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗻𝗮𝗵𝗶 𝗵𝗼𝘁𝗮… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝘀𝗮𝗯 𝗸𝗮𝗿 𝗹𝗶𝘆𝗮 😈🔥",
    "𝗣𝗮𝗸𝗮𝗱𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗳𝗲𝗲𝗹 𝗸𝗮𝗿𝗻𝗲 𝗱𝗲 😏💋",
    "𝗟𝗮𝗽𝗲𝘁𝗻𝗲 𝗸𝗮 𝗺𝗼𝗼𝗱 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗱𝗲𝗸𝗵 𝗸𝗲 𝗵𝗶 𝗸𝗮𝗮𝗺 𝗰𝗵𝗮𝗹𝗮 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😘💦",
    "𝗧𝗼𝘂𝗰𝗵 𝗸𝗮𝗿𝗻𝗲 𝗸𝗮 𝗽𝗹𝗮𝗻 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝘂𝗻𝗱𝗿𝗲𝘀𝘀 𝗵𝗼 𝗿𝗮𝗵𝗮 𝗵𝗮𝗶 😈🔥",
    "𝗧𝗲𝗿𝗲 𝗰𝘂𝗿𝘃𝗲𝘀 𝗽𝗲 𝗵𝗮𝗮𝘁𝗵 𝗽𝗵𝗶𝗿𝗮𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗸𝗮𝗮𝗳𝗶 𝗵𝗮𝗶 😏💋",
    "𝗕𝗮𝘀 𝗱𝗲𝗸𝗵 𝗸𝗲 𝗵𝗶 𝗵𝗼𝗿𝗻𝘆 𝗵𝗼 𝗴𝗮𝘆𝗮… 😜💦",
    "𝗗𝗶𝗹 𝗸𝗮𝗿𝘁𝗮 𝗵𝗮𝗶 𝗸𝗵𝗲𝗲𝗻𝗰𝗵 𝗹𝗼𝗼𝗻… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝘀𝘁𝗿𝗶𝗽 𝗸𝗮𝗿 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😈🔥",
    "𝗣𝗮𝗸𝗮𝗱𝗻𝗲 𝗸𝗶 𝗶𝗰𝗵𝗵𝗮 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗵𝗶 𝘁𝗿𝗶𝗽 𝗵𝗼 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😘💦",
    "𝗖𝗵𝗵𝗲𝗱𝗻𝗲 𝗸𝗮 𝗺𝗼𝗼𝗱 𝗵𝗮𝗶… 𝗽𝗮𝗿 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗵𝗶 𝗸𝗵𝗲𝗹 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😏💋",
    "𝗕𝗼𝗱𝘆 𝗸𝗼 𝗳𝗲𝗲𝗹 𝗸𝗮𝗿𝗻𝗮 𝗵𝗮𝗶… 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗵𝗶 𝗻𝗮𝘀𝗵𝗮 𝗵𝗼 𝗴𝗮𝘆𝗮 😜🔥",
    "𝗞𝗵𝗮 𝗹𝗲𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 𝗱𝗲𝗸𝗵 𝗸𝗲 𝗵𝗶 𝘁𝗿𝗶𝗽 𝗵𝗼 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😈💦",
    "𝗛𝗮𝗮𝘁𝗵 𝘀𝗲 𝘁𝗼𝘂𝗰𝗵 𝗸𝗮𝗿𝘂𝗻? 𝗡𝗮𝗵𝗶… 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗸𝗮𝗮𝗳𝗶 𝗵𝗮𝗶 😏💋",
    "𝗔𝗮𝗷 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝘀𝘁𝗿𝗶𝗽 𝗸𝗮𝗿𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 😜🔥",
    "𝗠𝗮𝗻𝗻 𝗸𝗮𝗿𝘁𝗮 𝗵𝗮𝗶 𝘀𝗮𝗯 𝗸𝘂𝗰𝗵 𝗸𝗮𝗿 𝗹𝗼𝗼𝗻… 𝗱𝗲𝗸𝗵𝗻𝗲 𝗺𝗲𝗶𝗻 𝗵𝗶 𝗺𝗮𝘇𝗮 𝗵𝗮𝗶 😈💦",
    "𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗻𝗮𝗵𝗶 𝗵𝗼 𝗿𝗮𝗵𝗮… 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝘀𝗮𝗯 𝗸𝗮𝗿 𝗹𝗶𝘆𝗮 😘💋",
    "𝗗𝗶𝗹 𝗸𝗮𝗿𝘁𝗮 𝗵𝗮𝗶 𝗴𝗮𝗹𝗲 𝗹𝗮𝗴𝗮 𝗹𝗼𝗼𝗻… 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗽𝗼𝘀𝘀𝗲𝘀𝘀 𝗸𝗮𝗿 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😏🔥",
    "𝗖𝗵𝗵𝗲𝗱 𝗰𝗵𝗵𝗮𝗱 𝗸𝗮𝗿𝗻𝗲 𝗸𝗮 𝗺𝗮𝗻𝗻 𝗵𝗮𝗶… 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗸𝗮𝗿 𝗿𝗮𝗵𝗮 𝗵𝗼𝗼𝗻 😜💦",
    "𝗔𝗮𝗷 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗵𝗶 𝘀𝗮𝗯 𝗸𝘂𝗰𝗵 𝗸𝗮𝗿𝗻𝗲 𝗸𝗮 𝗺𝗼𝗼𝗱 𝗵𝗮𝗶 😈💋",
    "𝗧𝗲𝗿𝗲 𝗰𝘂𝗿𝘃𝗲𝘀 𝗮𝗮𝗻𝗸𝗵𝗼𝗻 𝘀𝗲 𝗵𝗶 𝗯𝗵𝗶𝗴𝗼 𝗱𝗶𝗲… 😏🔥",
]

REACTION_LINE = "❤️‍🔥 𝗥𝗘𝗔𝗖𝗧𝗜𝗢𝗡𝗦 𝗕𝗛𝗜 𝗗𝗘𝗗𝗢 🥺"

@app.on_message(filters.channel)
async def auto_caption(client, message: Message):
    try:
        chat = await client.get_chat(message.chat.id)
        channel_name = f"<b>{chat.title}</b>"
        post_link = f"https://t.me/c/{str(chat.id)[4:]}/{message.id}"
        random_caption = random.choice(CAPTIONS)

        final_caption = (
            f"<blockquote>{channel_name}</blockquote>\n\n"
            f"💬 <b>{random_caption}</b>\n\n"
            f"<blockquote>{post_link}</blockquote>\n\n"
            f"{REACTION_LINE}"
        )

        if message.photo or message.video or message.document:
            await message.edit_caption(final_caption, parse_mode="html")

    except Exception as e:
        print(f"Error: {e}")

app.run()	