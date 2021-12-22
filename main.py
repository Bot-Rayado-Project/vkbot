import config
import sheethandler
import random
import requests
from bs4 import BeautifulSoup
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
from vkwave.bots.utils.uploaders import PhotoUploader

bot = SimpleLongPollBot(tokens=config.TOKEN, group_id=config.GROUP_ID)

# OMG MANDARINA HI & THE ROCK

photo = None
gif = None

# Создание экземпляров клавиатуры

keyboardStart = Keyboard(one_time=False)
keyboardChooseGroup = Keyboard(one_time=False)
keyboardChooseDayOfWeek = Keyboard(one_time=False)

# Названия кнопок
start: list = ['Расписание', 'Анекдот', 'MI AMOR?', 'Помощь']
groups: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
                'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
daysofweek: list = ['понедельник', 'вторник',
                    'среда', 'четверг', 'пятница', 'суббота']
users: dict = {}
# Генерация кнопок
for i in range(len(start)):
    keyboardStart.add_text_button(start[i], ButtonColor.SECONDARY)
    if i == 0:
        keyboardStart.add_row()
for i in range(1, len(groups)+1):
    keyboardChooseGroup.add_text_button(
        groups[i-1].upper(), ButtonColor.SECONDARY)
    if i % 3 == 0:
        keyboardChooseGroup.add_row()
    if i == len(groups):
        keyboardChooseGroup.add_row()
        keyboardChooseGroup.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(1, len(daysofweek)+1):
    keyboardChooseDayOfWeek.add_text_button(
        daysofweek[i-1].capitalize(), ButtonColor.SECONDARY)
    if i % 3 == 0:
        keyboardChooseDayOfWeek.add_row()
    if i == len(daysofweek):
        keyboardChooseDayOfWeek.add_text_button('Меню', ButtonColor.PRIMARY)


@bot.message_handler(bot.text_filter(["привет", "начать", "начало", "старт", "меню"]))
async def greet(event: SimpleBotEvent) -> str:
    global keyboardStart, users
    users[event.from_id] = None
    await event.answer(message='omg mandarina hii!!!', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("mi amor?"))
async def roulette(event: SimpleBotEvent) -> str:
    global keyboardStart, users
    users[event.from_id] = None
    await event.answer(message='MI AMOR LA VINO!!! CASILLERO DEL DIABLO!!!!', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("помощь"))
async def roulette(event: SimpleBotEvent) -> str:
    global keyboardStart, users, photo
    users[event.from_id] = None
    if photo == None:
        photo = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://preview.redd.it/1azakjoq2k181.jpg?auto=webp&s=cc7d0fe98322bc63a556c92e218b19d2d9336408")
    await event.answer(message='omg mandarina hii\n@lamabot2000\n@crymother', keyboard=keyboardStart.get_keyboard(), attachment=photo)


@bot.message_handler(bot.text_filter("дима"))
async def roulette(event: SimpleBotEvent) -> str:
    global keyboardStart, users, gif
    users[event.from_id] = None
    if gif == None:
        gif = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681-1024x1024.jpg")
    await event.answer(message='?', keyboard=keyboardStart.get_keyboard(), attachment=gif)


@bot.message_handler(bot.text_filter("анекдот"))
async def get_joke(event: SimpleBotEvent) -> str:
    global keyboardStart
    url = 'https://baneks.ru/{}'.format(str(random.randint(1, 1142+1)))
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    msg = ((str(soup.p).replace("<p>", "")).replace(
        "</p>", "")).replace("<br/>", "")
    await event.answer(message=msg, keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("расписание"))
async def get_schedule(event: SimpleBotEvent) -> str:
    global keyboardChooseDayOfWeek, users
    if users.get(event.from_id) == None or users.get(event.from_id) == [False]:
        users[event.from_id] = [True]
        await event.answer(message='Выберите день недели', keyboard=keyboardChooseDayOfWeek.get_keyboard())


@bot.message_handler(bot.text_filter(daysofweek))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    global keyboardChooseDayOfWeek, users
    if users.get(event.from_id) == [True]:
        users[event.from_id] = [False, event.text]  # день недели
        print(users[event.from_id])
        await event.answer(message='Выберите группу.', keyboard=keyboardChooseGroup.get_keyboard())


@bot.message_handler(bot.text_filter(groups))
async def get_group(event: SimpleBotEvent) -> str:
    global keyboardChooseDayOfWeek, users
    if users.get(event.from_id)[0] == False:
        users[event.from_id] += [event.text]  # группа
        schedule = sheethandler.get_schedule(
            users[event.from_id][1].lower(), users[event.from_id][2].lower())
        await event.answer(message=schedule, keyboard=keyboardStart.get_keyboard())
        users[event.from_id] = None


bot.run_forever()
