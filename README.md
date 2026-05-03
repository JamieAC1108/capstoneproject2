# UVDeskTicket Bot

This discord bot is able to take ticket requests from users via command, and upload them to UVDesk

## Features

Simply type "!ticket" followed by your problem, and the discord bot will create and submit a ticket to UVDesk

## Set up

### Requirements

- Python
- Some sort of IDE (Script was originally in VSCode)
- A virtual environment (optional)
- The necessary installations

### Virtual Environment setup

Run the following in your terminal, preferably the integrated one on your IDE, if you have it. 
    
    - First, make sure you're in the correct directory. This is why we reccomend doing it in your integrated terminal.

    python3 -m venv .venv

    - .venv can be whatever name you'd like for your virtual enviroment, but .venv is common practice

    source .venv/bin/activate

    - These commands will have created a virtual environment for you, and now you should have a (.venv) in front of your directory on the command line. 

### Installations

Run the following PIP commands to install the necessary libraries

    pip install discord.py
    pip install requests
    pip install python-dotenv

### .env

Create your .env file in the same directory as your program. The .env file should contain the following.

    discord_token=your_token_here

To get your token, simply go to the develepor portal for discord, create the bot, and copy that token. 

You should also make sure your bot has the necessary permissions to function, being reading and sending messages.

    apikey=your_uvdesk_key_here
    apilink=your_endpoint_here

To get these, you need admin access to UVDesk. If you have someone with admin access create the API key for you, then your endpoint should look something like

    https://(domain_name).uvdesk.com/api/v1/tickets

This can vary based upon how UVDesk on your network is set up.

### .gitignore

DO NOT SKIP THIS STEP. IF YOU DO, YOU ARE EXPOSING YOUR DISCORD AND UVDESK TO EXPOSURE.

make a file called .gitignore, and in it put the following

    .env
    .venv (if you have a virtual environment)

This will keep your github clean of any security risks

## RUNNING THE BOT

Simply run the code. If you've done everything right, then you should be all set with that.