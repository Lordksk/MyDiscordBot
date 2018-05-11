import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random
Client = discord.Client()
client = commands.Bot(command_prefix = "k!")


BotLink = "https://discordapp.com/api/oauth2/authorize?client_id=437242135322951680&permissions=8&scope=bot"
UserIDS = ["362882906923859968","300868677429886976","407186187443372043"]
restricted_words = ["FUCK","WTF","SEX"]
@client.event
async def on_ready():
    print("KushBot is now Active!")

@client.event
async def on_message(message):
    if message.content.upper().startswith("K!TOSS"):
        k = random.randint(0,1)
        if k == 1:
            await client.send_message(message.channel, "Heads!")
        else:
            await client.send_message(message.channel, "Tails!")
    if message.content.upper().startswith("K!HELP"):
        emb = (discord.Embed(description="1]Toss\n2]rps rock|paper|scissors\n3]want the invite link? just do k!invite-link\n4]clr", colour=0x3DF270))
        emb.set_author(name="KushBot")
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith("K!CLR"):
        if message.author.id not in UserIDS:
            await client.send_message(message.channel, "You dont have the rights to use this command!")
        elif "421308675622305812" in [role.id for role in message.author.roles] or "366590120457142272" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            k = int(args[1])
            if k >= 100:
                await client.send_message(message.channel, "The Limit is only 99!")
            elif k <= 0:
                await client.send_message(message.channel, "Bruhh! Dont act foolish")
            elif k > 0 and k < 100:
                await client.purge_from(message.channel, limit=k)

            
    if message.content.upper().startswith("K!INVITE-LINK"):
        await client.send_message(message.channel, "My invite link is %s" % (BotLink))

    k = message.content.upper().split(" ")
    for j in k:
        if j in restricted_words:
            await client.delete_message(message)
            await client.send_message(message.channel, "<@%s> Such words are not allowed!" % (message.author.id))
            break
    if message.content.upper().startswith("K!RPS"):
        args = message.content.upper().split(" ")
        k = random.randint(1,3)
        if len(args) == 1:
            await client.send_message(message.channel, "No arguments provided")
        else:
            if args[1].upper() == "SCISSOR":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> awww you lost :cry:" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> You win cool! :cool:" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> Tie! :P:" % (message.author.id))
            elif args[1].upper() == "ROCK":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> Tie!" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> aww you lost :cry:" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> you win cool! :cool:" % (message.author.id))
            elif args[1].upper() == "PAPER":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> You win cool! :cool:" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> Tie!" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> awww you lost :cry:" % (message.author.id))
            else:
                await client.send_message(message.channel, "<@%s> Invalid argument try k!help" % (message.author.id))
    if message.content.upper().startswith("K!PERVERT"):
        if "436467140581654529" not in [role.id for role in message.author.roles]:
            role1 = discord.utils.get(message.server.roles, id="436467140581654529")
            mem = message.author
            await client.add_roles(mem,role1)
            await client.send_message(message.channel, "<@%s> role set :wink:" % (message.author.id))
        else:
            role1 = discord.utils.get(message.server.roles, id="436467140581654529")
            mem = message.author
            await client.remove_roles(mem,role1)
            await client.send_message(message.channel, "<@%s> Role removed!!!!!" % (message.author.id))
    if message.content.upper().startswith("K!SENPAI"):
        if "442267667064422400" not in [role.id for role in message.author.roles]:
            role2 = discord.utils.get(message.server.roles, id="442267667064422400")
            mem = message.author
            await client.add_roles(mem,role2)
            await client.send_message(message.channel, "<@%s> role set :wink:" % (message.author.id))
        else:
            role2 = discord.utils.get(message.server.roles, id="442267667064422400")
            mem = message.author
            await client.remove_roles(mem, role2)
            await client.send_message(message.channel, "<@%s> Role removed!!!" % (message.author.id))
    if message.content.upper().startswith("K!ROLES"):
        emb3 = (discord.Embed(description="1]Pervert\n2]Senpai\n3]Dark", colour=0x3DF170))
        emb3.set_author(name="KushBot")
        await client.send_message(message.channel, embed=emb3)
    if message.content.upper().startswith("K!DARK"):
        if "442273547214258177" not in [role.id for role in message.author.roles]:
            dark_role = discord.utils.get(message.server.roles, id="442273547214258177")
            mem = message.author
            await client.add_roles(mem, dark_role)
            await client.send_message(message.channel, "<@%s> role set :wink:" % (message.author.id))
        else:
            dark_role = discord.utils.get(message.server.roles, id="442273547214258177")
            mem = message.author
            await client.remove_roles(mem, dark_role)
            await client.send_message(message.channel, "<@%s> Role removed!!!" % (message.author.id))
    if message.content.upper().startswith("K!KICK"):
        args = message.content.split(" ")
        await client.kick(id=args[1])
        
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




client.run(os.getenv('TOKEN'))
