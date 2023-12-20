import disnake
from disnake.ext import commands
from random import choice
import math
import asyncio
import codecs
import os
bot=commands.Bot(help_command=None,intents=disnake.Intents.all())

def get_file_path(id):

    filename = str(id)+".txt"

    folder_dir = os.path.dirname(__file__)

    # creates the "config" folder if it doesnt exist
    folder_dir = os.path.join(folder_dir, "config")
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)
    h=os.path.join(folder_dir, filename)
    if not os.path.exists(h):
        with open(h, "w") as f: pass

    return os.path.join(folder_dir, filename)

def openfile(guild_id):
    return codecs.open(get_file_path(guild_id), encoding="utf-8")

# it is like openfile() but for editing
def editfile(guild_id):
    return codecs.open(get_file_path(guild_id), "w", encoding="utf-8")

# add line to the end of the file:
def altteotf(guild_id,line):
    file_list=openfile(guild_id).read().split("\n")
    with codecs.open(get_file_path(guild_id), "w", encoding="utf-8") as file:
        for every in file_list:
            if every!="":
                file.write(f"{every}\n")
        file.write(line)

# remove line from the file:
def rlfrf(guild_id, line):
    file_list=openfile(guild_id).read().split("\n")
    typingemoji=""
    for every in file_list:
        if every!=line:
            typingemoji+=f"{every}\n"
    editfile(guild_id).write(typingemoji[:-1])

def makeembed(page, list):
    pages = math.ceil(len(list)/10)
    uhhh=""
    if list == ['']:
        return disnake.Embed(description="there is no tags you idiot")
    elif page == pages:
        for every in list[10*(page-1):]:
            uhhh+=f"- {every}\n"
    else:
        for every in list[10*(page-1):10*(page-1)+10]:
            uhhh+=f"- {every}\n"
    return disnake.Embed(title=f"Page {page}/{pages}", description=uhhh)

def makecomponents(uhh):
    if uhh != None:
        components = []
        h = int(uhh[5:uhh.find("/")])
        g = int(uhh[uhh.find("/") + 1:])
        if h != 1:
            components+=[disnake.ui.Button(label="<", style=disnake.ButtonStyle.secondary, custom_id=str(h-1))]
        if h != g:
            components+=[disnake.ui.Button(label=">", style=disnake.ButtonStyle.secondary, custom_id=str(h+1))]
        return components

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

@bot.listen("on_button_click")
async def help_listener(ctx):
    h = ctx.component.custom_id
    t = []
    for every in openfile(ctx.guild.id).read().split("\n"):
        t+=[every.split(";")[0]]
    embed=makeembed(int(h), t)
    await ctx.response.edit_message(embed=embed, components=makecomponents(embed.title))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()

    with openfile(message.guild.id) as file:
        for every in file.read().split("\n"):
            h=every.split(";")
            if len(h)==3 and message.author.id!=flowmeter:
                proglet=False
                if h[1]=="default" and h[0].lower() in balls: proglet=True
                elif h[1]=="=" and h[0].lower()==balls: proglet=True
                elif h[1]=="==" and h[0]==message.content: proglet=True
                elif h[1]=="split" and h[0].lower() in balls.split(): proglet=True
                elif h[1]=="startswith" and balls.startswith(h[0].lower()): proglet=True
                elif h[1]=="endswith" and balls.endswith(h[0].lower()): proglet=True
                if proglet: await message.reply(h[2])

    if balls.startswith("hey flowmeter "):
        if balls[14:].startswith("add tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id==tema5002):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule = message.content[22:]
                h = rule.split(";")
                if rule in openfile(message.guild.id).read().split("\n"):
                    msg = "silly you already have added that tag"
                elif len(h)!=3:
                    msg = f"you need to type **3** arguments here but **{len(h)}** was given"
                elif len(h[0])>100:
                    msg = "keyword cant be longer than 100 symbols"
                elif len(h[2])>500:
                    msg = "reply cant be longer than 500 symbols"
                elif not any(_==h[1] for _ in ["=", "==", "default", "split", "startswith", "endswith"]):
                    msg = "incorrect detection type <:yeh:1183111141409435819>\n"
                elif "\n" in rule:
                    msg = "you cant word wrap"
                else:
                    altteotf(message.guild.id, rule)
                    msg = f"`{rule}` was added to **{message.guild.name}**'s tags"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[14:].startswith("remove tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id==tema5002):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule=message.content[25:]
                for every in openfile(message.guild.id).read().split("\n"):
                    if every.split(";")[0]==rule:
                        rule=every
                if rule in openfile(message.guild.id).read().split("\n"):
                    rlfrf(message.guild.id, rule)
                    msg = f"`{rule}` was removed from **{message.guild.name}**'s tags"
                else:
                    msg = f"`{rule}` is not an actual tag you silly"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[14:]=="list tags":
            t=[]
            for every in openfile(message.guild.id).read().split("\n"):
                t+=[every.split(";")[0]]
            embed=makeembed(1, t) 
            await message.channel.send(embed=embed, components=makecomponents(embed.title))

        elif balls[14:]=="sort tags":
            if not(message.guild.owner_id==message.author.id or message.author.id==tema5002):
                await message.channel.send("perms issue "+"<:pointlaugh:1128309108001484882>"*5)
            else:
                input_list=sorted(openfile(message.guild.id).readlines())
                with editfile(message.guild.id) as output:
                    for every in input_list:
                        output.write(every)
                await message.channel.send("oke it sorted i think")

@bot.slash_command(name="help",description="help")
async def help(ctx):
    embed=disnake.Embed(title="Flowmeter",color=0x00FFFF,description=
        "bot made by tema5002\n\n"+
        "how to use it:\n"+
        "> Commands Arguments\n"+
        "> - **keyword** - keyword which triggers the reply\n"+
        "> - **detection_type**:\n"+
        "> - - **default** - triggers if **keyword** in message content (not case sensitive)\n"+
        "> - - **split** - i have no clue how do i explain but it uses python `.split()`\n"+
        "> - - **=** - match\n"+
        "> - - **==** - exact match (it means case sensitive)\n"
        "> - - **startswith** - triggers when **reply** starts with **keyword**\n"
        "> - - **endswith** - triggers when **reply** ends with **keyword**\n"+
        "> - **reply** - uhhhh a reply maybe\n"+
        "> Say *hey flowmeter add tag keyword;detection_type;reply* to **add new tag**\n"+
        "> Say *hey flowmeter remove tag keyword* to **remove tag**\n"+
        "> Say *hey flowmeter list tags* to **list existing tags on this server**\n"+
        "> Say *hey flowmeter sort tags* to sort all tags on this server in alphabetic order\n"+
        "[support server](https://discord.gg/kCStS6pYqr) (kind of)")
    await ctx.send(embed=embed)

@bot.slash_command(name="ping",description="shows ping")
async def ping(ctx):
    await ctx.response.defer()
    h=round(bot.latency*1000)
    await ctx.send(f"<:ammeter:1181921753790939146>📡\n<:flowmeter:1185673481258545233>📡<:blank:1185673931894554715> <--[{h}ms]--> <:blank:1185673931894554715><:discord:1185673704370352208>")

bot.run(open("TOKEN.txt").read())
