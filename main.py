# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use
# Modified by GH/WolverinexD 
from anonfile import AnonFile
import os, glob
from os import error
import logging
import pyrogram
import time
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document

    
bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING = """ Hi {}, I'm Anonymous File bot. 
 """


JOIN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')
        ]]
    )

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_STRING.format(update.from_user.mention)
    reply_markup = JOIN_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message(filters.command(["ping"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@bughunter0.on_message(filters.private & filters.command(["upload"]))
async def uploadfile(bot, message):  
    tx = await message.reply_text("Checking File...")    
    tx.edit("Downloading...")
    file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.zip"
    await message.reply_to_message.download(file_path)  
    await tx.edit("Downloaded") 
    anon = AnonFile()
    upload = anon.upload('file_path', progressbar=False)
    await tx.edit("Uploading...")
    start = time.time()
    await message.reply_text("URL : {upload.url.geturl()}")
    await tx.delete()   
    os.remove(file_path)
    #   os.remove(zip_path)
    except Exception as e:
        print(e)
        await message.reply_text("Error : {e}")

@bughunter0.on_message(filters.private & filters.command(["clearcache"]))
async def clearcache(bot, message):   
    # Found some Files showing error while Uploading, So a method to Remove it !!  
    txt = await message.reply_text("Checking Cache")
    await txt.edit("Clearing cache")
    dir = DOWNLOAD_LOCATION
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist :
           i =1
           os.remove(f)
           i=i+1
    await txt.edit("Cleared "+ str(i) + "File") 
    await txt.delete()
    

      
bughunter0.run()
