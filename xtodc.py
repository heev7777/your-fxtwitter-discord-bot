import discord
from discord.ext import commands
import re
from urllib.parse import urlparse, urlunparse

# Made by https://twitter.com/SkillG_

# Define the intents your bot needs
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to access message content

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to be triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

# Event to be triggered whenever a message is sent
@bot.event
async def on_message(message):
    # Check if the message is sent by a bot to avoid infinite loops
    if message.author.bot:
        return

    # Regular expression to match x.com URLs with query parameters
    xcom_url_pattern = re.compile(r'https://x\.com/(\S+)/status/(\d+)(\S*)')

    # Regular expression to match Twitter URLs with query parameters
    twitter_url_pattern = re.compile(r'https://twitter\.com/(\S+)/status/(\d+)(\S*)')

    # Check if the message contains a x.com URL
    match_xcom = xcom_url_pattern.search(message.content)
    if match_xcom:
        # Extract the username, status ID, and any remaining path or query parameters
        username = match_xcom.group(1)
        status_id = match_xcom.group(2)
        remaining_path_and_query = match_xcom.group(3)

        # Construct the modified URL without query parameters
        modified_url = f'https://fxtwitter.com/{username}/status/{status_id}{remaining_path_and_query}'
        
        # Remove query parameters from the URL
        parsed_url = urlparse(modified_url)
        modified_content = urlunparse(parsed_url._replace(query=''))

        # Send the modified message back to the channel
        await message.channel.send(f'{message.author.mention}, I modified your x.com link:\n{modified_content}')

    # Check if the message contains a Twitter URL
    match_twitter = twitter_url_pattern.search(message.content)
    if match_twitter:
        # Extract the username, status ID, and any remaining path or query parameters
        username = match_twitter.group(1)
        status_id = match_twitter.group(2)
        remaining_path_and_query = match_twitter.group(3)

        # Construct the modified URL without query parameters
        modified_url = f'https://fxtwitter.com/{username}/status/{status_id}{remaining_path_and_query}'
        
        # Remove query parameters from the URL
        parsed_url = urlparse(modified_url)
        modified_content = urlunparse(parsed_url._replace(query=''))

        # Send the modified message back to the channel
        await message.channel.send(f'{message.author.mention}, I modified your Twitter link:\n{modified_content}')

    # Allow other event handlers to process the message
    await bot.process_commands(message)

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
