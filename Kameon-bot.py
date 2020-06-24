import discord
from discord.ext import commands
from random import choice, randint
import aiohttp
import random
from datetime import timedelta
from asyncio import sleep
import asyncio
import requests
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import datetime
import os
import wikipedia
import nekos
#import youtube_dl


Bot = commands.Bot(command_prefix='k!')
Bot.remove_command('help')


@Bot.event
async def on_ready():
    print("Bot is online")
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('k!help'))


hueplet_chance = 5
prefix = "k!"


@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    if message.channel.id == 723252561758388276 or message.channel.id == 723888963521347594:
        await message.add_reaction("✅")
        await message.add_reaction("❎")




@Bot.command()
async def userinfo(ctx, Member: discord.Member = None):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles)
    emb = discord.Embed(title='Про {}'.format(Member.name),
                        description=f"Когда присоеденился к серверу: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                    f"Имя пользователя: {Member.name}\n\n"

                                    f"Ник на сервере: {Member.nick}\n\n"
                                    f"Статус: {Member.status}\n\n"
                                    f"ID: {Member.id}\n\n"
                                    f"Наивысшая роль: {Member.top_role}\n\n"
                                    f"Когда был создан аккаунт пользователя: {Member.created_at.strftime('%b %#d, %Y')}",
                        color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url=Member.avatar_url)
    emb.set_footer(icon_url=Member.avatar_url)
    emb.set_footer(text='Запросил: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@Bot.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    await ctx.message.delete()
    embed = discord.Embed(title=f'{user}`s avatar', description= f'[link here]({user.avatar_url})', color=user.color)
    embed.set_footer(text= f'Запросил: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    embed.set_image(url=user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@Bot.command()
async def emoji(ctx, emotie: discord.Emoji):
    if emotie == None:
        await ctx.message.delete()
        await ctx.send('Обязательно введите эмодзи!!!')
    else:
        await ctx.message.delete()
        color = discord.Colour.red()
        emb = discord.Embed(title = 'Держи своё емодзи', colour = color)
        emb.set_image(url = emotie.url)
        await ctx.send(embed=emb)
    
       
@Bot.command()
async def domination(ctx):
    pass


@Bot.command()
async def my_roles(ctx):
    for i in ctx.guild.members:
        for j in i.roles:
            await i.send(j.name)


@Bot.command()
@commands.has_permissions(administrator=True)  # Могут использовать лишь пользователи с правами Администратора
async def say(ctx, channel: discord.TextChannel, *, cnt):  # Удаляет написанное вами сообщение
    await channel.send(cnt)

    
POST_ID = 725083322614808697

ROLES = {
'🟩': 724953981373251694,
'🟪': 724953899265687592, 
'🟧': 725069938875695204,
'🟥': 725069721510346762, 
'🟦': 724954042744176660, 
}

EXCROLES = () 

MAX_ROLES_PER_USER = 7







@Bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == POST_ID:
        channel = Bot.get_channel(payload.channel_id) 
        message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
    try:
        emoji = str(payload.emoji) # эмоджик который выбрал юзер
        role = utils.get(message.guild.roles, id=ROLES[emoji]) # объект выбранной роли (если есть)
           
        if(len([i for i in member.roles if i.id not in EXCROLES]) <= MAX_ROLES_PER_USER):
            await member.add_roles(role)
            print('[log] Участнику - {0.display_name}, успешно была выдана роль: {1.name}'.format(member, role))
        else:
            await message.remove_reaction(payload.emoji, member)
            print('[log] У {0.display_name} слишком много ролей, что-бы выдать еще...'.format(member))
           
    except KeyError as e:
        print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
    except Exception as e:
        print(repr(e))


@Bot.event
async def on_raw_reaction_remove(payload):
    channel = Bot.get_channel(payload.channel_id) 
    message = await channel.fetch_message(payload.message_id)
    member = utils.get(message.guild.members, id=payload.user_id)
 
    try:
        emoji = str(payload.emoji)
        role = utils.get(message.guild.roles, id=ROLES[emoji])
 
        await member.remove_roles(role)
        print('[log] Роль - {1.name}, была успешно снята у участника: {0.display_name}'.format(member, role))
 
    except KeyError as e:
        print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
    except Exception as e:
        print(repr(e))



@Bot.event
async def on_message_delete(message):
    channelDelete = discord.utils.get(message.guild.channels, id = 725064979039911966)
    DeleteMessage = discord.Embed(title= 'Сообщение было удалено', color = 0x383a3d)
    DeleteMessage.add_field(name= 'Удалённое сообщение:', value = f'{message.content}')
    DeleteMessage.add_field(name= 'Автор удалённого сообщения:', value = f'{message.author.mention}')
    DeleteMessage.add_field(name= 'В канале:', value = f'{message.channel}')
    for a in message.attachments:
        if a.filename.endswith(('.jpg', '.jpeg', '.png')):
            DeleteMessage.set_image(url = a.proxy_url)
    await channelDelete.send(embed = DeleteMessage)
 

@Bot.command()
async def send_ch(ctx, text):
    await ctx.send(f'{message.author.mention}, сказал {text}')
    
@Bot.command()
async def user(ctx, member: discord.Member):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)

    embed.set_author(name = f"Информация пользователя - {member} ")
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(text = f"Запросил : {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name = "ID", value = member.id)
    embed.add_field(name = "Name", value = member.display_name)

    embed.add_field(name = "Зарегистрирован ", value = member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))
    embed.add_field(name = "Вошел на сервер", value = member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))

    embed.add_field(name = f"Роли({len(roles)})", value = "".join(role.mention for role in roles))
    embed.add_field(name = "Высшая роль", value = member.top_role.mention)


    await ctx.send(embed = embed)
   
