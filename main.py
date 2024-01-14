prefix="hey flowmeter " # enter whatever you want here

import disnake, math, asyncio, codecs, os, pickle, emoji
from disnake.ext import commands
from random import choice

bot=commands.Bot(command_prefix="fm!", help_command=None, intents=disnake.Intents.all())

def isemoji(string, ctx_guild_emojis):
    if string.isdigit():
        char = bot.get_emoji(int(string))
        if char!=None and char in ctx_guild_emojis:
            return True
    return emoji.is_emoji(string)

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

def readfile(guild_id):
    return codecs.open(get_file_path(guild_id), encoding="utf-8").read().split("\n")

# it is like openfile() but for editing
def editfile(guild_id):
    return codecs.open(get_file_path(guild_id), "w", encoding="utf-8")

# this is for whatever you want
def smthfile(guild_id, readingmode):
    return codecs.open(get_file_path(guild_id), readingmode, encoding="utf-8")

# add line to the end of the file:
def altteotf(guild_id, line):
    with smthfile(guild_id, "a+") as file:
        file.seek(0)
        if file.read():
            file.seek(0, 2)
            file.write("\n")
        file.write(line)

# remove line from the file:
def rlfrf(guild_id, line):
    typingemoji=""
    for every in readfile(guild_id):
        if every != line:
            typingemoji+=f"{every}\n"
    editfile(guild_id).write(typingemoji[:-1])

