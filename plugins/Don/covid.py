import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("✘ ᴄʟᴏsᴇ ✘", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/0c14a59310d29ccfcc7fa.jpg",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Cᴏᴠɪᴅ 𝟷𝟿 Iɴғᴏʀᴍᴀᴛɪᴏɴ**--
**᚛› Cᴏᴜɴᴛʀʏ : {country}
᚛› Aᴄᴛɪᴠᴇᴅ : {active}
᚛› Cᴏɴғɪʀᴍᴇᴅ : {confirmed}
᚛› Dᴇᴀᴛʜs : {deaths}
᚛› ID : {info_id}
᚛› Lᴀsᴛ Uᴘᴅᴀᴛᴇ  : {last_update}
᚛› Lᴀᴛɪᴛᴜᴅᴇ : {latitude}
᚛› Lᴏɴɢɪᴛᴜᴅᴇ : {longitude}
᚛› Rᴇᴄᴏᴠᴇʀᴇᴅ : {recovered}**"""
        return covid_info
    except Exception as error:
        return error
