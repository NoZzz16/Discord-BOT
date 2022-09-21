from discord.ext import commands
import discord
from random import randint
from discord.utils import get
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 311133605101568000  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command() #This is the !name feature
async def name(ctx):
    username = ctx.author.name
    await ctx.send(username)

@bot.command() #This is the !d6 feature
async def d6(ctx):
    rand = randint(1,6)
    await ctx.send(rand)

@bot.event #This is the "Salut tout le monde" feature
async def on_message(message):
    if message.content == "Salut tout le monde" :
        user = message.author.mention
        await message.channel.send(f"Salut tout seul {user}")
    await bot.process_commands(message)

@bot.command(pass_context=True) #Give a role to a member
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, {user.name} made u a : {role.name}")

@bot.command(pass_context=True) #Create the "Admin" role, with all permissions allowed
async def create_role(ctx):
	guild = ctx.guild
	await guild.create_role(name="Admin", permissions=Permissions.all())
	await ctx.send(f'Role Admin has been created')


@bot.command(pass_context=True) #This is the !admin feature
async def admin(ctx, member: discord.Member):
    if get(ctx.guild.roles, name="Admin") :
        await giverole(ctx, member, get(ctx.guild.roles, name="Admin"))
    else :
        await create_role(ctx)
        await giverole(ctx, member, get(ctx.guild.roles, name="Admin"))

@bot.command(pass_context=True) #This is the ban feature
async def ban(ctx, member: discord.Member) :
    await ctx.guild.ban(member, reason="Cheh")
    await ctx.send(f"{member} has been successfully banned.")

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = "MTAyMjE5MzE0NzU3ODY5MTYxNA.GU_4lE.Kci_TVjr4bgUp1cSvA6VIdC7ImM-J40C898-RE"
bot.run(token)  # Starts the bot