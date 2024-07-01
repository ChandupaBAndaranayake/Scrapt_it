import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import tasks, commands

# Function to get latest uploads from TorrentGalaxy
def get_latest_uploads():
    url = 'https://torrentgalaxy.to/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section containing latest uploads
    latest_uploads_section = soup.find('div', {'class': 'new-movies'})
    latest_uploads = latest_uploads_section.find_all('a', {'class': 'card'})

    uploads = []
    for upload in latest_uploads[:4]:  # Get the first 4 uploads
        title = upload.get('title')
        link = upload.get('href')
        uploads.append((title, url + link))
    
    return uploads


# Discord bot token
TOKEN = 'Token of the discord'
# Discord channel ID where you want to send the notifications
CHANNEL_ID = "channelID"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    check_new_uploads.start()
    print(f'Logged in as {bot.user}')

@tasks.loop(hours=1)
async def check_new_uploads():
    uploads = get_latest_uploads()
    channel = bot.get_channel(CHANNEL_ID)
    for title, link in uploads:
        await channel.send(f'New Upload: {title} - {link}')

bot.run(TOKEN)
