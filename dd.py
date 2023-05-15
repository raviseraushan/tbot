from pyrogram import Client, filters, enums
import yt_dlp as youtube_dl
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
opts = {"format": "best", 'flat_playlist': True, "addmetadata": True, "key": "FFmpegMetadata", "prefer_ffmpeg": True, "geo_bypass": True, "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}], "outtmpl": "%(title)s.mp4", "logtostderr": False, "quiet": True, }


bot = Client("youtube_xtd", parse_mode=enums.ParseMode.MARKDOWN)


@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Hey, I wana miss You!")


@bot.on_message(filters.command('me') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "This is a ReplyKeyboardMarkup example",
                     reply_markup=ReplyKeyboardMarkup(
                         [
                             ["💌Anime💌"],  # First row
                             ["💺Hollywood💺"],  # Second row
                             ["🧳Bollywood🧳", "South"],  # Third row
                             [">> Back"]  # Fourth row
                         ],
                         resize_keyboard=True  # Make the keyboard smaller
                     ))


@bot.on_message(filters.command('test'))
def com(bot, message):
    bot.send_message(message.chat.id, "This is a InlineKeyboardMarkup example",
                     reply_markup=InlineKeyboardMarkup(
                         
                             [  # First row
                                 InlineKeyboardButton(  # Generates a callback query when pressed
                                     "Button",
                                     callback_data="data"
                                 ),
                                 InlineKeyboardButton(  # Opens a web URL
                                     "JSON File",
                                     url="https://docs.pyrogram.org"
                                 ),
                             ]
                         
                     ))


@bot.on_message(filters.command('help'))
def command2(bot, message):
    message.reply_text(f'''
**bold**

__italic__

--underline--

~~strike~~

||spoiler||

[text URL](https://pyrogram.org/)

[text user mention](tg://user?id=123456789)

`inline fixed-width code`

```
pre-formatted
  fixed-width
   code block
```

```python
pre-formatted
  fixed-width
   code block
with language
```''')


@bot.on_message(filters.command('img'))
def command2(bot, message):
    bot.send_photo(message.chat.id, 'https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=clement-m-F_-0BxGuVvo-unsplash.jpg')

@bot.on_message(filters.command('doc'))
def command2(bot, message):
    bot.send_document(
        message.chat.id, 'BQACAgUAAxkBAAIByWRKQhxSCtA-ENh9v7SWYnqqRDy-AAJYEAACbrJJVmFLh_c3MlcJHgQ')
    
@bot.on_message(filters.document)
def command2(bot, message):
    message.reply(f"`{message.document.file_id}`")
    # await bot.download_media(message.video.file_id,)
@bot.on_message(filters.text & filters.private)
def command3(bot,message):
    if "playlist" in message.text:
        message.reply(message.text.replace(
            "https://www.youtube.com/playlist?list=", ""))
    elif "𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !" in message.text:
        c=[]
        for i in message.text.split('𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 !')[1:]:
            c.append(i.split('✨ Dᴏᴡɴʟᴏᴀᴅ :')[1].split('\n')[0].replace(' ','')+'\n')
            
        f=open("download.txt",'w')
        f.writelines(c)
        f.close()
        message.reply(c)
        bot.send_document(message.chat.id,'download.txt',caption="document caption")
        
    elif "you" in message.text:
        with youtube_dl.YoutubeDL(opts) as ydl:
            info_dict = ydl.extract_info(message.text, download=False)
            bot.send_photo(
                message.chat.id, f"https://img.youtube.com/vi/{info_dict['id']}/maxresdefault.jpg", info_dict['title'])
            for i in info_dict['formats']:
                if "audio_channels" in i:
                    if i['audio_channels'] == 2:
                        if i['resolution'] != 'audio only':
                            formatNote = i['format_note']
                            ext = i['video_ext']
                            durl = i['url']
                            message.reply(
                                f'''[Download your video in {formatNote}]({durl})''')
    else:
        message.reply_text(message.text)


# welcome bot


print("I am Running.....")
bot.run()