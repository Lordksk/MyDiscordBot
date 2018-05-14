import discord
from discord.ext import commands
import asyncio
import random
import os

client = commands.Bot(command_prefix="k!")

userIDforClr = ["300868677429886976"]
help_msg = "Toss\nClr\nrps rock|paper|scissor\ncredits\ncmds\ntimer SEC|MINS"
credits_msg= "Kushurox aka Kushal\nJackaboi (his yt:https://www.youtube.com/channel/UCNp8BvJDLjsxFwl97FgDX7A)"
restricted_words = ["FUCK","WTF","FUK","GAY","STFU","NAVYA","BOBS","BOB"]
count = 0
four = 4 #Bruhh of course

@client.event
async def on_ready():
    print("{0.user.name} with an id {1.user.id} logged in!".format(client,client))
    await client.change_presence(game=discord.Game(name="with my k!cmds"))
@client.command()
async def toss():
    k = random.randint(0,1)
    if k == 0:
        await client.say("Heads")
    else:
        await client.say("Tails")

@client.command(pass_context=True)
async def clr(ctx):
    if ctx.message.author.id not in userIDforClr:
        warningembed = discord.Embed(description="You Dont Have The Perms!!!", colour=discord.Color.red())
        warningembed.set_author(name="kushBot")
        await client.say(embed=warningembed)
    else:
        try:
            args = ctx.message.content.split(" ")
            number = int(args[1])
            await client.purge_from(ctx.message.channel, limit=number)
        except ValueError:
            await client.say("Only numbers!!!")
        except IndexError:
            await client.say("Please Provide a Valid argument (int)")
        except discord.HTTPException:
            await client.say("Limit 0 - 100")
@client.command(pass_context=True)
async def rps(ctx):
    k = random.randint(0,2)
    args = ctx.message.content.split(" ")
    try:
        if args[1].upper() == "ROCK" or args[1].upper() == "SCISSOR" or args[1].upper() == "PAPER":
            if k == 0:
                await client.say("<@{0.message.author.id}> you win :D !".format(ctx))
            elif k == 1:
                await client.say("<@{0.message.author.id}> Tie :| !".format(ctx))
            else:
                await client.say("<@{0.message.author.id}> You Lose ;( !".format(ctx))
        else:
            await client.say("Invalid Arguments try k!help")
    except IndexError:
        await client.say("No Arguments Provided try k!help")
@client.command()
async def cmds():
    helpembed = discord.Embed(description=help_msg, colour=discord.Color.blue())
    helpembed.set_author(name="KushBot")
    await client.say(embed=helpembed)

@client.command()
async def credits():
    creditsembed = discord.Embed(description=credits_msg, colour=discord.Color.purple())
    creditsembed.set_author(name="Kushbot")
    await client.say(embed=creditsembed)
@client.event
async def on_message(message):
    k = message.content.upper().split(" ")
    for j in k:
        if j in restricted_words:
            await client.delete_message(message)
            await client.send_message(message.channel, "<@%s> Such words are not allowed!" % (message.author.id))
            break
    await client.process_commands(message)
@client.event
async def on_member_join(member: discord.Member):
    serverchannel = discord.utils.get(member.server.channels, name="join-leave-messages")
    role = discord.utils.get(member.server.roles, id="366593681396072448")
    await client.add_roles(member, role)
    emb1 = (discord.Embed(description="Yo Welcome to our channel <@%s>\nWant cool ranks please do k!roles" % (member.id), colour=0x3DF270))
    emb1.set_author(name="KushBot")
    await client.send_message(serverchannel, embed=emb1)
@client.event
async def on_member_remove(member: discord.Member):
    serverchannel = discord.utils.get(member.server.channels, name="join-leave-messages")
    meml = member.name
    embl = (discord.Embed(description= meml+" has left T_T.He/she/it doesn't knows the value of this server", colour=0x3DF170))
    embl.set_author(name="KushBot")
    await client.send_message(serverchannel, embed=embl)

@client.command(pass_context=True)
async def timer(ctx, units = "none", amount :int = -1, *, reason = " "):
    
    if amount == -1:
        await client.say("Invalid Argument try for k!help or k!cmds")
        return False
    elif amount == 0:
        await client.send_message(ctx.message.author, "Are you a fool????")
        return False
    elif units == "none":
        await client.send_message(ctx.message.channel, "Invalid Argument try k!help or k!cmds")
        return False
    elif units.upper() == "MINS":
        await client.send_message(ctx.message.author, "No worries do your job ill Remind you :wink:\nReason:" + reason)
        await asyncio.sleep(amount * 60)
        await client.send_message(ctx.message.author, "Timer is done get back!\nReason:" + reason)
    elif units.upper() == "SEC":
        await client.send_message(ctx.message.author, "No worries do your job ill Remind you :wink:\nReason:" + reason)
        await asyncio.sleep(amount)
        await client.send_message(ctx.message.author, "Timer is done get back!\nReason:" + reason)
    else:
        await client.say("Something is wrong")







        

client.run(os.getenv('TOKEN'))
