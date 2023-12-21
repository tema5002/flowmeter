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

def filereadlines(guild_id):
    return codecs.open(get_file_path(guild_id), encoding="utf-8").readlines()

# it is like openfile() but for editing
def editfile(guild_id):
    return codecs.open(get_file_path(guild_id), "w", encoding="utf-8")

# add line to the end of the file:
def altteotf(guild_id,line):
    file_list=filereadlines(guild_id)
    with editfile(guild_id) as file:
        for every in file_list:
            if every!="":
                file.write(every)
        file.write("\n"+line)

# remove line from the file:
def rlfrf(guild_id, line):
    file_list=filereadlines(guild_id)
    typingemoji=""
    for every in file_list:
        if every!=line:
            typingemoji+=f"{every}"
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

trustedpeople=[
    558979299177136164,  # tema5002
    903650492754845728,  # slinx92
    1163914091270787125, # dtpls20
    801078409076670494,  # hexahedron1
    1143072932596305932, # kesslon1632
    1186681736936050691, # ammeter.
    1122540181984120924, # voltmeter2
    1172796751216906351  # aperturesanity
    ]

# bot's id here so it ignores itself
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
    "Code::Blocks 20.03",
    "wuggy games"
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
    for every in filereadlines(ctx.guild.id):
        t+=[every.split(";")[0]]
    embed=makeembed(int(h), t)
    await ctx.response.edit_message(embed=embed, components=makecomponents(embed.title))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()

    for every in filereadlines(message.guild.id):
        h=every.split(";")
        if len(h)==3 and message.author.id!=flowmeter:
            proglet=False
            k=h[0]
            content=h[2][:-1]
            kl=k.lower()
            if  (h[1]=="default"    and kl in balls          ) or \
                (h[1]=="="          and kl==balls            ) or \
                (h[1]=="=="         and k==message.content   ) or \
                (h[1]=="split"      and kl in balls.split()  ) or \
                (h[1]=="startswith" and balls.startswith(kl) ) or \
                (h[1]=="endswith"   and balls.endswith(kl)   ):
                    if content.endswith("DELETE"):
                        await message.reply(content[:-6])
                        try: await message.delete()
                        except: await message.channel.send("nevermind cant delete messages :skull:")
                    else:
                        await message.reply(content)

    if balls.startswith("hey flowmeter "):
        if balls[14:].startswith("add tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule = message.content[22:]
                h = rule.split(";")
                if rule in filereadlines(message.guild.id):
                    msg = "silly you already have added that tag"
                elif len(h)!=3:
                    msg = f"you need to type **3** arguments here but **{len(h)}** was given"
                elif len(h[0])>125:
                    msg = "keyword cant be longer than 125 symbols"
                elif len(h[2])>500:
                    msg = "reply cant be longer than 500 symbols"
                elif not any(_==h[1] for _ in ["=", "==", "default", "split", "startswith", "endswith"]):
                    msg = "incorrect detection type <:yeh:1183111141409435819>\n"
                elif "\n" in rule:
                    msg = "you cant word wrap"
                elif h[1]=="split" and " " in h[0]:
                    msg = "you cant use spaces with **split** detection type!"
                elif h[0].strip()=="" or h[2].strip().replace("DELETE","")=="":
                    msg = "<:pangooin:1153354856032116808>"
                else:
                    rule=rule[:rule.find(";")].strip()+rule[rule.find(";"):]
                    altteotf(message.guild.id, rule)
                    msg = f"`{rule}` was added to **{message.guild.name}**'s tags"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[14:].startswith("remove tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule=message.content[25:]
                for every in filereadlines(message.guild.id):
                    if every.split(";")[0]==rule:
                        rule=every
                if rule in filereadlines(message.guild.id):
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
            for every in filereadlines(message.guild.id):
                t+=[every.split(";")[0]]
            embed=makeembed(1, t) 
            await message.channel.send(embed=embed, components=makecomponents(embed.title))

        elif balls[14:]=="sort tags":
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                await message.channel.send("perms issue "+"<:pointlaugh:1128309108001484882>"*5)
            else:
                input_list=sorted(filereadlines(message.guild.id))
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
        "> - - If **keyword** ends with `DELETE` message will be deleted\n"+
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
        "[support server](https://discord.gg/kCStS6pYqr) (kind of) | [source code](https://github.com/tema5002/flowmeter)")
    await ctx.send(embed=embed)

@bot.slash_command(name="ping",description="shows ping")
async def ping(ctx):
    await ctx.response.defer()
    h=round(bot.latency*1000)
    await ctx.send(f"<:ammeter:1181921753790939146>📡\n<:flowmeter:1185673481258545233>📡<:blank:1185673931894554715> <--[{h}ms]--> <:blank:1185673931894554715><:discord:1185673704370352208>")

bot.run(open("TOKEN.txt").read())
