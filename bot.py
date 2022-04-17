import requests
import json
import time
import discord
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

#token list
  if message.content == "?tokens":
              embed = discord.Embed(title="Token commands available on Paladin bot", description="")
              embed.add_field(name="Token list", value = "?vis - Vigorus price \n ?slp - Smooth Love Potion price \n ?btc - Bitcoin price \n ?ada - Cardano price")
              await message.channel.send(content= None, embed=embed)
          
#-----------------------------------------------Coins---------------------------------------------------------------
#btc price  
  if message.content == "?btc":
            while 0 == 0:
              api_requests = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
              api1 = json.loads(api_requests.content)
              cprice = api1['bitcoin']['usd']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579")
              embed.add_field(name="Bitcoin ", value = "$" + str(cprice))
              await message.channel.send(content= None, embed=embed)
              break

#ada price
  if message.content == "?ada":
            while 0 == 0:
              api_requests = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd")
              api1 = json.loads(api_requests.content)
              cprice = api1['cardano']['usd']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://assets.coingecko.com/coins/images/975/small/cardano.png?1547034860")
              embed.add_field(name="Cardano ", value = "$" + str(cprice))
              await message.channel.send(content= None, embed=embed)
              break

#vis price
  if message.content == "?vis":
            while 0 == 0:
              api_requests = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vigorus&vs_currencies=usd")
              api1 = json.loads(api_requests.content)
              cprice = api1['vigorus']['usd']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://assets.coingecko.com/coins/images/21245/small/VIS.PNG?1638768736")
              embed.add_field(name="Vigorus ", value = "$" + str(cprice))
              await message.channel.send(content= None, embed=embed)
              break
#slp price
  if message.content == "?slp":
            while 0 == 0:
              api_requests = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=smooth-love-potion&vs_currencies=usd")
              api1 = json.loads(api_requests.content)
              cprice = api1['smooth-love-potion']['usd']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://assets.coingecko.com/coins/images/10366/small/SLP.png?1578640057")
              embed.add_field(name="Smooth love potion ", value = "$" + str(cprice))
              await message.channel.send(content= None, embed=embed)
              break

#--------------------------------------------------------------------------------------------------------------
              

 #-----------------------------------------------------NFTs-----------------------------------------------------             
  #RB nft floor
  if message.content == "?rb floor":
            while 0 == 0:
              api_requests = requests.get("https://api.opensea.io/api/v1/collection/rebelbots/stats")
              api = json.loads(api_requests.content)
              floor = api['stats']['floor_price']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://media.giphy.com/media/d6Ej8cphDMpeUxJeYY/giphy.gif")
              embed.add_field(name="Rebel Bots", value = "Current floor price is " + str(floor) + " ETH")
              await message.channel.send(content= None, embed=embed)
              break

#Chibverse nft floor
  if message.content == "?chibv1 floor":
            while 0 == 0:
              api_requests = requests.get("https://api.opensea.io/api/v1/collection/chibverse/stats")
              api = json.loads(api_requests.content)
              floor = api['stats']['floor_price']
              embed = discord.Embed(title="", description="")
              embed.set_image(url="https://media.giphy.com/media/qRMWBjHl2lAIhhAmCX/giphy.gif")
              embed.add_field(name="Chibverse", value = "Current floor price is " + str(floor) + " ETH")
              await message.channel.send(content= None, embed=embed)
              break

#--------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------Time---------------------------------------------------              
#neal time
  if message.content == "?neal time":
            while 0 == 0:
              api_requests = requests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=US/Central")
              api2 = json.loads(api_requests.content)
              neal_time = api2['time']
              embed = discord.Embed(title="Neal's time", description="")
              embed.set_image(url="https://cdn.pixabay.com/photo/2017/06/26/00/46/flat-2442462__340.png")
              embed.add_field(name="US/Central", value = str(neal_time))
              await message.channel.send(content= None, embed=embed)
              break


#-------------------------------------------------------------------------------------------------------------- 

#-----------------------------------------------------Misc----------------------------------------------------- 
#joke api  
  if message.content.startswith('?joke'):
    while 0 == 0:
      api_requests = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist&type=single")
      api2 = json.loads(api_requests.content)
      joke = api2['joke']
      await message.channel.send(joke)
      break


  if message.content.startswith('?greet'):
      channel = message.channel
      await channel.send('Say hello!')

      def check(m):
          return m.content == 'hello' and m.channel == channel

      msg = await client.wait_for('message', check=check)
      await channel.send(f'Hello {msg.author}!')



              #----------------------might need this shit later-------------------------------#
#while 0 == 0:
  #api_requests = requests.get("https://api.opensea.io/api/v1/collection/rebelbots/stats")
  #api = json.loads(api_requests.content)
 #price = api['stats']['floor_price']
  #print ("the floor price of Rebel Bots is currently " + str(price) + " ETH")
  #time.sleep(60)

#def btcprice():
  #while 0 == 0:
    #api_requests = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=true&include_last_updated_at=false")
    #api1 = json.loads(api_requests.content)
    #cprice = api1['bitcoin']['usd']
    #print("The price of Bitcoin is currently " + "$" + str(cprice))
    #time.sleep(5)
    #break
              #----------------------------------------------------------------------------------#



client.run('OTY0OTY2NzA3MzA5NDY1NjIw.YlsVRw.9Ql_iNx3L5Ab7rFlZHUiGsb9Tac')
