import discord

from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())


class MyClient(discord.Client):
    @staticmethod
    async def on_ready():
        print("Bot is ready")

    async def on_message(self, message: discord.Message):
        """Проверяет, пишет человек или бот"""
        if message.author == self.user:
            return
        """Проверяет, что написал человек и отвечает"""
        if message.content == "Привет":
            await message.channel.send("Привет")


client = MyClient()

if __name__ == "__main__":
    client.run(getenv("token"))
