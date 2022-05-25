import discord

from typing import Union


def _search_member(suspect: discord.Member, members: list[str]) -> Union[None, tuple]:
    for member in members:
        name, level, experience = member.split()
        if suspect.__str__() == name:
            return int(level), int(experience)

    return None


async def add_new_member(member: discord.Member, channel: discord.TextChannel):
    with open("LEVELS.txt", "r") as file:
        member_levels = file.readlines()
        search = _search_member(member, member_levels)
        if search:
            await channel.send(f"Ваш уровень {search[0]}, ваш exp {search[1]}")
            return

    with open("LEVELS.txt", "a") as file:
        print(member, 0, 0, file=file)
    # cистема уровней: сначала у человека 0 уровень, 0 хр, потом с каждым следующим уровнем количество необходимого хр
    # будет увеличиваться в 1.5 раза, максимальный уровень - 30.


async def levels_system(member: discord.Member, message: discord.Message):
    with open("LEVELS.txt", "r") as file:
        member_levels = file.readlines()
        search = _search_member(member, member_levels)
        x = 100
        while search[0] != 30:
            if search[1] == x:
                search[0] += 1
                x *= 1.5
                search[1] *= 0
            if message.content.lower():
                search[1] += 5







