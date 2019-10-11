import discord
import asyncio
import random
import pickle
import os

'''docstring'''

client = discord.Client()
raid = []
nightfall = []
strikes = []
crucible = []
trials = []
events = []
rCount = 0
nCount = 0
sCount = 0
cCount = 0
tCount = 0
eCount = 0
queue = [
    raid, nightfall, strikes, crucible, trials, events
    ]

queueCommands = (
    '?!r', '?!R', '?!raid',
    '?!nightfall', '?!nf', '?!NF',
    '?!s', '?!S', '?!strike', '?!strikes',
    '?!c', '?!crucible', '?!C', '?!pvp',
    '?!t', '?!T', '?!trials',
    '?!events', '?!e', '?!HE', '?!heroic', '?!h',
    )

validCommands = (
    '?!r', '?!R', '?!raid',
    '?!nightfall', '?!nf', '?!NF',
    '?!s', '?!S', '?!strike', '?!strikes',
    '?!c', '?!crucible', '?!C', '?!pvp',
    '?!t', '?!T', '?!trials',
    '?!events', '?!e', '?!HE', '?!heroic', '?!h',
    '?!l', '?!L', '?!leave',
    '!r'
    )

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global raid
    global nightfall
    global strikes
    global crucible
    global trials
    global events
    global rCount
    
    # blocks the bot from messaging itself
    if message.author == client.user:
        return
    # leave queue        
    if (message.author.mention in raid or message.author.mention in nightfall or
    message.author.mention in strikes or message.author.mention in crucible or
    message.author.mention in trials or message.author.mention in events):
        # queue error catch
        if message.content.startswith(queueCommands):
            await client.send_message(message.channel, 'You can only queue for one activity at a time!')
            return
            
        # leave raid queue
        elif message.author.mention in raid:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the raid queue.'.format(message.author)
                raid.remove(message.author.mention)
                rL = '{} player(s) are in the raid queue.'.format(len(raid))
                embed=discord.Embed(title=removed, description=rL, color=0xdd9b00)
                await client.send_message(message.channel, embed=embed)                

            elif message.content.startswith('!r'):
                rCount += 1
                if rCount == len(raid):
                    ready = ' '.join(raid)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your raid is ready! Please join the appropriate voice channel.')
                    raid = []
                    rCount = 0
                    
            elif message.content.startswith('!yes'):
                channel = client.get_channel('379353708649250816') #requires channel id
                await client.send_message(channel, 'TEST')
                
                #dm author to set date time and server
                
        # leave nightfall queue        
        elif message.author.mention in nightfall:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the nightfall queue.'.format(message.author)
                nightfall.remove(message.author.mention)
                nL = '{} player(s) are in the nightfall queue.'.format(len(nightfall))
                embed=discord.Embed(title=removed, description=nL, color=0x394dfd)
                await client.send_message(message.channel, embed=embed)
            elif message.content.startswith('!r'):
                global nCount
                nCount += 1
                if nCount == len(nightfall):
                    ready = ' '.join(nightfall)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your nightfall is ready! Please join the appropriate voice channel.')
                    nightfall = []
                    nCount = 0 

        # leave strikes queue        
        elif message.author.mention in strikes:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the strikes queue.'.format(message.author)
                strikes.remove(message.author.mention)
                sL = '{} player(s) are in the strikes queue.'.format(len(strikes))
                embed=discord.Embed(title=removed, description=sL, color=0x394dfd)
                await client.send_message(message.channel, embed=embed)
            elif message.content.startswith('!r'):
                global sCount
                sCount += 1
                if sCount == len(strikes):
                    ready = ' '.join(strikes)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your strike is ready! Please join the appropriate voice channel.')
                    strikes = []
                    sCount = 0 
        # leave crucible queue        
        elif message.author.mention in crucible:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the crucible queue.'.format(message.author)
                crucible.remove(message.author.mention)
                cL = '{} player(s) are in the crucible queue.'.format(len(crucible))
                embed=discord.Embed(title=removed, description=cL, color=0xff373d)
                await client.send_message(message.channel, embed=embed)
            elif message.content.startswith('!r'):
                global cCount
                cCount += 1
                if cCount == len(crucible):
                    ready = ' '.join(crucible)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your crucible is ready! Please join the appropriate voice channel.')
                    crucible = []
                    cCount = 0
                    
        # leave trials queue        
        elif message.author.mention in trials:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the trials queue.'.format(message.author)
                trials.remove(message.author.mention)
                tL = '{} player(s) are in the trials queue.'.format(len(trials))
                embed=discord.Embed(title=removed, description=tL, color=0xff373d)
                await client.send_message(message.channel, embed=embed)
            elif message.content.startswith('!r'):
                global tCount
                tCount += 1
                if tCount == len(trials):
                    ready = ' '.join(trials)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your trials queue is ready! Please join the appropriate voice channel.')
                    trials = []
                    tCount = 0 

        # leave heroic events queue        
        elif message.author.mention in events:
            if (message.content.startswith('?!l') or message.content.startswith('?!L') or
            message.content.startswith('?!leave')):
                removed = '{} has left the heroic events queue.'.format(message.author)
                events.remove(message.author.mention)
                eL = '{} player(s) are in the events queue.'.format(len(events))
                embed=discord.Embed(title=removed, description=eL, color=0xa000dd)
                await client.send_message(message.channel, embed=embed)
            elif message.content.startswith('!r'):
                global eCount
                eCount += 1
                if eCount == len(events):
                    ready = ' '.join(events)
                    await client.send_message(message.channel, ready)
                    await client.send_message(message.channel, 'Your heroic events queue is ready! Please join the appropriate voice channel.')
                    events = []
                    eCount = 0 
        return
    
    # join queue        
    if (message.author.mention not in raid or message.author.mention not in nightfall or
    message.author.mention not in strikes or message.author.mention not in crucible or
    message.author.mention not in trials or message.author.mention not in events):
        
        # leave error catch
        if (message.content.startswith('?!l') or message.content.startswith('?!L') or
        message.content.startswith('?!leave')):            
            await client.send_message(message.channel, 'You must be queued before you can leave!')
            
        # queue for raid
        elif (message.content.startswith('?!r') or message.content.startswith('?!R') or
        message.content.startswith('?!raid')):
            if rCount == 0:
                await client.send_message(message.channel, 'No raid is scheduled. Would you like to schedule one? (!yes)') #working in this part
                raid.append(message.author.mention)