@Bot.command()
async def report(ctx, member:discord.Member=None, *, arg=None):
    message = ctx.message
    channel = Bot.get_channel(724934926167834698)    
    if member == None:
        await ctx.send(embed=discord.Embed(description='Укажите пользователя!', color=discord.Color.red()))
    elif arg == None:
        await ctx.send(embed=discord.Embed(description='Укажите причину жалобы!', color=discord.Color.red()))
    else:
        emb = discord.Embed(title=f'Жалоба на пользователя {member}', color=discord.Color.blue())
        emb.add_field(name='Автор жалобы:', value=f'*{ctx.author}*')
        emb.add_field(name='Причина:', value='*' +arg + '*')
        emb.add_field(name='ID жалобы:', value=f'{message.id}')
        await channel.send(embed=emb)
        await ctx.author.send('✅ Ваша жалоба успешно отправлена!')


@Bot.command()
async def wiki(ctx, *, text):
    wikipedia.set_lang("ru")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(
        title= new_page.title,
        description= summ,
        color = 0xc582ff)

    await ctx.send(embed=emb)
    
@Bot.command()
async def r_text(ctx, *, args):
    await ctx.send(f"{''.join(random.sample(args,len(args)))}")

@Bot.command()
async def weather(ctx, *, name):
    def prognoz(href):
        r = requests.Session()
        res = r.get(href)
        ans = bs(res.content, 'html.parser')
        weather = ans.findChildren('body')[0]
        Weather = weather.find('div', class_='det_pog')
        return Weather.find('p').get_text()
        r.close()

    s = requests.Session()
    res = s.get('https://goodmeteo.ru/poisk/?s=' + name)
    s.close()

    try:
        await ctx.send('**Расчитываем прогноз на сегодня...**')
        ans_bs = bs(res.content, 'html.parser')
        Choose = ans_bs.find_all('div', class_='search_line')[0]
        search_name = Choose.find_all('a', target="_blank")[0].get_text().replace(' ', '')
        search_href = 'https://goodmeteo.ru' + Choose.find_all('a', target="_blank")[0]['href']
        await ctx.send(prognoz(search_href))
    except IndexError:
        await ctx.send('**Ничего не найдено, попробуйте изменить поиск**')


