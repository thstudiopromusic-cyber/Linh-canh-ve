import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} đã sẵn sàng trên đám mây!")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Đã đuổi {member.mention}. Lý do: {reason or 'Không có'}")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
