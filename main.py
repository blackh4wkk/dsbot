import discord
from discord.ext import commands
import time
import random
from typing import List

# {ctx.guild} - возвращает название канала
t = 1

TOKEN = "ODg3NDExNTMzMTY3MDg3NjYw.YUDwZA.vTUnbvO3SNcS70UPimezT8W1wWM"
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Im ready now')
def merge(a, b):
    i = 0
    j = 0
    tmp = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            tmp.append(a[i])
            i+=1
        else:
            tmp.append(b[j])
            j+=1
    tmp += a[i:] + b[j:]
    return tmp
def mergesort(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    if len(a) <= 1:
        return a
    l = a[:len(a)//2]
    r = a[len(a)//2:]
    return merge(mergesort(l), mergesort(r))
    
@bot.command()
async def сортировка(ctx, *args):
    a = list(args)
    a = mergesort(a)
    await ctx.send(a)

@bot.command()
async def помощь(ctx):
    await ctx.send("""**!проверка** - возвращает сегодняшнего пидорасика
**!топ** - топ пидорасов за все время
**!создатель** - создатель
**!добавить <упомянуть пользователя>** - добавляет типа в наше ахуенное сообщество(или шлет нахуй)
**!сортировка a1 a2 ... an** - сортирует числа в порядке возрастания за nlogn
    """)
@bot.command()
async def создатель(ctx):
    await ctx.send(f"Меня создал <@{332807192186978307}> с помощью видосов от индусов")


@bot.command()
async def топ(ctx):
    f = open("data.txt", "r")
    s = f.read()
    s = s.split("\n")
    s.pop(0)
    top1 = []
    # top1 = [[0] * 2] * len(s)
    for i in range(len(s)):
        qq = s[i].split(' - ')
        qq.reverse()
        qq[0] = int(qq[0]) # бегу по строчкам, и в каждой строчке у меня len(A[i]) элементов
        top1.append(qq)
    top1.sort(reverse=True)
    for i in range(len(top1)):
        top1[i].reverse()
    s_list = ""
    for i in range(len(top1)):
        #user =  await bot.fetch_user(int(top1[i][0]))
        user = top1[i][0]
        if top1[i][1] != 0:
            s_list += f'<@{str(user)}>' + ' - ' + str(top1[i][1]) + ' ' + 'раз(а)' + '\n'
        #s_list += f'{str(user)[:-5]}' + ' - ' + top1[i][1] + ' ' + 'раз(а)' + '\n'
    await ctx.send(f'Пидорасами были:\n {s_list}')
    f.close()



@bot.command()
@commands.has_permissions(manage_roles=True)
async def добавить(ctx, user: discord.Member):
    role = discord.utils.get(user.guild.roles, name="pidorbot")
    if role in user.roles:
        await ctx.send(f"{user.mention} уже с нами, пошел нахуй")
    else:
        await user.add_roles(role)
        await ctx.send(f"Теперь ты один из нас, {user.mention}")
        f = open("data.txt", 'a')
        f.write('\n' + str(user.id) + ' - 0')
        f.close()


@bot.command()
async def проверка(ctx):
    n = 86400  # время(в секундах)
    global t
    if time.time() - t >= n:
        ri = int(887681333139210240)
        f = open("data.txt")
        s = f.read()
        s1 = s.split('\n')
        s2 = []
        qq = random.randint(1, len(s1) - 1)
        s2 = s1[qq].split(' - ')
        usrn = str(s2[0])
        numm = int(s2[1])
        numm += 1
        o = usrn + ' - ' + str(numm)
        s1[qq] = o
        f.close()
        f = open('data.txt', 'w')
        for i in range(len(s1)):
            f.write(str(s1[i]))
            if i != len(s1) - 1:
                f.write('\n')
        f.close()
        # usrn1 = usrn.split('#')
        await ctx.send(f"Господа, сегодняшний пидорюга:<@{int(usrn)}>")
        t = time.time()
    else:
        ###############
        s = n - int(time.time() - t)
        m = 0
        while s - 60 > 0:
            s -= 60
            m += 1
        h = 0
        while m - 60 > 0:
            m -= 60
            h += 1
        ###############
        await ctx.send(f"долбаеб, {ctx.author.mention}, осталось {h} часов {m} минут {s} секунд")


bot.run(TOKEN)