##                added = '{} has joined the raid queue.'.format(message.author)
##                raid.append(message.author.mention)
##                rL = '{} player(s) are in the raid queue.'.format(len(raid))
                    
            if len(raid) == 2:
                ready = ' '.join(raid)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            #embed=discord.Embed(title=added, description=rL, color=0xdd9b00)
            #await client.send_message(message.channel, embed=embed)
        
        # queue for nightfall
        elif (message.content.startswith('?!nf') or message.content.startswith('?!NF') or
        message.content.startswith('?!nightfall')):
            added = '{} has joined the nightfall queue.'.format(message.author)
            nightfall.append(message.author.mention)
            nL = '{} player(s) are in nightfall queue.'.format(len(nightfall))
            if len(nightfall) == 2:
                ready = ' '.join(nightfall)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            embed=discord.Embed(title=added, description=nL, color=0x394dfd)
            await client.send_message(message.channel, embed=embed)
            
        # queue for strikes    
        elif (message.content.startswith('?!s') or message.content.startswith('?!S') or
        message.content.startswith('?!strikes') or message.content.startswith('?!strike')):
            added = '{} has joined the strikes queue.'.format(message.author)
            strikes.append(message.author.mention)
            sL = '{} player(s) are in the strikes queue.'.format(len(strikes))
            if len(strikes) == 1:
                ready = ' '.join(strikes)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            embed=discord.Embed(title=added, description=sL, color=0x394dfd)
            await client.send_message(message.channel, embed=embed)
            
        # queue for crucible
        elif (message.content.startswith('?!c') or message.content.startswith('?!C') or
        message.content.startswith('?!crucible') or message.content.startswith('?!pvp')):
            added = '{} has joined the crucible queue.'.format(message.author)
            crucible.append(message.author.mention)
            cL = '{} player(s) are in the crucible queue.'.format(len(crucible))
            if len(crucible) == 1:
                ready = ' '.join(crucible)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            embed=discord.Embed(title=added, description=cL, color=0xff373d)
            await client.send_message(message.channel, embed=embed)
        
        # queue for trials
        elif (message.content.startswith('?!t') or message.content.startswith('?!T') or
        message.content.startswith('?!trials')):
            added = '{} has joined the trials queue.'.format(message.author)
            trials.append(message.author.mention)
            tL = '{} player(s) are in the trials queue.'.format(len(trials))
            if len(trials) == 1:
                ready = ' '.join(trials)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            embed=discord.Embed(title=added, description=tL, color=0xff373d)
            await client.send_message(message.channel, embed=embed)
        
        # queue for heroic events
        elif (message.content.startswith('?!he') or message.content.startswith('?!e') or
        message.content.startswith('?!events') or message.content.startswith('?!heroic') or
        message.content.startswith('?!h')):
            added = '{} has joined the heroic events queue.'.format(message.author)
            events.append(message.author.mention)
            eL = '{} player(s) are in queue.'.format(len(events))
            if len(events) == 1:
                ready = ' '.join(events)
                await client.send_message(message.channel, ready)
                await client.send_message(message.channel, 'Type !r if you are ready.')
            embed=discord.Embed(title=added, description=eL, color=0xa000dd)
            await client.send_message(message.channel, embed=embed)

client.run(TOKEN)
