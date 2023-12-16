import disnake
from disnake.ext import commands
from random import choice
import asyncio
import codecs
import os
bot=commands.Bot(help_command=None,intents=disnake.Intents.all())

def get_file_path(id):

    filename = str(id)+".txt"

    folder_dir = os.path.dirname(__file__)

    # creates the "config" folder if it doesnt exist
    folder_dir = os.path.join(folder_dir, "config")
    if not os.path.exists(folder_dir): os.makedirs(folder_dir)

    return os.path.join(folder_dir, filename)

# i store user ids here
tema5002=558979299177136164
flowmeter=1184192159944028200

games=[
    "Minecraft",
    "Half-Life 2",
    "Among Us",
    "CMMM+MM",
    "Crazy Machines 3",
    "Tetris",
    "Minesweeper",
    "Mindustry",
    "Worms Armageddon",
    "Baba is You",
    "Cell Machine Indev",
    "Geometry Dash",
    "VVVVVV",
    "Infinitode 2",
    "Minecraft Launcher",
    "Source Filmmaker",
    "Blender",
    "Code::Blocks 20.03"
    ]

@bot.event
async def on_ready():
    print(f"@{bot.user} is now online")

    while True:
        await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(choice(games)))
        await asyncio.sleep(60)

@bot.event
async def on_guild_remove(guild):
    channel=bot.get_channel(1183416187326038110)
    try: await channel.send(f"**{guild.owner.name}** пидорас тупой он меня по IP забанил с сервера **{guild.name}** :hugging::hugging::hugging::smiling_face_with_3_hearts::smiling_face_with_3_hearts::exploding_head::relaxed::relaxed::relaxed::kissing_heart::kissing_heart::kissing_heart::heart_eyes::heart_eyes::blush::blush::kissing_closed_eyes::kissing_closed_eyes:")
    except: await channel.send("i got removed from some server which name i dont know")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()
    if balls.startswith("hey flowmeter "):
        if balls[14:].startswith("add tag "):
            if not(message.guild.owner_id==message.author.id or message.author.id==tema5002):
                await message.channel.send("perms issue "+"<:pointlaugh:1128309108001484882>"*5)
            else:
                d=message.content[22:]
                h=d.split(";")
                if d in codecs.open(get_file_path(message.guild.id), encoding="utf-8").read().split("\n"):
                    await message.channel.send("silly you already have added that tag")
                else:
                    if len(h)!=3: await message.channel.send(f"you need to type **3** arguments here but **{len(h)}** was given")
                    else:
                        if h[1]!="default" and h[1]!="=" and h[1]!="==":
                            await message.channel.send("incorrect detection type <:yeh:1183111141409435819>")
                        else:
                            typingemoji=""
                            try:
                                for every in codecs.open(get_file_path(message.guild.id), encoding="utf-8").read().split("\n")+[d]:
                                    if every!="": typingemoji+=f"{every}\n"
                                with codecs.open(get_file_path(message.guild.id),"w", encoding="utf-8") as file:
                                    file.write(typingemoji[:-1])
                                await message.channel.send(f"`{d}` was added to **{message.guild.name}**'s tags")
                            except:
                                await message.channel.send("cant encode 💀💀💀")

        elif balls[14:].startswith("remove tag "):
            h=codecs.open(get_file_path(message.guild.id), encoding="utf-8").read().split("\n")
            d=message.content[25:]
            for every in h:
                if every.split(";")[0]==d:
                    d=every
            if d in h:
                typingemoji=""
                for every in h:
                    if every!="" and every!=d: typingemoji+=f"{every}\n"
                with codecs.open(get_file_path(message.guild.id), "w", encoding="utf-8") as file:
                    file.write(typingemoji[:-1])
                await message.channel.send(f"`{d}` was removed from **{message.guild.name}**'s tags")
            else: await message.channel.send(f"`{d}` is not an actual tag you silly")
        elif balls[14:]=="list tags":
            t=""
            with codecs.open(get_file_path(message.guild.id), encoding="utf-8") as file:
                list=file.read().split("\n")
            for every in list:
                h=every.split(";")
                t+=h[0]+"\n"
            await message.channel.send(t)
    with codecs.open(get_file_path(message.guild.id), encoding="utf-8") as file:
        list=file.read().split("\n")
        for every in list:
            h=every.split(";")
            if len(h)==3 and message.author.id!=flowmeter:
                proglet=False
                if h[1]=="default" and h[0].lower() in balls: proglet=True
                elif h[1]=="=" and h[0].lower()==balls: proglet=True
                elif h[1]=="==" and h[0]==balls: proglet=True
                if proglet: await message.channel.send(h[2])

@bot.slash_command(name="add_tag",description="add tag")
async def send_splash_here(ctx):
    pass

@bot.slash_command(name="help",description="help")
async def help(ctx):
    embed=disnake.Embed(title="Flowmeter",color=0x00FFFF,description=
        "bot made by tema5002\n\n"+
        "how to use it:\n"+
        "> Commands Arguments\n"+
        "> - **keyword** - keyword which triggers the reply\n"+
        "> - **detection_type**:\n"+
        "> - - **default** - triggers if **keyword** in message content (not case sensitive)\n"+
        "> - - **=** - match\n"+
        "> - - **==** - exact match (it means case sensitive)\n"+
        "> - **reply** - uhhhh a reply maybe\n"+
        "> You can use /add_tag slash command or say *hey flowmeter add tag keyword;detection_type;reply* to **add new tag**\n"+
        "> You can use /remove_tag slash command or say *hey flowmeter remove tag keyword* to **remove tag**\n"+
        "> You can use *hey flowmeter list tags* to **list existing tags on this server**\n"+
        "[support server](https://discord.gg/kCStS6pYqr) (kind of)")
    await ctx.send(embed=embed)

bot.run(open("TOKEN.txt").read())
