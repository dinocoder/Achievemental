import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time
import re

global wallet_grabbable
global TERMS
global purchased
global swearWords
global canRun
#For the Holy Golden Duck achievement
TERMS = ['collected', 'golden', 'duck']
#For "Sneaky Operations"
swearWords = ['insert', 'swear', 'words', 'here']
canRun = True

Client = discord.Client()
client = commands.Bot(command_prefix = '-a ')
wallet_grabbable = False
purchased = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    canRun = True
    #Starting your Adventure
    if message.content.startswith('Congratulations') and message.author == message.guild.get_member('365975655608745985'):
        currentRoles = []
        args = message.content.split()
        username = ("%s" % (args[1]))
        userID = re.sub(r'[^\w]', '', username)
        userData = await client.get_user_info(userID)
        roleChange = discord.utils.get(message.guild.roles, name = 'Starting Your Adventure (achievement)')
        member = discord.utils.get(message.guild.members, name = userData.name, id = userData.id)
        print(type(userData.name))
        role_names = [role.name for role in member.roles]
        if not "Starting Your Adventure (achievement)" in role_names:
            await member.add_roles(roleChange)
            await message.channel.send('Congratulations, ' + username + ' You\'ve earned the "Starting your Adventure" achievement!"!')

    #Bad boy(or girl)
    if message.content.startswith('Someone just dropped their wallet in this channel!') and message.author == message.guild.get_member('346353957029019648'):
        global wallet_grabbable
        wallet_grabbable = True
        
    if message.content.startswith('~grab') and wallet_grabbable == True:
        roleChange = discord.utils.get(message.guild.roles, name = 'Bad Boy(or girl) (achievement)')
        role_names = [role.name for role in message.author.roles]
        if not 'Bad Boy(or girl) (achievement)' in role_names:
            await message.author.add_roles(roleChange)
            await message.channel.send('Congratulations, ' + str(message.author) + '! You\'ve earned the "Bad Boy(or girl)" achievement!')
        wallet_grabbable = False

    #The Holy, Golden Duck
    if message.author == message.guild.get_member('332938855835500547'):
        TERMS = ['collected', 'golden', 'duck']
        Aw_Yiss_message = str(message.content.split())
        accepted_message = True
        for i in range(0, 3):
            if not TERMS[i] in Aw_Yiss_message:
                accepted_message = False
                break
        if accepted_message == True:
            username = (re.findall('\w+', message.content))[0]
            member = discord.utils.get(message.guild.members, name = username)
            roleChange = discord.utils.get(message.guild.roles, name = 'The Holy, Golden Duck (achievement)')
            role_names = [role.name for role in member.roles]
            if not 'The Holy, Golden Duck (achievement)' in role_names:
                await message.author.add_roles(roleChange)
                await message.channel.send('Congratulations, ' + str(message.author) + '! You\'ve earned "The Holy, Golden Duck" achievement!')

    #Hypebeast I
    if message.content.startswith('-a addedby'):
        file = open('addedby.txt', 'r')
        if not str(message.author) in file.readlines():
            seperator = re.compile("([ ])")
            username = re.split(seperator, message.content)
            member = discord.utils.get(message.guild.members, name = username[4])
            if member == message.author:
                file.close()
                return
            if member == None:
                member = message.mentions[0]
            if member == message.author:
                file.close()
                return
            await message.channel.send('Thanks, ' + str(member) + ' for adding ' + str(message.author) + ' to the server!')
            role_names = [role.name for role in member.roles]
            roleChange = discord.utils.get(message.guild.roles, name = 'Hypebeast I (achievement)')
            if not 'Hypebeast I (achievement)' in role_names:
                await member.add_roles(roleChange)
                await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Hypebeast I" achievement!')
            file.close()
            file = open('addedby.txt', 'a')
            file.write(str(message.author))
        file.close()

    #Helper I
    if message.content.startswith('-a helpedby'):
        seperator = re.compile('([ ])')
        username = re.split(seperator, message.content)
        member = discord.utils.get(message.guild.members, name = username[4])
        if member == message.author:
            return
        if member == None:
                member = message.mentions[0]
        if member == message.author:
            return
        await message.channel.send('Thanks, ' + str(member) + ' for helping ' + str(message.author) + '!')
        role_names = [role.name for role in member.roles]
        roleChange = discord.utils.get(message.guild.roles, name = 'Helper I (achievement)')
        if not 'Helper I (achievement)' in role_names:
            await member.add_roles(roleChange)
            await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Helper I" achievement!')

    #Memes I
    try:
        test = message.attachments[0]
    except IndexError:
        canRun = False
    if canRun == True:
        if message.attachments[0] and message.channel == discord.utils.get(message.guild.channels, name = 'general'):
            role_names = [role.name for role in message.author.roles]
            roleChange = discord.utils.get(message.guild.roles, name = 'Memes I (achievement)')
        if not 'Memes I (achievement)' in role_names:
            await message.author.add_roles(roleChange)
            await message.channel.send('Congratulations, ' + str(message.author) + '! You\'ve earned the "Memes I" achievement!')
    else:
        canRun = True
        
    #Bad Luck I
    try:
        test = message.embeds[0].description
    except IndexError:
        canRun = False
    if canRun == True:
        embedTitle = message.embeds[0].title
        if not str(embedTitle) == 'Embed.Empty':
            if 'Coinflip' in message.embeds[0].title:
                if 'thanks for the free' in message.embeds[0].description:
                    coinflipInfo = message.embeds[0].title.split()
                    amount = re.sub("[^\w]", '', coinflipInfo[4])
                    if int(amount) >= 1000:
                        rawUserInfo = coinflipInfo[2]
                        userInfo = rawUserInfo.split('#')
                        member = discord.utils.get(message.guild.members, name = userInfo[0], discriminator = userInfo[1])
                        role_names = [role.name for role in member.roles]
                        roleChange = discord.utils.get(message.guild.roles, name = 'Bad Luck I (achievement)')
                        if not 'Bad Luck I (achievement)' in role_names:
                            await member.add_roles(roleChange)
                            await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Bad Luck I" achievement!')
    else:
        canRun = True
    
    #Rich Kid I
    try:
        test = message.embeds[0].description
    except IndexError:
        canRun = False
    if canRun == True:
        if 'balance contains' in message.embeds[0].description:
            balInfo = message.embeds[0].description.split()
            money = re.sub("[^\w]", '', balInfo[4])
            if int(money) >= 1000:
                userInfo = balInfo[0].split('#')
                member = discord.utils.get(message.guild.members, name = userInfo[0])
                role_names = [role.name for role in member.roles]
                roleChange = discord.utils.get(message.guild.roles, name = 'Rich Kid I (achievement)')
                if not 'Rich Kid I (achievement)' in role_names:
                    await member.add_roles(roleChange)
                    await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Rich Kid I" achievement!')
    else:
        canRun = True

    #Prestige Command
    if message.content.startswith('-a prestige'):
        role_names = [role.name for role in message.author.roles]
        if 'Prestige #1' in role_names:
            #Triggers Prestige 2 (W.I.P)
            pass
        elif 'Prestige #2' in role_names:
            #Triggers Prestige 3 (W.I.P)
            pass
        elif 'Prestige #3' in role_names:
            #Triggers Prestige 4 (W.I.P)
            pass
        elif 'Prestige #4' in role_names:
            #Triggers Prestige 5 (W.I.P)
            pass
        else:
            #Triggers Prestige 1
            member = message.author
            role_names = [role.name for role in member.roles]
            if 'Rich Kid I (achievement)' in role_names and 'Bad Luck I (achievement)' in role_names and 'Helper I (achievement)' in role_names and 'Hypebeast I (achievement)' in role_names and 'The Holy, Golden Duck (achievement)' in role_names and 'Bad Boy(or girl) (achievement)' in role_names and 'Starting Your Adventure (achievement)' in role_names and 'Impersonator (achievement)' in role_names and 'Memes I (achievement)' in role_names:
                removeRichKidI = discord.utils.get(message.guild.roles, name = 'Rich Kid I (achievement)')
                removeBadLuckI = discord.utils.get(message.guild.roles, name = 'Bad Luck I (achievement)')
                removeHelperI = discord.utils.get(message.guild.roles, name = 'Helper I (achievement)')
                removeHypebeastI = discord.utils.get(message.guild.roles, name = 'Hypebeast I (achievement)')
                removeGoldenDuck = discord.utils.get(message.guild.roles, name = 'The Holy, Golden Duck (achievement)')
                removeBadBoy = discord.utils.get(message.guild.roles, name = 'Bad Boy(or girl) (achievement)')
                removeStartingAdventure = discord.utils.get(message.guild.roles, name = 'Starting Your Adventure (achievement)')
                removeImpersonator = discord.utils.get(message.guild.roles, name = 'Impersonator (achievement)')
                removeMemesI = discord.utils.get(message.guild.roles, name = 'Memes I (achievement)')
                await member.remove_roles(removeRichKidI, removeBadLuckI, removeHelperI, removeHypebeastI, removeGoldenDuck, removeBadBoy, removeStartingAdventure, removeImpersonator, removeMemesI, reason = '{0} is reaching Prestige 1!'.format(member))
                roleChange = discord.utils.get(message.guild.roles, name = 'Prestige # 1')
                generalChannel = discord.utils.get(message.guild.channels, name = 'general')
                await member.add_roles(roleChange)
                await generalChannel.send('Congratulations, ' + str(message.author) + '! You have reached Prestige 1!')
    

    
