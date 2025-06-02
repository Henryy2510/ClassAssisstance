import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename = 'discord.log', encoding = 'utf-8', mode = 'w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)

role_list = "12A"  

"""  
Event (các thông báo tự động của Bot)
"""
# thông báo btvn
# thống kê thiếu btvn

# thống kê điểm danh onl

@bot.event
async def on_ready():
    print(f"Chào mừng bạn học mới, {bot.user.name}")

@bot.event
async def btvn():
    await print()


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if "dm" in message.content.lower():
#         await message.delete()
#         await message.channel.send(f"{message.author.mention} cảnh cáo lần 1") # nên có dict lưu trữ từ ban, và dict lưu thống kê số lần cảnh cáo vào sổ đỏ
#     await bot.process_commands(message)
    
# """
# Command của bot
# """
# # xin nợ bài
# # xin nghỉ
# # đổi lớp

# @bot.command()
# async def content(ctx):
#     await ctx.send(f"Hello, {ctx.author.mention}!")

# @bot.command()
# async def assign(ctx): 
#     role = discord.utils.get(ctx.guild.roles, name = role_list)
#     if role: 
#         await ctx.author.add_roles()
#         await ctx.send(f"{ctx.author.mention} is now assigned to {role_list[ctx]}")
#     else:
#         await ctx.send("Role do not exist or there is an error!")

# @bot.command()
# async def remove(ctx):
#     role = discord.utils.get(ctx.guild.roles, name = role_list)
#     if role: 
#         await ctx.author.remove_roles()
#         await ctx.send(f"{ctx.author.mention} is removed from {role_list[ctx]}")
#     else:
#         await ctx.send("Role do not exist or there is an error!")

# @bot.command()
# @commands.has_role("12A")
# async def secret(ctx):
#     await ctx.send("Welcome tho the class!")

# @secret.error
# async def secret_error(ctx, error):
#     if isinstance(error, commands.MissingRole):
#         await ctx.send("You don't belong to this class")

# @bot.command()
# async def dm(ctx,*,msg):
#     await ctx.author.send(f"You said {msg}")

# @bot.command
# async def reply(ctx):
#     await ctx.reply("This is a reply")

# @bot.command()
# async def poll(ctx,*,question):
#     embed = discord.Embed(title="New Poll", description= question)
#     poll_message = await ctx.send(embed=embed)
#     await poll_message.add_reaction("😇")
#     await poll_message.add_reaction("💀")

bot.run(token, log_handler = handler, log_level = logging.DEBUG)