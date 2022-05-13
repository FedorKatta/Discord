import discord

from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_task.start()

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
        if message.content.lower() == "стоп":
            await message.channel.send("Кибератака завершена")
            _Spam.setIsStatusSpam(True)
        if message.content.lower() == "старт":
            await message.channel.send("Начинаю кибератаку")
            _Spam.setIsStatusSpam(False)

    @tasks.loop(seconds=5)
    async def background_task(self):
        # await self.get_channel(888702867244978221).send(self.get_user(722516249002901547).mention)
        if _Spam.getIsStatusSpam() == False:
            await self.get_channel(862661837043925015).send(self.get_user(722516249002901547).mention(self.user))


    @background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

class Spam():

  def __init__(self):
    self.isStop: bool = False

  def setIsStatusSpam(self, arg: bool = True):
    self.isStop = arg

  def getIsStatusSpam(self):
    return self.isStop





client = MyClient()

if __name__ == "__main__":
    _Spam = Spam()
    client.run(getenv("token"))

