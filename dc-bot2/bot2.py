import discord
from discord.ext import commands
import yenidosya
import yolov2


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def ypy(ctx):
    if ctx.message.attachments:
        for resim in ctx.message.attachments:
            await resim.save(f"./yeni_img/{resim.filename}")
            await ctx.send(f"Mesajiniz gonderildi")
            ege =yolov2.top(yolov2.gor)
            await ctx.send(ege)

    else:
        await ctx.send(f"Resmin yaninda bir ek gonderilmedi")




if class_name[2:-1] == "Thumbs Up":
    print("Başparmak yukarıda!:Uluslararasi bir onaylama isaretidir")
elif class_name[2:-1] == "Peace Sign":
    print("Barış işareti!Uluslararasi bir baris isaretidir")
elif class_name[2:-1] == "Fist":
    print("Güçlü yumruk! Bu bir saldiri isaretidir dikkatli ol")
elif class_name[2:-1] == "Open Palm":
    print("Açık el!Bircok ulkede bu selam anlamina gelmektedir")



bot.run("000000000000000")