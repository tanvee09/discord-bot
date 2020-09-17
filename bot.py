import discord
from discord.ext import commands
import random
from get_from_reddit import get_posts
import animal_images


TOKEN = '<INSERT YOUR TOKEN HERE>'
client = commands.Bot(command_prefix = '&')


client.remove_command('help')


@client.command()
async def ping(ctx) :
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ')


@client.command()
async def quote(ctx) :
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)


@client.command()
async def meme(ctx) :
    await ctx.send(get_posts('meme'))        


@client.command()
async def programmerHumor(ctx) :
    await ctx.send(get_posts('ProgrammerHumor'))     


@client.command()
async def dadJoke(ctx) :
    await ctx.send(get_posts('DadJokes'))


@client.command()
async def dankMeme(ctx) :
    await ctx.send(get_posts('dankmemes'))


@client.command()
async def historyMeme(ctx) :
    await ctx.send(get_posts('historymemes'))


@client.command()
async def showerThoughts(ctx) :
    await ctx.send(get_posts('Showerthoughts'))


@client.command()
async def dog(ctx) :
    await ctx.send(animal_images.dog())


@client.command(pass_context=True)
async def greet(ctx, *args) :
    greet = ['Heya', 'Hello', 'Hi', 'Henlo']
    insult = ['useless', 'dumb', 'idiot', 'stupid']
    if len(args) == 0 :
        person = ctx.message.author.mention
    else :
        person = ' '.join(args)
    await ctx.send(random.choice(greet) + ', ' + person + '! My ' + random.choice(insult) + ' friend!')


@client.command(pass_context = True)
async def help(ctx) :
    embed = discord.Embed(color = discord.Color.green())
    embed.set_author(name = 'Help : list of commands available')
    embed.add_field(name='&ping', value='Returns bot responds time in milliseconds', inline=False)
    embed.add_field(name='&greet <x>', value='Make bot greet x', inline=False)
    embed.add_field(name='&quote', value='Get inspired by a powerful quote', inline=False)
    embed.add_field(name='&meme', value='Get memes from reddit', inline=False)
    embed.add_field(name='&programmerHumor', value='Get memes on programmers and programming from reddit', inline=False)
    embed.add_field(name='&dankMeme', value='Get dank memes from reddit', inline=False)
    embed.add_field(name='&historyMeme', value='Get history memes from reddit', inline=False)
    embed.add_field(name='&dadJoke', value='Get dad jokes from reddit', inline=False)
    embed.add_field(name='&showerThoughts', value='Get thoughts & ideas to keep you thinking.', inline=False)
    embed.add_field(name='&dog', value='Get random dog images and videos', inline=False)
    await ctx.send(embed=embed)
    

@client.event
async def on_command_error(ctx, error) :
    if "Command" in f'{error}' and "not found" in f'{error}' :
        await ctx.send('The command you are trying is not currently available.')
    else :
        await ctx.send('There has been some problem at our end. We will try to repair it as soon as possible.')


client.run(TOKEN)