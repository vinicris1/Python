import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

discord_token = ''

a = 0
lov = ['Te amo amor :heart:', 'Você é a mais gostosa de todo o mundo :heart_on_fire:', "Te macetaria firme neste momento :wood: :hammer:"]

@bot.command()
async def lovHelp(ctx):
     await ctx.send("```Comandos disponiveis: \n /teste - mostra quantas vezes o comando foi digitado \n /vibs - mensagens de amor pra vibs \n /amor - imagem de amor pra vibs \n /amor1 [Numero da imagem] - imagem de amor pra vibs com seleção \n /clean [quantidade] - limpa a quantidade desejadas de mensagens do canal\n```") 

@bot.command()
async def teste(ctx):
    global a
    a = a + 1
    await ctx.send(":otter: {}".format(a))

@bot.command()
async def vibs(ctx):
        global lov
        rand_lov = random.choice(lov)
        await ctx.send("{}".format(rand_lov))

file_path = ['images\linda.png','images\linda2.jpg','images\linda3.png','images\linda.jpg','images\linda5.jpg', 'images\linda6.png','images\linda7.png','images\linda8.jpg']

@bot.command(pass_context = True)
async def amor(ctx):
    global file_path
    rand_path = random.choice(file_path)
    await ctx.send(file=discord.File(rand_path))

@bot.command(pass_context = True)
async def amor1(ctx, message):
     global file_path
     await ctx.send(file=discord.File(file_path[int(message)]))

@bot.command()
async def clean(ctx, quantidade: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=quantidade + 1)
        await ctx.send(f"{quantidade} mensagens foram apagadas por {ctx.author.mention}.", delete_after=1)
    else:
         await ctx.send("Você não tem permissão para apagar mensagens neste canal.")

bot.run(discord_token)