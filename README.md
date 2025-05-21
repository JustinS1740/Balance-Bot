# Marvel Rivals Balance Bot 🤖

A Discord bot that automatically announces new **balance patch posts** from the [Marvel Rivals](https://www.marvelrivals.com/balancepost/) website. The bot is designed to run periodically, check for updates, and notify a designated channel only when a new patch is released.

---

## 📌 Project Purpose

I built this bot to automate the process of tracking balance changes in *Marvel Rivals*, a game I actively follow. Rather than manually checking the website for updates (which can happen unpredictably every few weeks or months), the bot monitors the official site and posts an announcement directly in my personal Discord server.

This bot serves as a **useful alert system** for my gaming group and a **learning project** for building bots and web scrapers with Python.

---

## 🧠 What I Learned

Through this project, I gained hands-on experience with:

- ✅ **Python web scraping** using `aiohttp` and `BeautifulSoup`
- ✅ **Async programming** with `asyncio` and `discord.py`
- ✅ **HTML parsing** to extract dynamic content from websites
- ✅ **Environment variable handling** using `python-dotenv` for sensitive data like bot tokens
- ✅ **Deploying bots** on mini server infrastructure like Raspberry Pi for 24/7 uptime
- ✅ **Debugging real-world issues** like selector mismatches, HTML changes, and bot hosting

---

## ⚙️ Tech Stack

- **Python 3.10+**
- [discord.py](https://pypi.org/project/discord.py/)
- [aiohttp](https://pypi.org/project/aiohttp/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Hosted on: **Raspberry Pi 4**

---

## 🚀 How to Runs

```bash
# Clone the project
git clone https://github.com/your-username/marvel-rivals-balance-bot.git
cd marvel-rivals-balance-bot

# Create a .env file with your Discord bot token and channel ID
DISCORD_TOKEN=your_token_here
DISCORD_CHANNEL_ID=your_channel_id_here

# Run the bot
python main.py
