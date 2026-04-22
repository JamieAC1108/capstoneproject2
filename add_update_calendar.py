import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Load your environment variables
DISCORD_TOKEN = os.getenv('discord_token')
UVDESK_API_URL = os.getenv('apilink')
UVDESK_API_KEY = os.getenv('apikey')

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
    print(f"Message received: {message.content}")  # Debugging print statement
    if message.author.bot:
        return

    if message.content.startswith(PREFIX):
        ticket_content = message.content[len(PREFIX):].strip()

        if not ticket_content:
            await message.channel.send("Please include a message after !ticket")
            return

        # Debugging the content length and structure
        print(f"Ticket Content Length: {len(ticket_content)}")
        print(f"Subject: {f'Discord Ticket from {message.author}'} (Length: {len(f'Discord Ticket from {message.author}')})")

        # Prepare UVDesk payload
        payload = {
            "from": "student@example.com",  # Use a default or a custom method for getting email
            "subject": f"Discord Ticket from {message.author}",
            "message": ticket_content,
            "name": str(message.author)
        }

        # Debug print for payload
        print("Payload being sent to UVDesk:", payload)

        # Send to UVDesk
        try:
            headers = {
                'Authorization': f'Bearer {UVDESK_API_KEY}',
                'Content-Type': 'application/json'  # Change to application/json
            }
            response = requests.post(UVDESK_API_URL, json=payload, headers=headers, verify=False)

            if response.status_code == 200:
                await message.channel.send("✅ Ticket created successfully!")
            else:
                print(f"Error response code: {response.status_code}")
                print(f"Raw error response: {response.text}")  # Print raw response body
                await message.channel.send(f"❌ Failed to create ticket: {response.status_code} - {response.text}")

        except Exception as e:
            await message.channel.send(f"⚠️ Error: {str(e)}")

client.run(DISCORD_TOKEN)