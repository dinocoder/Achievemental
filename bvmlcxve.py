#get_message
#edit_role
#discord.utils.find
#class discord.User
#get_member_named(name)
#[:-1]
#discord.Client.add_roles(discord.Client.get_user_info(None, ("%s" % (args[1]))), '<@&423269531805548545>')
#getUsername = re.compile('/([!])+/g')
#and message.author == discord.User.bot
#client.wait_for

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
TERMS = ['collected', 'golden', 'duck']
swearWords = ['fuck']
canRun = True

Client = discord.Client()
client = commands.Bot(command_prefix = '-a ')
wallet_grabbable = False
purchased = False

'''
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
'''

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('-a Trolololol'):
        await client.send_message(message.channel, 'Your first clue is \"\'''CjMwIDMxIDMwIDMwIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMxIDMxIDMxIDMxIDIwIDMwIDMwIDMxIDMwIDMwIDMwIDMwIDMwIDIwIDMwIDMwIDMwIDMwIDMxIDMwIDMxIDMwIDIwIDMwIDMwIDMxIDMwIDMxIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMwIDMxIDIwIDMwIDMwIDMxIDMwIDMwIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMxIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMwIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMwIDMxIDMxIDMwIDMxIDMwIDMwIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMxIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMxIDMxIDIwIDMwIDMxIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMxIDMxIDMxIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMxIDMxIDMxIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMxIDMxIDIwIDMwIDMxIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMwIDMxIDMxIDMwIDMwIDMxIDMxIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMxIDMxIDMwIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMxIDIwIDMwIDMwIDMxIDMxIDMxIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMwIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMxIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMxIDMxIDMxIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMwIDMwIDMwIDMwIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMxIDMwIDMwIDMxIDMwIDIwIDMwIDMxIDMxIDMxIDMwIDMxIDMxIDMxIDIwIDMwIDMxIDMxIDMwIDMxIDMxIDMxIDMxIDIwIDMwIDMxIDMxIDMwIDMwIDMxIDMwIDMxIDIwIDMwIDMxIDMxIDMwIDMxIDMwIDMwIDMxCg==\'''\"')


    if message.content.startswith('-a kve9r8ty489wefdcxjbfruiosdfhiodcx39etuerfd~8yu8eury~~~```urwoei'):
        await client.send_message(message.channel, '''The final challenge: zoigap69q7vsxz6prs2xdpmxxu2xqbbuxjryw3c4l4p4hc7qw9vrghnvume4yp2mttoj38t5xl1quizzdhjis87z0gqpimy9qcxbq81tovnfr1nh06skrh8hfttebeixybqb5myw9p0u8d8izt8djvoo0f985y6mhfakare5ap436wust8l5w4k61l30uy0lv9gwjpi2qcjdqsjzndedimmwmtr05zvto7es235qsovlrzw96x3ozu69oxbb4tqbgyos3q7xx132dewgx5ro3k6dvhz3tq19a9ydg0hagr3qcwiyke4hrkt1r2mvzuw0np3aw8i0q2ogkeytiz5qca50fer0fyfxj0zpemmdoza4vrbyi8hbr5kr9rh8qtwyjipla5qhyzj1xye5e33vc0f67nzp569cvuk7a4sfppy9jy420htfgi9whu6ek6dgw9vtx9d3hp37zklineuq3mcs51gofh460jfl0vnsjy7usl2dihbu3ccxrisvube5osv2ydlvd3wfc17nz6d61fjwwdt8fjauo77xhtv07x3cxt9afd8qcfhef9gkg5qglhl4f28yer5pr4tn1m8lnuvhxog43naor37e8v2uyjmlr3xvb0aqmu0l3ybwcvvciqskppwtpd0qz61a2o5dhk1wkxcuf767z0tr036t1omx0pzari6ugp32tfct8f1swqhq0ic7xqd1fjo3vgyyxy7zfti5wu7tw451b2jn81c953252bo20a546wqrr5cqm3c43nv6ci6cfm2tfmb4kvahuojip074bcxsyy2a29mzckaip836e5l2qhpwqzxrgzhit9pk7r6lcznl2x0h3m5uhjsfriuqdjs5gub23e0f2rkv7tdqlvaarrlh16898vfc4juo1ytu6ctyp7f5b0n4t52scuo0n6ttdq4ywagb551cfpdpvphqzk011t14ibh9ys688gj5d741r0nwt8jfki7qnzr3dwgc7qkripzkmtk58e6ewvemsbp8c4nys5cwgdyug4sevlhnjs3f77oe68rip34buhxf6w8bhjmfoyjzbwx4mheripnliarb2pcwx443et71tod2kyq3sinqihda6uj5ctbg8yjfrpe8mgsuia36ma52t15bd4t5xpu5ddoxje1ia4z3zo5bpg7y7irknnv6qh576ger58u2vox3s26llkm8c97vdkq46ga8m0g3rbjt3gpyhbve3chjaicem8h626efbw3oc0bnp94xox0mrogskhc5w7xl2h5v88a0xbpiwpruybybvh2out0e8u0n68jw51fbo57hf4fzy3xo0mvq0xmlnupxee8qwnk19fnd0ocl24rgeezlfizue2wdhcgusibeinmvt2ws03irr1hun85ydy1d2fqffmenyjcmfpsi6xcfczuuvac33afa7vclg2se5qwgbguyq045883fvl2wbqikba9hpemubc6qq8eosnchf6wn7hvsxtf891dph317s0x97zz30kdaoln2fv3911akgwaucrxtcvkks881yuw0irw7ox6okhtx9teoukee856t3z7s5kd568rjx6vez119it43m9y669ehzo304i77itdqakfm24kiab1skshzoeix3s93ekb0r1dl1ryk6tqxl51zdr01oxgm2twkzljniyzjlknm6ugk0592uiqj34du03y287wsrjo79gph093vp6fnqrbxd5lgq1hwu8ok5r09ec8vxqvrzbs2fneoh8l7ms2yw9lgf5sygkcsfv17g2fldgy7f34r72y7tmluh3l0nqrdu6vb1nr4d7jb79614y48hqczythwlmt2283t2l3g5xsjk46nfjqujydj3s5b1v10xha0kormcmedrzvtj70rateh6zmpjxt8qgkii9998lbeqgycmbhp64zbwilmcb648cxn3r11qg07nvy6tqrtnm2y4j3b1f0n145gi00ockbm9ww6gzglwz2we5iaobgamhyt68kev1vw6fo9kvv3gs4m840ys2gwv64xo9vtjpqgl4g7ekjfn23ci9c8atr9dduxwomyvi06ee9x0oo8sr4n3o5mha9v21yopplufth3dt5io62sldc2wfyiyts94qz8jpvfk2lj63nv0uuhxg23kjjq1i1a9h2b60vifoj8levfqagm12cntomi7l8pu6i0kd5kn8v6y5fr6pmvayd8jljqsfm1o34pdzkamjicdd9falrkgxa15b2lqg8oj9fzap9f5qdhw1rruox5psq1tkeroyi5s3sb96fjpbbt5c53i0txcvgwfatu1cbrien80ih6w4in56ktgkmgpvosz9nu87xrplo2xehhxbemlgl4lg1ob4d6mmf7v1qeqidrfuue6mx0bb535xdac0pg9t94d6j8t43h7yk9v9eh5g3jtjsvnkfsh134nmma780e0nfd3i2iu7yz48twph7i1g45ahhu6ctuypm5agjc7qsoppl030irvsie48mtxsazlgnnb9470iffdhustyzlfpz7zf654j5fnmun0ptb3smo3gvh4xzcvmdo657rx7no54xibnfvriqh21jtlp6qjnvj7cdx53y8zfzh4cuz6iy6yccrrxw1gsly74rcirrhku1z7xkgcd1slk64hv27mmr9sedz9eeeoylzi60acaemc1anwn7xfn3ugt46zs9kaoy0pg72kqsfbxgb0ka38x2673m48kopkd3l0mjyvc9njpk9l98cgd582oponde8fkpo1yel0t9hcb245ggo35v21ji1cpemqfyyazrgl6n9zefyor8rb571phyx9labu3xco5d1ryz7oy0whvhyg7puy137ftck81rneatzk7recj28cqcntes7rokoisz9hrn7ds3yldd4fhv8mtpkeiamjfg67zjkqr8nzwjtvng1vi83a1bj7gr6b02ypor2u2ix7l13ofisnbt53s1o17onrk8t9txchpczr1t4ybnmtyjx0ts5eywzpjm6xsrkwq3izcftf6v72xr2tuvardba56ee7t7aat0pbamam6o3ar13fknkncn8d0ztgeryf3qc7yp7vcjzsgy5pl7cf4omcpgi821f3z1ax3hjujfyl6q1zswpygaj4l1lo1cp6paby5hjt1mms81tf192uh56qp9sbzriwnzp71nfkt1xtgaikqo3pfc8rhrumjaux28rxupdlys4qksfl37gd
                                  is your code. Wall:2 Shelf:3 Volume:10. Good luck.''')
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

    #Prestige 1
    if message.content.startswith('-a prestige'):
        role_names = [role.name for role in message.author.roles]
        if 'Prestige #1' in role_names:
            pass
        elif 'Prestige #2' in role_names:
            pass
        elif 'Prestige #3' in role_names:
            pass
        elif 'Prestige #4' in role_names:
            pass
        else:
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
        print('dfghv')
        if message.content.startswith('You got ') and message.author == message.guild.get_member('365975655608745985'):
            role_names = [role.name for role in member.roles]
            roleChange = discord.utils.get(message.guild.roles, name = 'Voting!? (achievement)')
            if not 'Voting!? (achievement)' in role_names:
                await member.add_roles(roleChange)
                await message.channel.send('Congratulations, ' + str(member) + '! You\'ve earned the "Voting!?" achievement!')

    #Sneaky Operations
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
            
client.run('NDI4MDczMDczMzI1ODk5Nzc2.DZ3svg.ejaQHsvLIBZXOpxM3xsJj9N3Z-k')
