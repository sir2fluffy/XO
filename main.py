# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:35:16 2021

@author: charl
This is going to be the replit area
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:35:16 2021

@author: charl
This is going to be the replit area
"""

import discord, asyncio
from discord.ext import commands
import datetime
from keep_alive import keep_alive



cw_slots = [[11, True],[41, True],[48, False],[83, False],[89, False],[96, True],[131, True],[137, True],[144, True],[155, True],[179, True],[209, True]]

import time_table 

cw_table = time_table.table


for slot in cw_slots:
    mode_dict = {True:'Clan',False:'Levi'}
    mode = mode_dict[slot[1]]
    cw_table.add_event(4,0,slot[0],0,mode)







client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Ready'))
  print('We have logged in as {0.user}'.format(client))


        
@client.command()
async def hello(ctx):
  'hi'
  await ctx.send('Hello')


@client.command()
async def sayname(ctx):
    'Says the users name'
    await ctx.send(f"Your name is {ctx.author}")




@client.command()
async def cw(ctx):
    day = datetime.datetime.today().weekday()
    hour = datetime.datetime.hour()
    minute = datetime.datetime.minute()
    time_till,event_active, details = cw_table.next_event(day, hour, minute)    
    print(time_till,event_active, details)
    await ctx.send(message)


async def status():
  await client.wait_until_ready()
  

  while True:
    
    message, active, mode,time_till = (cw_time(status_ = True)) #mode = true if CW, time till is in mins

    if active == True:

      await client.change_presence(status=discord.Status.online, activity=discord.Game(message))

    else:

      await client.change_presence(status=discord.Status.idle, activity=discord.Game(message))


    await asyncio.sleep(2)






#keep_alive()
#client.loop.create_task(status())
#client.loop.create_task(alert())
client.run('ODA4MDI1ODI5MDkwMDAwOTEy.YCAisg.OF0k1-RUoVm4UxEtam_mNbODFWo')