def update_line(guild_id, oldLine, newLine):
    typingemoji=""
    for every in readfile(guild_id):
        if every != oldLine:
            typingemoji+=every
        else:
            typingemoji+=newLine
        typingemoji+="\n"
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
    710621353128099901,  # rech2020
    712639066373619754,  # aflyde
    1186681736936050691, # ammeter.
    1122540181984120924, # voltmeter2
    1172796751216906351  # aperturesanity
    ]

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
    for every in readfile(ctx.guild.id):
        t+=[every.split(";")[0]]
    embed=makeembed(int(h), t)
    await ctx.response.edit_message(embed=embed, components=makecomponents(embed.title))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()

    for every in readfile(message.guild.id):
        h=every.split(";")
        if 3<=len(h)<=4 and message.author!=bot.user:
            lenh=len(h)
            k=h[0]
            content=h[2]
            if lenh==4: reply_type=h[3].lower()
            kl=k.lower()
            if  (h[1]=="default"    and kl in balls          ) or \
                (h[1]=="="          and kl==balls            ) or \
                (h[1]=="=="         and k==message.content   ) or \
                (h[1]=="split"      and kl in balls.split()  ) or \
                (h[1]=="startswith" and balls.startswith(kl) ) or \
                (h[1]=="endswith"   and balls.endswith(kl)   ):
                    if h[0]=="amigger" and h[2]=="amigger and his family 😂😂😀":
                        content = choice(pickle.load(open("amiggerquotes.dat", "rb")))
                    if h[0]=="mrkrabs":
                        content = choice(pickle.load(open("mrkrabsquotes.dat", "rb")))
                    if lenh==4 and reply_type=="react":
                        if h[2].isdigit():
                            emoji = bot.get_emoji(int(h[2]))
                            if emoji:
                                await message.add_reaction()
                            else:
                                await message.channel.send(f"couldn't find emoji with id `{h[2]}`", delete_after=10)
                        else: await message.add_reaction(h[2])
                    else:
                        await message.channel.send(content)
                    delete = False
                    if lenh==4 and reply_type=="delete":
                        try:
                            await message.delete()
                        except disnake.MissingPermission:
                            await message.channel.send("nevermind cant delete messages <:yeh:1183111141409435819>")

    if balls.startswith(prefix):
        if balls[len(prefix):].startswith("add tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule = message.content[len(prefix)+8:]
                h = rule.split(";")
                if any(rule[:rule.find(";")]==_[:_.find(";")] for _ in readfile(message.guild.id)):
                    msg = "silly you already have added that tag"
                elif not 3<=len(h)<=4:
                    msg = f"you need to type **3**/**4** arguments here but **{len(h)}** was given"
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
                elif h[0].strip()=="" or h[2].strip()=="":
                    msg = "<:pangooin:1153354856032116808>"
                elif (len(h)>3 and h[3].lower()=="react" and not isemoji(h[2], message.guild.emojis)):
                    msg = "you either entered emoji from another server or its not an emoji <:typing:1133071627370897580>"
                #elif message.guild.id==938770488702951545:
                #    msg = "your server was added to blacklist you cant create tags go and cry about it <:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882>"
                else:
                    rule=rule[:rule.find(";")].strip()+rule[rule.find(";"):]
                    altteotf(message.guild.id, rule)
                    msg = f"`{rule}` was added to **{message.guild.name}**'s tags"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[len(prefix):].startswith("update tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule = message.content[len(prefix)+11:]
                h = rule.split(";")
                if not any(rule[:rule.find(";")]==_[:_.find(";")] for _ in readfile(message.guild.id)):
                    msg = "you havent added that tag yet"
                elif not 3<=len(h)<=4:
                    msg = f"you need to type **3**/**4** arguments here but **{len(h)}** was given"
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
                elif h[0].strip()=="" or h[2].strip()=="":
                    msg = "<:pangooin:1153354856032116808>"
                elif (len(h)>3 and h[3].lower()=="react" and not isemoji(h[2], message.guild.emojis)):
                    msg = "you either entered emoji from another server or its not an emoji <:typing:1133071627370897580>"
                #elif message.guild.id==938770488702951545:
                #    msg = "your server was added to blacklist you cant create tags go and cry about it <:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882><:pointlaugh:1128309108001484882>"
                else:
                    for every in readfile(message.guild.id):
                        if every.split(";")[0]==h[0]:
                            oldRule=every
                    rule=rule[:rule.find(";")].strip()+rule[rule.find(";"):]
                    update_line(message.guild.id, oldRule, rule)
                    msg = f"updated `{oldRule}` to `{rule}` on **{message.guild.name}**"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[len(prefix):].startswith("remove tag ") and not message.author.bot:
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                msg = "perms issue "+"<:pointlaugh:1128309108001484882>"*5
            else:
                rule=message.content[len(prefix)+11:]
                for every in readfile(message.guild.id):
                    if every.split(";")[0]==rule:
                        rule=every
                if rule in readfile(message.guild.id):
                    rlfrf(message.guild.id, rule)
                    msg = f"`{rule}` was removed from **{message.guild.name}**'s tags"
                else:
                    msg = f"`{rule}` is not an actual tag you silly"
            try:
                await message.channel.send(msg)
            except:
                print("cant send message wota hell")

        elif balls[len(prefix):]=="list tags":
            t=[]
            for every in readfile(message.guild.id):
                t+=[every.split(";")[0]]
            embed=makeembed(1, t)
            await message.channel.send(embed=embed, components=makecomponents(embed.title))

        elif balls[len(prefix):]=="sort tags":
            if not(message.guild.owner_id==message.author.id or message.author.id in trustedpeople):
                await message.channel.send("perms issue "+"<:pointlaugh:1128309108001484882>"*5)
            else:
                typingemoji=""
                for every in sorted(readfile(message.guild.id)):
                    typingemoji += every+"\n"
                with editfile(message.guild.id) as output:
                    output.write(typingemoji[:-1])
                await message.channel.send("oke it sorted i think")

@bot.slash_command(name="help",description="help")
async def help(ctx):
    embed=disnake.Embed(title="Flowmeter",color=0x00FFFF,description=
        "bot made by tema5002\n\n"+
       f"> Say *{prefix}add tag keyword;detection_type;reply;reply_type* to **add new tag**\n"+
       f"> Say *{prefix}remove tag keyword* to **remove tag**\n"+
       f"> Say *{prefix}list tags* to **list existing tags on this server**\n"+
       f"> Say *{prefix}sort tags* to sort all tags on this server in alphabetic order\n"+
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
        "> - - If you use \"react\" in reply must be an emoji id or emoji itself if its unicode\n"+
        "> - **reply_type**\n"+
        "> - - react - read lines above"
        "> - - delete - deletes the message"
        "[support server](https://discord.gg/kCStS6pYqr) (kind of) | [source code](https://github.com/tema5002/flowmeter)")
    await ctx.send(embed=embed)

@bot.slash_command(name="ping",description="shows ping")
async def ping(ctx):
    await ctx.response.defer()
    h=round(bot.latency*1000)
    await ctx.send(f"<:ammeter:1181921753790939146>📡\n<:flowmeter:1185673481258545233>📡<:blank:1185673931894554715> <--[{h}ms]--> <:blank:1185673931894554715><:discord:1185673704370352208>")

bot.run(open("TOKEN.txt").read())
