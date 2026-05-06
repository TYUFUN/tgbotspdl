# 🎵tgbotspdl - telegram bot spotify downloader
![python](https://img.shields.io/badge/python-3.13.5-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-red.svg)](https://choosealicense.com/licenses/mit/)
![bot](https://img.shields.io/badge/BOT-gray?logo=telegram&logoColor=26A5E4)

A Telegram bot that allows you to download Spotify songs by simply sending a link.


## ⚙️ HOW IT WORKS?
The bot extracts the song title and artist from the Spotify link, searches for the audio on YouTube, and delivers the downloaded file directly to you.

## 🌟  DEPLOYMENT
1. run
```
git clone https://github.com/TYUFUN/tgbotspdl
```
2. create file **.env** and write there
```
Token=your_token
```
change *your_token* to token that you get from telegram bot **@BotFather** 
> 📺 [tutorial: how to get telegram token bot](https://www.youtube.com/watch?v=B9VsT7vV6jI)
3. put your **.env** into a folder **tgbot_spt_dwnld**

4. 
install libraries 
```
pip install -r requirements.txt
```
- if you got an error try:

**Windows:**
```
python -m venv venv
venv/Scrips/activate
pip install -r requirements.txt
```
**Linux:**
```
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
```
5. run 
```
python main.py
```
or 
```
python3 main.py
```
## ⚠️ mportant notes:

1. *If you deploy bot on VPS firstly upload folder to the server then or follow instructions that hosting says or follow our instructions (depends of hosting automatization level)*

2. *you must have installed python 3.10+*