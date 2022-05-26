"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "<i>**🙂 Yᴏᴜ Aʀᴇ Nᴏᴛ Dᴇᴀᴅ.Yᴏᴜ Aʀᴇ Sᴛɪʟʟ Hᴇʀᴇ.Yᴏᴜ Hᴀᴠᴇ Nᴏ Lᴏᴠᴇ Fᴏʀ Mᴇ Nᴏᴡ Oᴋᴀʏ ❤️... Yᴏᴜ'ʀᴇ Nᴏᴛ Cʜᴀɴɢᴇᴅ Lɪᴋᴇ Yᴏᴜ Usᴇᴅ Tᴏ Bᴇ...Jᴜsᴛ Sᴛᴀʀᴛ**</i> 🥰 /start <i><b>Oɴᴇ Aᴛ A Tɪᴍᴇ...</b></i>"
REPO = "<i><b>Tʜɪs Nᴏᴛᴇ A Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏɪᴇᴄᴛ 😋 </b></i>"
CHANNEL = "<i><b>🥰 Uᴘᴅᴀᴛᴇs ›› [Mᴏᴠɪᴇs𝟺ʏᴏᴜBᴀᴄᴋᴜᴘ](https://t.me/Movies4youBackup)</b></i>\n\n<i><b>😇 Gʀᴏᴜᴘ ›› [Mᴏᴠɪᴇs 4 ʏᴏᴜ](https://t.me/Movies_4you)</b></i>\n\n<i><b>😎 Mʏ Fᴀᴛʜᴇʀ ›› [會؄𝚂𝚄𝚁𝙰𝙹؄會](https://t.me/KingOf_univers)</b></i>"
JOKER = "<b>Mᴇʟᴏᴅʏ ›› http://t.me/Melody_AutoFilterBot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("melody", COMMAND_HAND_LER) & f_onw_fliter)
async def joker(_, message):
    await message.reply_text(JOKER)




