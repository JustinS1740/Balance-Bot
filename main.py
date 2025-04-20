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
URL = "https://www.marvelrivals.com/balancepost/"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_seen_post = None

async def fetch_latest_post():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            if resp.status != 200:
                print(f"Failed to fetch page, status: {resp.status}")
                return None
            
            html = await resp.text()
            '''soup = BeautifulSoup(html, "html.parser")

            post = soup.find('a', class_="list_item")
            if post:
                title = post.get_text(strip=True)
                link = post["href"]
                return(title, link)
            return None'''
            match = re.search(r'Marvel Rivals Version (\d{8}) Balance Post.*?href="([^"]+)"', html, re.DOTALL)
            if match:
                date_str, link = match.groups()
                title = f"Marvel Rivals Version {date_str} Balance Post"
                if not link.startswith('http'):
                    link = f"https://www.marvelrivals.com{link}"
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
        await asyncio.sleep(300) # Checks every 5 minutes

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

async def main():
    async with client:
        asyncio.create_task(check_for_updates())
        await client.start(TOKEN)
        
asyncio.run(main())