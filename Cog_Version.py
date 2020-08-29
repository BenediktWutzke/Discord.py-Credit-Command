import discord
import json
from discord.ext import commands

class CreditCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def credits(self, ctx):
        with open("users.json") as file:
            users = json.load(file)

        credit_message = ""
        for user in users:
            credit_message = credit_message + f"Name: {users[str(user)]['Name']}\n"
            credit_message = credit_message + f"Social Links: {users[str(user)]['Social Links']}\n"

            description = users[str(user)]["Description"]
            if description is None or description == "":
                description = None
            credit_message = credit_message + f"Description: {description}\n\n"

        embed = discord.Embed(title="Credits", description=credit_message, color=0xff9e00)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CreditCommand(client))