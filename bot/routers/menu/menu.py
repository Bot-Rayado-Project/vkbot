from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter, CommandsFilter
from bot.keyboards import create_menu_kb
from bot.utils import personal_request as pr
from bot.utils import post_request
from bot.constants import RESTIP, RESTPORT
from bot.logger import get_logger
from bot.utils import headman_request as hr
from bot.utils import EditHeadmanRequest
from vkwave.bots import Keyboard, ButtonColor
import random
import json

logger = get_logger(__name__)

menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, PayloadFilter({"button": "menu"}))
async def menu(event: SimpleBotEvent) -> None:
    '''Обработчик кнопки "Меню" по пейлоаду'''
    await event.answer(message='Выберите необходимую вам кнопку на клавиатуре', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(("старт", "start", "/start", "начало")))
async def menu(event: SimpleBotEvent) -> None:
    '''Обработчик начала взаимодействия с ботом'''
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку' +
                       'слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +
                       ' - Всегда новое расписание, полученное с сайта\n - Все потоки 1 курса\n - Редактор расписания для себя и группы\n ' +
                       ' - Быстрая работа бота\n - Регулярные обновления', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())


@simple_bot_message_handler(menu_router, CommandsFilter(("shuffle")))
async def shuffle(event: SimpleBotEvent) -> None:
    '''Обработчик - получает список пользователей в чате и перемешивает их.'''
    users_list = []
    chat_users = (await event.api_ctx.messages.get_conversation_members(peer_id=event.object.object.dict().get("message").get("peer_id"))).response.dict().get("items")
    chat_users_ids = [_user_id for _user_id in [user_id.get(
        "member_id") for user_id in chat_users] if _user_id > 0]
    for user_id in chat_users_ids:
        user_data = (await event.api_ctx.users.get(user_ids=[user_id])).response[0]
        users_list += ["@id" + str(user_id) + " " +
                       user_data.first_name + " " + user_data.last_name]
    random.shuffle(users_list)
    for i in range(len(users_list)):
        users_list[i] = str((i + 1)) + ". " + users_list[i] + "\n"
    print(event.text)
    event_name = event.text.replace("/shuffle", "")
    if event_name != "":
        await event.answer(message=event_name + "\n" + ' '.join(users_list))
    else:
        await event.answer(message=' '.join(users_list))


@simple_bot_message_handler(menu_router)
async def menu(event: SimpleBotEvent) -> None:
    '''Обработчик всех остальных команд посылаемых пользователем.
       В случае, если до этого было взаимодействие с редактором расписания, совершит необходимые действия
       для изменения расписания (post, get запросы к REST сервису для записи/считывания изменений).'''
    if (pr.edit_personal_requests.get(event.from_id) == None or hr.edit_headman_requests.get(event.from_id) == None):
        if int(event.object.object.dict().get("message").get("id")) != 0:
            await event.answer(message='Выберите необходимую вам кнопку на клавиатуре', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
    else:
        if pr.edit_personal_requests[event.from_id].writing_changes_or_annotation == True:
            # Записываем изменения
            if pr.edit_personal_requests[event.from_id].pair_number != 0:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/change-schedule-personal/',
                    data={
                        'stream_group': pr.edit_personal_requests[event.from_id].stream_group,
                        'day': pr.edit_personal_requests[event.from_id].day,
                        'parity': pr.edit_personal_requests[event.from_id].parity,
                        'pair_number': pr.edit_personal_requests[event.from_id].pair_number,
                        'changes': event.text,
                        'id': event.from_id
                    }
                )
                logger.info(response)
                try:
                    json.loads(response)['ok']
                except Exception:
                    logger.error(
                        'Ошибка при запросе к rest сервису на сброс всего дня.')
                    await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение персональной пары.')
                    await event.answer(message='Ошибка при изменении персональной пары. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                else:
                    await event.answer(message='Пара успешно изменена', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
            else:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/add-annotation-personal/',
                    data={
                        'stream_group': pr.edit_personal_requests[event.from_id].stream_group,
                        'day': pr.edit_personal_requests[event.from_id].day,
                        'parity': pr.edit_personal_requests[event.from_id].parity,
                        'id': event.from_id,
                        'annotation': event.text
                    }
                )
                logger.info(response)
                try:
                    json.loads(response)['ok']
                except Exception:
                    logger.error(
                        'Ошибка при запросе к rest сервису на сброс всего дня.')
                    await event.answer(message='Ошибка при сбросе персонального дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение персональной аннотации.')
                    await event.answer(message='Ошибка при изменении персональной аннотации. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                else:
                    await event.answer(message='Аннотация успешно изменена', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
            logger.info(
                f'{event.from_id}: {event.text} - {pr.edit_personal_requests[event.from_id]}')
        elif hr.edit_headman_requests[event.from_id].writing_changes_or_annotation == True:
            # Записываем изменения
            if hr.edit_headman_requests[event.from_id].pair_number != 0:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/change-schedule-headman/',
                    data={
                        'stream_group': hr.edit_headman_requests[event.from_id].stream_group,
                        'day': hr.edit_headman_requests[event.from_id].day,
                        'parity': hr.edit_headman_requests[event.from_id].parity,
                        'pair_number': hr.edit_headman_requests[event.from_id].pair_number,
                        'changes': event.text
                    }
                )
                logger.info(response)
                try:
                    json.loads(response)['ok']
                except Exception:
                    logger.error(
                        'Ошибка при запросе к rest сервису на сброс всего дня.')
                    await event.answer(message='Ошибка при сбросе дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение пары.')
                    await event.answer(message='Ошибка при изменении пары. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                else:
                    await event.answer(message='Пара успешно изменена', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
            else:
                response = await post_request(
                    url=f'http://{RESTIP}:{RESTPORT}/add-annotation-headman/',
                    data={
                        'stream_group': hr.edit_headman_requests[event.from_id].stream_group,
                        'day': hr.edit_headman_requests[event.from_id].day,
                        'parity': hr.edit_headman_requests[event.from_id].parity,
                        'annotation': event.text
                    }
                )
                logger.info(response)
                try:
                    json.loads(response)['ok']
                except Exception:
                    logger.error(
                        'Ошибка при запросе к rest сервису на сброс всего дня.')
                    await event.answer(message='Ошибка при сбросе  дня. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                if json.loads(response)['ok'] != True:
                    logger.error(
                        'Ошибка при запросе к rest сервису на изменение аннотации.')
                    await event.answer(message='Ошибка при изменении аннотации. Информация об ошибке направлена разработчикам', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
                else:
                    await event.answer(message='Аннотация успешно изменена', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
            logger.info(
                f'{event.from_id}: {event.text} - {hr.edit_headman_requests[event.from_id]}')
        else:
            await event.answer(message='Выберите необходимую вам кнопку на клавиатуре', keyboard=(await create_menu_kb(event.from_id)).get_keyboard())
