# Done By the Almighty Kushurox helpers:-
# 1]Jackaboi
# I am still working on this
import discord
from discord.ext import commands
import asyncio
import random
import os

client = commands.Bot(command_prefix="k!")

count = 0
help_msg = "Toss\nClr\nrps rock|paper|scissor\ncredits\ncmds\ntimer SEC|MINS\nroles <role name>[optional argument]\nkick\nmute [member] [time OPTIONAL]\nunmute [member]"
credits_msg= "Kushurox aka Kushal\nJackaboi (his yt:https://www.youtube.com/channel/UCNp8BvJDLjsxFwl97FgDX7A)"
restricted_words = ["FUCK","WTF","FUK","GAY","STFU"]
roles_msg = "**ROLES**\npervert\ndark\nsenpai\n\n***NOTE:Please add the roles in the server roles before using these***"
roles_list = ["pervert","dark","senpai"]
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
@commands.has_permissions(administrator=True)
async def clr(ctx, amount="0"):
    try:
        args = int(amount)
        if args == 0:
            await client.say("Please provide a valid argument")
            return False
        elif args < 0:
            await client.say("Please provide an positive integer")
            return False
        else:
            await client.purge_from(ctx.message.channel, limit=args)
            return True
    except ValueError:
        await client.say("Please provide numbers only")
    except discord.HTTPException:
        await client.say("bad request please provide small numbers to prevent such issues")
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
    try:
        serverchannel = discord.utils.get(member.server.channels, name="join-leave-messages")
        role = discord.utils.get(member.server.roles, id="member")
        await client.add_roles(member, role)
        emb1 = (discord.Embed(description="Yo Welcome to our channel <@%s>\nWant cool ranks please do k!roles" % (member.id), colour=0x3DF270))
        emb1.set_author(name="KushBot")
        await client.send_message(serverchannel, embed=emb1)
    except discord.Forbidden:
        serverchannel = discord.utils.get(member.server.channels, name="join-leave-messages")
        emb1 = (discord.Embed(description="Yo Welcome to our channel <@%s>\nWant cool ranks please do k!roles" % (member.id), colour=0x3DF270))
        emb1.set_author(name="KushBot")
        await client.send_message(member.channel, embed=emb1)
    except:
        emb1 = (discord.Embed(description="Yo Welcome to our channel <@%s>\nWant cool ranks please do k!roles" % (member.id), colour=0x3DF270))
        emb1.set_author(name="KushBot")
        await client.send_message(serverchannel, embed=emb1)
@client.event
async def on_member_remove(member: discord.Member):
    try:
        serverchannel = discord.utils.get(member.server.channels, name="join-leave-messages")
        meml = member.name
        embl = (discord.Embed(description= meml+" has left T_T.He/she/it doesn't knows the value of this server", colour=0x3DF170))
        embl.set_author(name="KushBot")
        await client.send_message(serverchannel, embed=embl)
    except:
        meml = member.name
        embl = (discord.Embed(description= meml+" has left T_T.He/she/it doesn't knows the value of this server", colour=0x3DF170))
        embl.set_author(name="KushBot")
        await client.say(embed=embl)
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
@client.command(pass_context=True)
async def roles(ctx, rolename = "none"):
    if rolename == "none":
        rembed = discord.Embed(description=roles_msg, colour=discord.Color.dark_gold())
        rembed.set_author(name="KushBot")
        await client.say(embed=rembed)
    elif rolename in roles_list:
        if rolename not in ctx.message.author.roles:
            role = discord.utils.get(ctx.message.server.roles, name=rolename)
            await client.add_roles(ctx.message.author, role)
            await client.say("**Role set**")
        else:
            role = discord.utils.get(ctx.message.server.roles, name=rolename)
            await client.remove_roles(ctx.message.author, role)
            await client.say("**Role Removed**")
    else:
        await client.say("Role not exisitng.")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, name : discord.Member = "none"):
    try:
        if name == "none":
            await client.say("Who the fish should i kick?")
            return False
        await client.kick(name)
        await client.say("Kicked his ass :wink:")
    except discord.Forbidden:
        await client.say("I lack perms bruhh")
    except:
        await client.say("User not existing")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member = None, minutes = "0"):
    try:
        time = int(minutes)
        if member != None and time == "0":
            try:
                role= discord.utils.get(ctx.message.server.roles, name="Muted")
                await client.add_roles(member, role)
                emb1 = discord.Embed(description="Shut up {0.name} you have been muted\nduration:∞".format(member), colour=discord.Color.blue())
                emb1.set_author(name="KushBot")
                await client.say(embed=emb1)
            except discord.Forbidden:
                await client.say("I dont have permissions ;(")
            except:
                await client.say("Role not existing please create one")
        elif member != None and time != "0":
            try:
                role = discord.utils.get(ctx.message.server.roles, name="Muted")
                await client.add_roles(member, role)
                emb1 = discord.Embed(description="Shut up {0.name} you have been muted\nduration:{1} min".format(member,time),colour=discord.Color.blue())
                emb1.set_author(name="KushBot")
                await client.say(embed=emb1)
                await asyncio.sleep(time * 60)
                await client.remove_roles(member, role)
                await client.say("You have been unmuted <@{0.id}>".format(member))
            except discord.Forbidden:
                await client.say("I lack perms ;(")
            except:
                await client.say("Role Not existing please create one")
        elif member != None and time < 0:
            await client.say("Provide a positive integer")
            return False
        else:
            await client.say("Invalid Arguments please try k!cmds")
            return False
    except:
        await client.say("Invalid Arguments try k!cmds")
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member = None):
    try:
        if member == None:
            await client.say("Who the fish should i mute?")
            return False
        m_role = discord.utils.get(ctx.message.server.roles, name="Muted")
        await client.remove_roles(member, m_role)
        await client.say("fine fine you can talk... {0.name}".format(member))
    except discord.Forbidden:
        await client.say("I lack perms bruhh")
    except:
        await client.say("Role not Existing")

        






        

client.run(os.getenv('TOKEN'))