@Bot.command()
async def time(ctx):
    emb = discord.Embed(title='Мск время', colour=discord.Colour.red(),
                        url='https://www.timeserver.ru/cities/ru/moscow')
    emb.set_author(name=Bot.user.name, icon_url=Bot.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://i.gifer.com/WnEJ.gif')
    now_time = datetime.datetime.now()
    emb.add_field(name='Time:', value=f'{now_time}'[:19])
    await ctx.send(embed=emb)


@Bot.command()
async def cat(ctx):
    emb = discord.Embed(description= f'**Вот тебе котик:**', color=0x6fdb9e)
    emb.set_image(url=nekos.cat())
    await ctx.send(embed=emb)
    
 
@Bot.event
async def on_member_join(member):
    if member.guild.id == int(701723124202471455):
        await Bot.get_channel(709019591535493151).send(f"Приветствую тебя на нашем сервере, {member.mention}!")
                   
@Bot.event
async def on_member_remove(member):
    if member.guild.id == int(701723124202471455):
        await Bot.get_channel(724917766565658656).send(f'Пока {member}!')
        await member.send(f'Пока {member.mention}, надеюсь ты к нам ещё вернёшся, если что то вот ссылка ')
    
                      
                   
@Bot.command()
async def ran_color(ctx):
    clr = (random.randint(0, 16777215))
    emb = discord.Embed(
        description=f'Сгенерированый цвет : ``#{hex(clr)[2:]}``',
        colour=clr
    )

    await ctx.send(embed=emb)

# оно блять даже не работает 🤦
@Bot.command()
async def num_msg(ctx, member: discord.Member = None):
    user = ctx.message.author if (member == None) else member
    number = await Messages(Bot).number_messages(user)
    embed = discord.Embed(description=f"Количество сообщений на сервере от **{user.name}** — **{number}**!",
                          colour=discord.Colour.green())
    await ctx.send(embed=embed)

    
@Bot.command()
async def dog(ctx):
    emb = discord.Embed(description= f'**Вот тебе собачка:**', color=0x6fdb9e)
    emb.set_image(url=nekos.dog())
    await ctx.send(embed=emb)
    
@Bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@Bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(description=f"Удалено {amount} сообщений", color=discord.Colour.green())
    await ctx.send(embed=embed, delete_after = 3)


@Bot.command()
async def genpass(ctx, lenght: int, number: int):
    if not lenght or not number:
        await ctx.send('Укажите длину и количество символов')
    else:
        chars = '1234567890!"№;%:?*()-_+=йцукенгшщзхъфывапролджэячсмитьбю.qwertyuiopasdfghjkl:"|zxcvbnm,.<\>?`~ЁёQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬ'

        for x in range(number):
            password = ''

            for i in range(lenght):
                password += random.choice(chars)
            await ctx.send(embed=discord.Embed(description=f'{password}'))


@Bot.command()
async def text_timer(ctx, text: str):
    await ctx.send(f'Длина текста: {len(text)} симвал/ов/а')


def time_repr(td: timedelta) -> str:
    "Time formatter with optional dates/hours"
    minutes, seconds = divmod(int(td.total_seconds()), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    res = f"{minutes:>02}:{seconds:>02}"
    if hours or days:
        res = f"{hours:>02}:" + res
    if days:
        res = f"{td.days} days, " + res
    return res


@Bot.command()
async def countdown(ctx, seconds: int):
    td = timedelta(seconds=seconds)
    while True:
        await ctx.send(time_repr(td))
        if td.total_seconds() > 30:
            td -= timedelta(seconds=1)
            await sleep(1)
        elif td.total_seconds() > 10:
            td -= timedelta(seconds=1)
            await sleep(1)
        elif td.total_seconds() > 1:
            td -= timedelta(seconds=1)
            await sleep(1)
        else:
            break


@Bot.command()
@commands.has_any_role('КАРАТЕЛЬ')
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.kick(member)


@Bot.command()
@commands.has_any_role('КАРАТЕЛЬ')
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(member)


@Bot.command(aliases=['коронавирус'])
async def cov(ctx):
    Corona = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/#operational-data'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    full_page = requests.get(Corona, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("div", {"class": "cv-countdown__item-value"})
    hz = soup.find("div", {"class": "cv-banner__description"})

    heads = []
    for i in convert:
        heads.append(i.string)

    emb = discord.Embed(title=f"Данные по короновирусу. {hz.string}", color=708090)
    emb.set_author(name=Bot.user.name, icon_url=Bot.user.avatar_url)
    emb.add_field(name="Заболело: ", value=heads[1], inline=False)
    emb.add_field(name="Выздоровело: ", value=heads[3], inline=False)
    emb.add_field(name="Умерло: ", value=heads[4], inline=False)
    emb.set_thumbnail(
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Biohazard_orange.svg/1200px-Biohazard_orange.svg.png')
    await ctx.send(embed=emb)


@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title='__**ОШИБКА**__', colour=discord.Colour.red())
        emb.add_field(name='Ошибка:',
                      value=f'{ctx.author.mention}, Обязательно укажите город в котором вы хотите узнать погоду:exclamation:')
        emb.set_thumbnail(url='https://i.gifer.com/72gi.gif')
        await ctx.send(embed=emb)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title='__**ОШИБКА**__', colour=discord.Colour.red())
        emb.add_field(name='Ошибка:',
                      value=f'{ctx.author.mention}, Обязательно укажите число сообщений корые вы хотите удалить:exclamation:')
        emb.set_thumbnail(url='https://i.gifer.com/72gi.gif')
        await ctx.send(embed=emb)


@Bot.command()
async def send(ctx, id, *, text: str = None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Спасибо за ваше предложение, оно отправлено в #{id}")
    channel1 = discord.utils.get(ctx.guild.channels, id=id)
    offer = discord.Embed(color=0xFF1818, description=f'{text}')
    await channel1.send(embed=offer)


@Bot.command()
@commands.has_permissions(administrator=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    global voice
    voice = discord.utils.get(Bot.voice_clients)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send("Я присоеденился к голосовому каналу!")


@Bot.command()
@commands.has_permissions(administrator=True)
async def disconnect(ctx):
    for x in Bot.voice_clients:
        if (x.guild == ctx.message.guild):
            await ctx.send("Ок), Я ухожу! Пока:smile:")
            return await x.disconnect()


@Bot.command()
@commands.has_permissions(administrator=True)
async def play_s(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print("[LOG]: Старый файл музыки удалён")
    except PermissionError:
        print("[LOG]: Не удалось удалить файл")
    await ctx.send("Pls wait, it won't take long.")
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestausio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[LOG]: Загружаю музыку')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[LOG]: Переименовываю файл: {file}')
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'[LOG]: {name}, music ended.'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    song_name = name.rsplit('-', 2)
    await ctx.send(f'Np: {song_name[0]}')


@commands.has_any_role('КАРАТЕЛЬ')
async def mute(ctx, member: discord.Member, duration: int, *, arg):
    emb = discord.Embed(title='MUTE')
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    emb.add_field(name="Кто-кого:",
                  value=f'{ctx.author.mention} __**отправил в дурку**__: {member.mention} __**на {duration} секунд.**__')
    emb.add_field(name="Причина:", value=f'__*{arg}*__')
    emb.set_image(url='https://antislang.ru/wp-content/uploads/%D0%B4%D1%83%D1%80%D0%BA%D0%B0-1.jpg')
    await ctx.send(embed=emb)
    await member.add_roles(role)
    await asyncio.sleep(duration)
    embed = discord.Embed(description=f'Товарищ {member.mention} успешно прошёл курс оздаровления в дурке.',
                          color=discord.Colour.green())
    await ctx.send(embed=embed)
    await member.remove_roles(role)


@Bot.command()
async def giveaway(ctx, seconds: int, *, text):
    def time_end_form(seconds):
        h = seconds // 3600
        m = (seconds - h * 3600) // 60
        s = seconds % 60
        if h < 10:
            h = f"0{h}"
        if m < 10:
            m = f"0{m}"
        if s < 10:
            s = f"0{s}"
        time_reward = f"{h} : {m} : {s}"
        return time_reward

    author = ctx.message.author
    time_end = time_end_form(seconds)
    message = await ctx.send(f"Розыгрыш!\nРазыгрывается:{text}\nЗавершится через {time_end}")
    await message.add_reaction("🎲")
    while seconds > -1:
        time_end = time_end_form(seconds)
        text_message = f"Розыгрыш!\nРазыгрывается:{text}\nЗавершится через {time_end}"
        await message.edit(content=text_message)
        await asyncio.sleep(1)
        seconds -= 1
    channel = message.channel
    message_id = message.id
    message = await channel.fetch_message(message_id)
    reaction = message.reactions[0]
    users = await reaction.users().flatten()
    user = choice(users)
    await ctx.send(f'Ахтунг!\n Победитель розыгрыша - {user.mention}!\n '
                   f'Напишите {author.mention}, чтобы получить награду')


@Bot.command()
async def game(ctx):
    a = random.randint(1, 2)
    if a == 1:
        emb = discord.Embed(title='__**Орёл и решка**__', colour=discord.Colour.red(), url='https://castlots.org/')
        emb.add_field(name='Что выпало:', value='*Вам выпал* __**орёл**__')
        emb.set_thumbnail(url='https://i.gifer.com/ZXv0.gif')
        await ctx.send(embed=emb)
        emb.set_footer(text=f"Запросил: {ctx.author}", icon_url=ctx.author.avatar_url)
    else:
        emb = discord.Embed(title='__**Орёл и решка**__', color=discord.Colour.green(), url='https://castlots.org/')
        emb.add_field(name='Что выпало:', value='*Вам выпала* __**решка**__')
        emb.set_thumbnail(url='https://i.gifer.com/ZXv0.gif')
        await ctx.send(embed=emb)
        emb.set_footer(text=f"Запросил: {ctx.author}", icon_url=ctx.author.avatar_url)


@Bot.command()
async def calc(ctx, operarion):
    await ctx.send(f'Ответ: {eval(operarion)}')


@Bot.command()
async def saper(ctx):
    embed = discord.Embed(description='''
                     Держи :smile:
||0️⃣||||0️⃣||||0️⃣||||1️⃣||||1️⃣||||2️⃣||||1️⃣||||2️⃣||||1️⃣||||1️⃣||||
2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||2️⃣||||💥||||3️⃣||||💥||||1️⃣||||
💥||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||3️⃣||||💥||||2️⃣||||1️⃣||||
2️⃣||||2️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||2️⃣||||1️⃣||||1️⃣||||0️⃣||||
0️⃣||||0️⃣||||0️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||0️⃣||||0️⃣||||0️⃣||||
1️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||
💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||💥||||1️⃣||||
1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||2️⃣||||1️⃣||||
1️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||💥||||1️⃣||||0️⃣||||0️⃣||||
💥||||2️⃣||||💥||||1️⃣||||1️⃣||||💥||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||
1️⃣||||2️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||            
    ''', color=discord.Colour.orange())
    await ctx.send(embed=embed)


@Bot.command()
async def choose(ctx, *, args):
    variants = ''.join(args).split(',')
    await ctx.send(f"Я выбираю: {random.choice(variants).replace(' ', ' ')}")


@Bot.command()
async def get_role(ctx, role=None):
    if role == None:
        return await ctx.send("Укажи роль, мудачило")
    elif role.lower() == "программист":
        await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name="Программист"))
        return await ctx.send("выдал тебе программист")
    elif role.lower() == "PUBGm player":
        await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name="PUBGm player"))
        return await ctx.send("выдал тебе PUBGm player")


