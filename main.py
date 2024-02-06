import discord
import random

# Botun ayrıcalıklarını tanımlayalım
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturalım ve ayrıcalıkları aktaralım
client = discord.Client(intents=intents)

# Plastik el işleri fikirleri içeren bir liste oluşturalım
catagories = ['bottle','paper','hurda']

bottle = ['pet_sise', 'demir_sise', 'sut_kutusu']
paper = ['kagit', 'karton', 'kutu']
hurda = ['araba', 'kamyon', 'ev_cihazlari']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    
    if message.content.startswith('pet_sise'):
        await message.channel.send(f"Pet siseler: Bir elma çöpü için 2 ay yeterliyken; plastik bir şişe için 450 yıl, bebek bezleri için 550 yıl, alüminyum kutular için 200-300 yıl geçmesi gerekir.")
        await message.channel.send("Karsidan saga don duz hemen solunda cop kutusu olacak ha oraya atacaksun")
        await message.channel.send("Pet sisenin deyeri su an $0.10")
    if message.content.startswith('kagit'):
        await message.channel.send("Sebzeler, 5 gün ile 1 ay arasında. Kâğıt, 2-5 ayda. Pamuklu giysiler, 6 ayda. Yün çoraplar, 1-5 yılda.")
        await message.channel.send("simdi surda Bakuden ucak gidecen Istanbula ordan sonra Besiktasa orda bir cop kutusu olcak ha oraya atcaksun")
        await message.channel.send("Su an kagitin deyeri $0.5")
       

# Botu çalıştıralım
client.run("MTE5Njg1NTM1NzQ4NjY3NDAxMg.GxhPX_.ZRDQsRfa3QKejbbq9Oy-9Zlth6Tml8FRr5aEVs")
