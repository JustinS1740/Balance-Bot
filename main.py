from dotenv import load_dotenv
import os
import discord
import asyncio
import aiohttp
import re
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1341637989452873799
URL = "https://www.marvelrivals.com/news/"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_seen_post = None

TEST_MODE = False
TEST_POST_FILE = "test.txt"

async def fetch_latest_post():
    if TEST_MODE: # test for updated post
        try:
            with open(TEST_POST_FILE, "r") as f:
                link = f.read().strip()
                if link:
                    date_str = link.split("/")[4]
                    title = f"Marvel Rivals Balance Post {date_str}"
                    return (title, link)
        except Exception as e:
            print(f"Error reading test post file: {e}")
        return None
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                if resp.status != 200:
                    print(f"Failed to fetch page, status: {resp.status}")
                    return None
                
                html = await resp.text()
                
                match = re.search(r'href="(https://www\.marvelrivals\.com/balancepost/\d{8}/\d+_\d+\.html)"', html)
                if match:
                    link = match.group(1)
                    date_str = link.split("/")[4]
                    title = f"Marvel Rivals Balance Post {date_str}"
                    return (title, link)
        return None
        
async def check_for_updates():
    global last_seen_post
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        latest = await fetch_latest_post()
        if latest and latest != last_seen_post:
            last_seen_post = latest
            title, link = latest
            await channel.send(f"**🚨New Balance Post🚨**\n**{title}**\n🔗 {link}")
        await asyncio.sleep(21600) # Checks every 6 hours

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

async def main():
    async with client:
        asyncio.create_task(check_for_updates())
        await client.start(TOKEN)
        
asyncio.run(main())