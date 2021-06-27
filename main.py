import os 
from os import error
import logging
import pyrogram
import time
import random
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

    
bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING = """ Hi {}, I'm Sticker Bot. 

I can Provide all Kind of Sticker Options Here """


JOIN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')
        ]]
    )

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


@bughunter0.on_message(filters.private & filters.command(["getsticker"]))
async def getsticker(bot, message):  
    random_id = random.randint(100,1000)         
    tx = await message.reply_text("Checking Sticker")
    if message.reply_to_message is None: 
       tx =  await tx.edit("Reply to a Sticker File!")       
    else : 
       if message.reply_to_message.sticker.is_animated is False:        
          try : 
               await tx.edit("Downloading..")
               file_path = f"./DOWNLOADS/{message.chat.id}-{random_id}.png"
               await message.reply_to_message.download(file_path)   
               await tx.edit("Uploading..")
               await message.reply_document(file_path)
               await tx.delete()   
               os.remove(file_path)
          except Exception as error:
            print(error)

       elif sticker.is_animated :
         try :
              await tx.edit("Downloading..")
              file_path = f"./DOWNLOADS/{message.chat.id}-{random_id}.gif"
              await message.reply_to_message.download(file_path)   
              await tx.edit("Uploading..")
              await message.reply_document(file_path)
              await tx.delete()   
              os.remove(file_path)
         except Exception as error:
            print(error)

@bughunter0.on_message(~filters.command(["stickerid"]) & (filters.private | filters.forwarded) & filters.sticker)
async def stickerid(bot, message):   
    if reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.sticker.file_unique_id}`", quote=True)

 
bughunter0.run()
