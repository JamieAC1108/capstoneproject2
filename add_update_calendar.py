import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()
# თქვენი credentials
DISCORD_TOKEN = os.getenv('discord_token')

# UVDesk API config
UVDESK_API_URL = "https://your-uvdesk-domain.com/en/api/tickets.json"
UVDESK_API_KEY = os.getenv('apikey')
UVDESK_API_SECRET = os.getenv('apisecret')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

PREFIX = "!ticket"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Check prefix
    if message.content.startswith(PREFIX):
        ticket_content = message.content[len(PREFIX):].strip()

        if not ticket_content:
            await message.channel.send("Please include a message after !ticket")
            return

        # Prepare UVDesk payload
        payload = {
            "from": message.author.email if hasattr(message.author, "email") else "student@example.com",
            "subject": f"Discord Ticket from {message.author}",
            "message": ticket_content,
            "name": str(message.author)
        }

        # Send to UVDesk
        try:
            response = requests.post(
                UVDESK_API_URL,
                data=payload,
                auth=(UVDESK_API_KEY, UVDESK_API_SECRET)
            )

            if response.status_code == 200:
                await message.channel.send("✅ Ticket created successfully!")
            else:
                await message.channel.send(f"❌ Failed to create ticket: {response.text}")

        except Exception as e:
            await message.channel.send(f"⚠️ Error: {str(e)}")

client.run(DISCORD_TOKEN)
