import discord
import action
import sys

async def send_message(message, user_message, is_private):
    try:
        response = action.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def get_Token():
    a = ""
    with open("C:/Users/DanK/Documents/bots/gotcha/token.txt") as f:
        a = f.readline()
        return a



def run_discord_bot():
    TOKEN = get_Token()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user}' is now running! Time to collect them all")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        else:
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            print(f'{username} said: "{user_message}" in {channel}')
            
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)