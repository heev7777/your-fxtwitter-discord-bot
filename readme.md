# Discord Bot for Modifying Links

Purpose of this bot is to modify certain URL links in messages sent by users. It specifically targets links from `https://x.com/` and `https://twitter.com/`, replacing them with `https://fxtwitter.com/`. So with that you can freely share your funny twitter links to your friends with embeded images and videos.
Why the hek they don't have embeds for twitter links in discord? I don't know, but this bot fixes that. Tested only with python version 'python 3.10' on windows machine.

## Prerequisites

- Python 3.x installed
- Discord.py library (`pip install discord`)

## Setup

1. Clone the repository:

   git clone https://github.com/heev7777/your-fxtwitter-discord-bot.git

2. Navigate the project repository

   cd your-fxtwitter-discord-bot

3. open terminal and pip install the requirements

   pip install discord

4. Create a new application and bot account on [Discord Developer Portal](https://discord.com/developers/applications)      
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
   - Go to the Bot tab and click Add Bot.
   - Click on the Copy button under the TOKEN section to copy your bot's token.
   - Paste the token into the bot.run('YOUR_BOT_TOKEN') section in the code.
   - Go to the OAuth2 tab and select `bot` in the scopes section.
   - Select the permissions you want your bot to have. For this bot, you will need to select the `Send Messages` and `Read Message History` permissions under the Text Permissions section.
   - Copy the URL and paste it into your browser. Select the server you want to add the bot to and click Authorize.
   - Also you may need to enable `Privileged Gateway Intents` in the Bot tab.

5. Run the bot

   python xtodc.py

   ## Usage

    - The bot will automatically run when you run the xtodc.py file.

## License
This project is licensed under the MIT License.