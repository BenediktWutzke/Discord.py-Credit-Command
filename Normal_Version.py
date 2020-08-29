import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix="$")

@client.command()
async def credits(ctx):
    with open("users.json") as file:
        users = json.load(file)

    credit_message = ""
    for user in users:
        name = users[str(user)]["Name"]
        if name is None or name == "":
            name = None

        social_links = users[str(user)]["Social Links"]
        if social_links is None or social_links == "":
            social_links = None

        description = users[str(user)]["Description"]
        if description is None or description == "":
            description = None

        credit_message = credit_message + f"Name: {name}\n"
        credit_message = credit_message + f"Social Links: {social_links}\n"
        credit_message = credit_message + f"Description: {description}\n\n"

    embed = discord.Embed(title="Credits", description=credit_message, color=0xff9e00)
    await ctx.send(embed=embed)

client.run("TOKEN")