#PRESTIGE 2

    #Bad Luck II
    try:
        test = message.embeds[0].description
    except IndexError:
        canRun = False
    if canRun == True:
        embedTitle = message.embeds[0].title
        if not str(embedTitle) == 'Embed.Empty':
            if 'Coinflip' in message.embeds[0].title:
                if 'thanks for the free' in message.embeds[0].description:
                    coinflipInfo = message.embeds[0].title.split()
                    amount = re.sub("[^\w]", '', coinflipInfo[4])
                    if int(amount) >= 10000:
                        rawUserInfo = coinflipInfo[2]
                        userInfo = rawUserInfo.split('#')
                        member = discord.utils.get(message.guild.members, name = userInfo[0], discriminator = userInfo[1])
                        role_names = [role.name for role in member.roles]
                        roleChange = discord.utils.get(message.guild.roles, name = 'Bad Luck II (achievement)')
                        if not 'Bad Luck II (achievement)' in role_names:
                            await member.add_roles(roleChange)
                            await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Bad Luck II" achievement!')
    else:
        canRun = True
        
    #Rich Kid II
    try:
        test = message.embeds[0].description
    except IndexError:
        canRun = False
    if canRun == True:
        if 'balance contains' in message.embeds[0].description:
            balInfo = message.embeds[0].description.split()
            money = re.sub("[^\w]", '', balInfo[4])
            if int(money) >= 10000:
                userInfo = balInfo[0].split('#')
                member = discord.utils.get(message.guild.members, name = userInfo[0])
                role_names = [role.name for role in member.roles]
                roleChange = discord.utils.get(message.guild.roles, name = 'Rich Kid II (achievement)')
                if not 'Rich Kid II (achievement)' in role_names:
                    await member.add_roles(roleChange)
                    await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Rich Kid II" achievement!')
    else:
        canRun = True

    #What a Loser
    try:
        test = message.embeds[0].description
    except IndexError:
        canRun = False
    if canRun == True:
        embedTitle = message.embeds[0].title
        if not str(embedTitle) == 'Embed.Empty':
            if 'has fainted!' in message.embeds[0].title:
                if 'wins' in message.embeds[0].description:
                    battleInfo = message.embeds[0].title.split()
                    username = re.sub("[^\w]", '', battleInfo[0])
                    member = discord.utils.get(message.guild.members, name = username)
                    role_names = [role.name for role in member.roles]
                    roleChange = discord.utils.get(message.guild.roles, name = 'What a Loser (achievement)')
                    if not 'What a Loser (achievement)' in role_names:
                        await member.add_roles(roleChange)
                        await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "What a Loser" achievement!')
    else:
        canRun = True

    #The Grind Is On!
    if message.content.startswith('p!buy 1') or message.content.startswith('p!buy 2') or message.content.startswith('p!buy 3') or message.content.startswith('p!buy 4'):
        purchased = True
        member = message.author
        if message.content.startswith('Successfully purchased') and message.author == message.guild.get_member('365975655608745985'):
            role_names = [role.name for role in member.roles]
            roleChange = discord.utils.get(message.guild.roles, name = 'The Grind Is On! (achievement)')
            if not 'The Grind Is On! (achievement)' in role_names:
                await member.add_roles(roleChange)
                await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned "The Grind Is On!" achievement!')
        purchased = False

    #Voting!?
    if message.content.startswith('p!daily claim'):
        member = message.author
        if message.content.startswith('You got ') and message.author == message.guild.get_member('365975655608745985'):
            role_names = [role.name for role in member.roles]
            roleChange = discord.utils.get(message.guild.roles, name = 'Voting!? (achievement)')
            if not 'Voting!? (achievement)' in role_names:
                await member.add_roles(roleChange)
                await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Voting!?" achievement!')

    #Sneaky Operations(W.I.P)
    if message.channel == discord.utils.get(message.guild.channels, name = 'christian-minecraft-server'):
        containsSwearing = False
        for i in swearWords:
            if i in message.content:
                containsSwearing = True
        if containsSwearing == True:
            await message.author.send('You have sworn in #christian-minecraft-server! To get the achievement "Sneaky Operations", the message must go unnoticed for 24 hours! Beware of people trying to complete "Bad Cop"! Deleting the message will disqualify you from the achievement.')
            time.sleep(43200)
            await message.author.send('12 hours left!')
            time.sleep(43200)
        



@client.event
async def on_member_update(before, after):
    adminList = []
    adminNicks = []
    for i in after.guild.members:
        checkRole = [role.name for role in i.roles]
        if "Master" in checkRole or "Master's Second In Command" in checkRole or "Master's Third In Command" in checkRole or "Master's Architect" in checkRole:
            adminList.append(i)
    for i in adminList:
        adminNicks.append(i.nick)
        adminNicks.append(i.name)
    while None in adminNicks:
        adminNicks.remove(None)
    if after.nick in adminNicks:
        role_names = [role.name for role in after.roles]
        roleChange = discord.utils.get(after.guild.roles, name = 'Impersonator (achievement)')
        if not 'Impersonator (achievement)' in role_names:
            await after.add_roles(roleChange)
            await discord.utils.get(after.guild.channels, name = 'general').send('Congratulations, ' + str(after) + '! You\'ve earned the "Impersonator" achievement!')
            
client.run('Bot Token')
