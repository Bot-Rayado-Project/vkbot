<div align="center">
  <a href="https://github.com/3xiced/vkbot/">
    <img src="https://sun9-2.userapi.com/impf/rk2ygDyEHBqBLbBUPpWGRKfP4n-envluGtF3Vg/T5XaeQtts3E.jpg?size=1024x1024&quality=95&sign=f48c68a1368be545efd1e88ad36d4ca1&type=album" height="512">
  </a>
  <h1><a href="https://github.com/3xiced/vkbot">Bot Rayado</a> - Python</h1>
  <h3>Bot Rayado - Бот для ВКонтакте, написанный на Python</h3>
</div>

# Bot Rayado

Bot Rayado - это бот, созданный двумя разработчками, чтобы облегчить жизнь студентов МТУСИ.

Bot Rayado вдохновлен многими другими ботами и был создан благодаря энтузиазму разработчиков.

**Текущий мейнтейнер** проекта: [@darttusin](https://github.com/darttusin)
# Почему именно мы?

- Есть шаблоны для быстрого получения расписания
- Всегда новое расписание, полученное с сайта в момент запроса
- Большое количество потоков
- Быстрая работа бота
- Регулярные обновления

# Установка

## Холодный старт:

Клонируем репозиторий:
```
git clone https://github.com/3xiced/vkbot
```

Делаем билд image'a docker:
```
docker build -t vkbot /vkbot/
```

Запускаем контейнер с прокинутыми токеном, айди пользователей и айди группы:
```
docker run -e API_TOKEN='***' -e ALLOWED_USER_IDS='***' -e GROUP_ID='***' -e STATE='STABLE' -d --name vk_bot vkbot
```

## Перезапуск бота с обновлениями:

Для начала синхронизируем файлы через Rsync, затем копируем базу данных из текущего контейнера докер:
```
docker cp vk_bot:/vkbot/users.db /vkbot/users.db
```

Останавливаем контейнер, удаляем его и image:
```
docker container stop vk_bot && docker container rm vk_bot -f && docker image rm vkbot -f
```

Далее повторяем действия с холодного старта.

# Статус тестов

![Dev tests](https://github.com/3xiced/vkbot/actions/workflows/python-app-dev.yml/badge.svg)
![Main tests & deployment](https://github.com/3xiced/vkbot/actions/workflows/python-app-main.yml/badge.svg)
# Производительность

Bot Rayado не самый легковесный, но довольно оптимизированный бот.

# Сообщество

Bot rayado - очень молодой проект.

[Группа ВКонтакте](https://vk.com/botrayado)

# Разработчики

[Александр Разумов](https://vk.com/lamabot2000)

[Иван Чепиков](https://vk.com/crymother)
