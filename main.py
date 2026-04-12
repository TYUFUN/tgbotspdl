import asyncio
import os
from os import rename, remove
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from pytubefix import Search, YouTube
load_dotenv()
Token = os.getenv("Token")
if not Token:
    exit("Error: BOT_TOKEN not found in environment variables!")
bot = Bot(token=Token)
dp = Dispatcher()
count = 0
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello! I'm a bot for downloading music from Spotify. 🎵\n\n"
    "How it works* Just send me a link to a Spotify song, "
    "wait a few seconds, and you'll get your m4a file!")
    await message.answer("Please join our Telegram channel! If you have any problems, "
    "you can find solutions there:\nhttps://t.me/TYUFUNTG")

@dp.message(Command('tg'))
async def help(message: Message):
    await message.answer("https://t.me/TYUFUNTG")
    
@dp.message(F.text.startswith("http"))
async def link(message: Message):
    try:
        global count
        oss = await message.answer("working...🛠️")
        h = {'User-Agent': 'facebookexternalhit/1.1'}
        request = requests.get(message.text, headers=h)    
        soup = BeautifulSoup(request.text, 'html.parser')
        song_name1 = soup.title.string.replace(" | Spotify", "").replace(" - song by", " -")
        song_name = song_name1.split(" - song")[0] 
        results = Search(song_name)
        for song in results.videos:
            url = song.watch_url
            name = song.title
            break
    except Exception:
        await message.answer("Something went wrong. Please try again. If the issue still continues, try a different song or contact the developer.")
    try:
        yt = YouTube(song.watch_url)
        k = yt.streams.filter(only_audio=True, file_extension='mp4')[-1]
        k.download()
        for audio_file in os.listdir("."):
           if audio_file.endswith(".m4a"):
               count = count + 1
               temporary = f"song" + str(count) + ".m4a"
               rename(audio_file, temporary)
               sent = FSInputFile(temporary, name + ".m4a")
               await message.answer_audio(sent)
               await bot.delete_message(chat_id=message.chat.id, message_id=oss.message_id)
               remove(temporary)
    except Exception:
        await bot.delete_message(chat_id=message.chat.id, message_id=oss.message_id)
        
        for f in os.listdir("."):
           if f.endswith(".m4a"):
                remove(f)
        await message.answer("Something went wrong. Please try again. If the issue still continues, try a different song or contact the developer.")
    
    
async def main():
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        pass