#bunlar modüller için modül için pip kullanılır
import discord
from discord.ext import commands
#bu modülleri ilk başta kullanmasınızda olur
import asyncio
from itertools import cycle
import random
import typing
import os

 
#buradan prefixinizi ayarlayabilirsiniz
master = commands.Bot(command_prefix = "!")

#bu kısım bot açılınca mesaj gönderiyor
@master.event
async def on_ready():
        print('Bot Hizmet Veriyor')

async def on_message(self, message):

  #bu kısım diğer botlara cevap vermemesi için aksi takdirde sıkıntı olabilir
        if message.author.id == self.user.id:
            return

#bu kısım help komutunu kaldırmak için help komutu kendiliğinden geliyor ve kötü görünüyor ama eğer burayı silerseniz help komutunu kullanabilirsiniz
master.remove_command('help')

#bu bir komut örneği internetden daha fazla function ve komut bulabilirsiniz
@master.command()
async def deneme(ctx):
 await ctx.send('Deneme Başarılı')


#botunuzun tokenini discord developer portal dan alınız
master.run('TOKEN')
