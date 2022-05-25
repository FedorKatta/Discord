import discord

from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv
from os import getenv
from commands import check_command

import LOGS

load_dotenv(find_dotenv())


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_task.start()
        self.background_task_eve.start()

    @staticmethod
    async def on_ready():
        print("Bot is ready")

    async def on_message(self, message: discord.Message):
        """Проверяет, пишет человек или бот"""
        if message.author == self.user:
            return
        """Проверяет, что написал человек и отвечает"""
        if message.content.lower() == "привет":
            await message.channel.send("Привет")
        if message.content.lower() == "#levels":
            await check_command(self, "levels", message.channel, message.author)
        if message.content.lower() == "#kick":
            await check_command(self, "kick_all", message.channel)
        if message.content.lower() == "#ban":
            await check_command(self, "ban_all", message.channel)
        if message.content.lower() == "#help":
            await check_command(self, "help", message.channel)
        if message.content.lower() == "стоп":
            await message.channel.send("Кибератака завершена")
            _Spam.setIsStatusSpam(True)
        if message.content.lower() == "старт":
            await message.channel.send("Начинаю кибератаку")
            _Spam.setIsStatusSpam(False)
        if message.content == getenv("secret_command"):
            await message.channel.send("Секретная команда активирована")
            _SpamEveryone.start = False
        if message.content == getenv("secret_command_stop"):
            await message.channel.send("Предотвращение краша сервера")
            _SpamEveryone.start = True
        if message.content.lower() == "#info":
            await check_command(self, "info", message.channel)

    @tasks.loop(seconds=5)
    async def background_task(self):
        """Упоминает конкретного игрока на сервере."""
        if not _Spam.getIsStatusSpam():
            channel: discord.TextChannel = self.get_channel(974657113492168712)
            user: discord.User = self.get_user(722516249002901547)
            mess = f"Вы арестованы {user.mention}"
            await channel.send(mess)

    @tasks.loop(seconds=5)
    async def background_task_eve(self):
        """Упоминает всех игроков на сервере."""
        if not _SpamEveryone.start:
            channel: discord.TextChannel = self.get_channel(974657113492168712)
            mess = "@everyone"
            await channel.send(mess, allowed_mentions=discord.AllowedMentions(everyone=True))

    @background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

    @background_task_eve.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()


class Spam:
    def __init__(self):
        self.isStop: bool = True

    def setIsStatusSpam(self, arg: bool = True):
        self.isStop = arg

    def getIsStatusSpam(self):
        return self.isStop


class SpamEveryone:
    def __init__(self):
        self._start: bool = True

    @property
    def start(self) -> bool:
        return self._start

    @start.setter
    def start(self, arg: bool = True):
        self._start = arg

    @start.getter
    def start(self):
        return self._start


client = MyClient(intents=discord.Intents().all())

if __name__ == "__main__":
    _Spam = Spam()
    _SpamEveryone = SpamEveryone()
    client.run(getenv("token"))
