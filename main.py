import sheethandler
import os
import sqlite3
import aiohttp
import geobot
from datetime import datetime
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
from vkwave.bots.utils.uploaders import PhotoUploader, DocUploader

try:
    ALLOWED_USERS_IDS = (os.getenv('ALLOWED_USERS_IDS')).split()
    API_TOKEN = os.getenv('API_TOKEN')
    GROUP_ID = os.getenv('GROUP_ID')
    STATE = os.getenv('STATE')
except AttributeError:
    print(
        '\nTOKEN: None\nGROUP_ID: None\nEmpty value error.'
    )
    exit()

print("WARNING: DEVELOPMENT MODE") if STATE == "dev" else print()
try:
    bot = SimpleLongPollBot(tokens=API_TOKEN, group_id=GROUP_ID)
    print(
        f'\nTOKEN: {API_TOKEN}\nGROUP_ID: {GROUP_ID}\nSuccessfully connected to VK API!'
    )
    try:
        sqlite_connection = sqlite3.connect('users.db')
        cursor = sqlite_connection.cursor()
        print("\nБаза данных успешно подключена к SQLite")
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
        exit()
except:
    print('Internal error.')
    exit()

# Команды БД

sqlite_add_command = 'INSERT INTO users VALUES({0}, current_timestamp, "{1}");'
sqlite_select_command = "SELECT command, max(date), user_id FROM users GROUP BY user_id HAVING user_id={0};"
sqlite_select_all_commands = "SELECT command FROM users WHERE user_id={0} ORDER BY date DESC;"

# OMG MANDARINA HI & THE ROCK

commands: list = ["привет", "начать", "начало",
                  "старт", "меню", "mi amor?",
                  "помощь", "дима", "анекдот"]

# Создание экземпляров клавиатуры

keyboardStart = Keyboard(one_time=False)
keyboardChooseGroup = Keyboard(one_time=False)
keyboardChooseDayOfWeek = Keyboard(one_time=False)
keyboardChooseCurrentOrNextWeek = Keyboard(one_time=False)


# Названия кнопок
start: list = ['Расписание', 'Анекдот', 'MI AMOR?', 'Помощь']
groups: list = ['бфи2101', 'бфи2102', 'бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106',
                'бвт2107', 'бвт2108', 'бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
daysofweek: list = ['понедельник', 'вторник', 'среда',
                    'четверг', 'пятница', 'суббота', 'вся неделя']
currentornextweek: list = ['текущая неделя', 'следующая неделя']
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
        keyboardChooseDayOfWeek.add_row()
        keyboardChooseDayOfWeek.add_text_button('Меню', ButtonColor.PRIMARY)
for i in range(len(currentornextweek)):
    keyboardChooseCurrentOrNextWeek.add_text_button(
        currentornextweek[i].capitalize(), ButtonColor.SECONDARY)
    if i == len(currentornextweek)-1:
        keyboardChooseCurrentOrNextWeek.add_row()
        keyboardChooseCurrentOrNextWeek.add_text_button(
            'Меню', ButtonColor.PRIMARY)


async def sqlite_fetch(from_id: int, text: str, ret: bool = False) -> str:
    cursor.execute(sqlite_add_command.format(from_id, text))
    sqlite_connection.commit()
    if ret:
        cursor.execute(sqlite_select_all_commands.format(from_id))
        return cursor.fetchall()
    return


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@bot.message_handler(bot.text_filter(["привет", "начать", "начало", "старт", "меню"]))
async def greet(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    await event.answer(message='Выберите команду из списка.', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("mi amor?"))
async def miamor(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    if str(event.from_id) in ALLOWED_USERS_IDS:
        await event.answer(message='ACCESS GRANTED.', keyboard=keyboardStart.get_keyboard())
        await geobot.write_gpx(0, 5)
        gpx = await DocUploader(bot.api_context).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path="geobot/test.gpx", title=f"Route {datetime.now()}")
        await event.answer(message='Карта:', keyboard=keyboardStart.get_keyboard(), attachment=gpx)
    else:
        await event.answer(message='MI AMOR LA VINO!!! CASILLERO DEL DIABLO!!!!', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("помощь"))
async def help(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    photo_lamabot = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://sun9-83.userapi.com/impg/bVoWiYTwRgQ4ThlsaJNHMUKh_-nGIZM9IOID0Q/LVt87ogMi4g.jpg?size=591x556&quality=95&sign=30bf84a7dae605fb9ed4050a4c0e93dc&type=album")
    photo_crymother = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://sun9-63.userapi.com/impg/BpR7pnTl6CWAw0ud7ph8Qy1eZoWl0aD4qlJpgg/YLkSB-8Tib8.jpg?size=595x560&quality=95&sign=ecf377f818c46e7c8cf634fab5957d02&type=album")
    await event.answer(message='Помощи нет и не будет. \n@lamabot2000\n@crymother', keyboard=keyboardStart.get_keyboard(), attachment=[photo_lamabot, photo_crymother])


@bot.message_handler(bot.text_filter("дима"))
async def easteregg(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    gif = await PhotoUploader(bot.api_context).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link="https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681-1024x1024.jpg")
    await event.answer(message='?', keyboard=keyboardStart.get_keyboard(), attachment=gif)


@bot.message_handler(bot.text_filter("анекдот"))
async def get_joke(event: SimpleBotEvent) -> str:
    await sqlite_fetch(event.from_id, event.text)
    msg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
    await event.answer(message=msg, keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter("расписание"))
async def get_schedule(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if fetch[0][0].lower() not in commands:
        await event.answer(message='Выберите день недели.', keyboard=keyboardChooseDayOfWeek.get_keyboard())
    else:
        await event.answer(message='Выберите правильную команду.', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter(daysofweek))
async def get_day_of_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in daysofweek), fetch[1][0].lower() == 'расписание')):
        await event.answer(message='Выберите группу.', keyboard=keyboardChooseGroup.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана группа.', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter(groups))
async def get_group(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in groups), any(cmd.lower() in [fetch[1][0].lower()] for cmd in daysofweek), fetch[2][0].lower() == 'расписание')):
        await event.answer(message='Выберите неделю.', keyboard=keyboardChooseCurrentOrNextWeek.get_keyboard())
    else:
        await event.answer(message='Неверно выбрана что то.', keyboard=keyboardStart.get_keyboard())


@bot.message_handler(bot.text_filter(currentornextweek))
async def get_week(event: SimpleBotEvent) -> str:
    fetch = await sqlite_fetch(event.from_id, event.text, True)
    if all((any(cmd.lower() in [fetch[0][0].lower()] for cmd in currentornextweek), any(cmd.lower() in [fetch[1][0].lower()] for cmd in groups), any(cmd.lower() in [fetch[2][0].lower()] for cmd in daysofweek), fetch[3][0].lower() == 'расписание')):
        schedule = await sheethandler.print_schedule(fetch[2][0].lower(), fetch[1][0].lower(), fetch[0][0].lower())
        if fetch[2][0].lower() == 'вся неделя':
            for i in range(len(schedule)):
                await event.answer(message=schedule[i], keyboard=keyboardStart.get_keyboard())
        else:
            await event.answer(message=schedule, keyboard=keyboardStart.get_keyboard())


bot.run_forever()