@Bot.command()
async def help(ctx):
    emb = discord.Embed(title='Навигация по командам :page_with_curl:', colour=discord.Colour.green())
    emb.set_author(name=Bot.user.name, icon_url=Bot.user.avatar_url)
    emb.add_field(name=f'{prefix}game', value='Игра орёл и решка')
    emb.add_field(name=f'{prefix}clear', value='Очистка чата(Доступно лишь адмиинам)')
    emb.add_field(name=f'k!ban либо k!kick', value='Команды для для кика и бана участников сервера')
    emb.add_field(name=f'k!saper', value='Команда для игры --"сапёр"')
    emb.add_field(name=f'k!choose', value='Выбирает любой параметр рандомно. Пример: "k!choose 1 2 3 4"')
    emb.add_field(name=f'k!userinfo', value='Информация об участнике сервера')
    emb.add_field(name=f'k!countdown', value='Таймер(Пример: "k!countdown секунды")')
    emb.add_field(name=f'k!mute', value='Мут участника(Команда доступна лишь людям имеющим роль "КАРАТЕЛЬ")')
    emb.add_field(name=f'k!cov', value='Статистика заболевшим коронавирусом в РФ')
    emb.add_field(name=f'k!weather',
                  value='Подскажет вам погоду в любом городе(прим. "k!weather Москва(можете написать тут любой другой город)")')
    emb.add_field(name=f'k!genpass',
                  value='Генератор пароля (прим. "k!genpass 10(Длина пароля), 1(кол-во паролей котрых надо сгенерировать)")')
    emb.add_field(name=f'k!calc',
                  value='Простой калькулятор(+ = сложить, - = вычесть, * = умножить, / = делить, ** = степень, // = целочисленное деление)')
    emb.add_field(name=f'k!search_video', value='Ищет видео на YouTube(прим. "k!search_video лайфхаки")')
    emb.add_field(name=f'k!text_timer', value='Команды для измерения текста')
    emb.set_footer(text=f"Запросил: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@Bot.command()
async def info(ctx, user: discord.Member):
    emb = discord.Embed(title="Info __{}__".format(user.nick), colour=0x42f4f4)
    emb.set_author(name=Bot.user.name, icon_url=Bot.user.avatar_url)
    emb.add_field(name="Ник на сервере:", value=user.nick)
    emb.add_field(name="Когда присоеденился:", value=str(user.joined_at)[:16])
    emb.set_thumbnail(url=user.avatar_url)
    emb.set_author(name=user.name, url=user.avatar_url)
    await ctx.send(embed=emb)

@Bot.command()
async def load(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}') 
    await ctx.send('loaded')

@Bot.command()
async def reload(ctx, extensions):
    Bot.load_extension(f'cogs.{extensions}')
    Bot.unload_extensions(f'cogs.{extensions}')
    await ctx.send('reloaded')

@Bot.command()
async def unload(ctx, extensions):
    Bot.unload_extension(f'cogs.{extensions}') 
    await ctx.send('unloaded')
    
Bot.load_extension('x0')
               
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
