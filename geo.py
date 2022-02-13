import random
import math
import json
# import asyncio
from geopy import distance
from datetime import datetime, timedelta


async def set_time() -> tuple:
    # Задание времени
    currenttime = datetime.today().strftime("%d февр. %Y г. %H:%M:%S").replace("0", "", 1) if datetime.today().strftime(
        "%d февр. %Y г. %H:%M:%S")[0] == "0" else datetime.today().strftime("%d февр. %Y г. %H:%M:%S")  # Название файла
    starttime = datetime.utcnow().strftime(
        "%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"  # Время создания
    start_time = datetime.utcnow()
    return currenttime, starttime, start_time


async def get_route_points_length_duration() -> list:
    with open("config.json", encoding='UTF-8') as json_data_file:
        data = json.load(json_data_file)
        routecoordinates = [j["coordinates"]
                            for j in [data["routes"][i] for i in data["routes"]]]
        # Вместо 0 номер маршрута -----------------------------------------------------------v
        points = [[float(j[0]), float(j[1])]
                  for j in [i.split(", ") for i in routecoordinates[1]]]
        length = random.uniform(3000.0, 3020.0)
        duration = random.randint(1750000, 1800000)
        return points, length, duration


async def set_coordinates_shift(points: list, devider: int) -> tuple:
    # Считывание с файла координат, расчет расстояния м/д точками, средняя сокрость, тайминги и сдвиг в координатах
    distances = [distance.geodesic(points[i], points[i+1], ellipsoid='WGS-84').m for i in range(len(points)-1)]+[
        distance.geodesic(points[0], points[-1], ellipsoid='WGS-84').m]  # Расстояние между точками
    avgspeed = 5.8/float(3.6)  # Средняя скорость в м/с
    timings = [float(i/avgspeed) for i in distances]
    counters = [math.floor(i/devider) for i in timings]
    for i in range(len(counters)):
        if counters[i] == 0:
            counters[i] = 1
    coordshift = [[(points[i+1][0]-points[i][0])/counters[i], (points[i+1][1]-points[i][1])/counters[i]]
                  for i in range(len(points)-1)]+[[(points[0][0]-points[-1][0])/counters[1], (points[0][1]-points[-1][1])/counters[1]]]
    return distances, counters, coordshift


async def set_blueprints() -> tuple:
    # Blueprints
    with open("blueprint", "r", encoding="UTF-8") as tracing:
        entrypoint = tracing.read(1200)  # MAIN1
        movement = tracing.read(209)  # MAIN2
        closingbracket = tracing.read(29)  # MAIN3
        return entrypoint, movement, closingbracket


async def write_gpx(finaldistance: int, devider: int) -> None:
    # 0 - entrypoint #1 - movement #2 - closingbracket
    entrypoint, movement, closingbracket = await set_blueprints()
    # 0 - currenttime #1 - starttime #2 - starttimeoutput #3 - start_time
    currenttime, starttime, start_time = await set_time()
    # 0 - points #1 - length #2 - duration
    points, length, duration = await get_route_points_length_duration()
    # Сдвиг координат
    distances, counters, coordshift = await set_coordinates_shift(points=points, devider=devider)
    with open("test.gpx", "w+", encoding="UTF-8") as output:
        output.write(entrypoint.format(
            currenttime, starttime, length, duration))
        # Главный цикл
        lat, lon = points[0][0], points[0][1]
        latestpoint = [lat, lon]
        israndom = False
        gap1x, gap1y = -0.00002, 0.00002
        gap2x, gap2y = -0.00002, 0.00002
        height = random.randint(155, 165+1)
        while finaldistance < length:  # Цикл проверки длины
            for k in range(len(distances)):  # Внешний цикл на вход в линию
                lat = points[k][0] + random.uniform(gap2x, gap2y)
                lon = points[k][1] + random.uniform(gap2x, gap2y)
                for j in range(counters[k]):  # Обработка линии
                    lat += coordshift[k][0]  # Сдвиг к следующей точке
                    lon += coordshift[k][1]
                    if j % 19 == 0:
                        height = random.randint(155, 165+1)
                    finaldistance += distance.geodesic([lat, lon],
                                                       latestpoint, ellipsoid='WGS-84').m
                    if finaldistance >= length:
                        break
                    # Величины c и s
                    c, s = float('{:.2f}'.format(random.uniform(1.0, 360.0))), float(
                        '{:.2f}'.format(random.uniform(1.0, 360.0)))
                    if israndom:
                        deltalat = random.uniform(gap1x, gap1y)
                        deltalon = random.uniform(gap1x, gap1y)
                        latestpoint = [lat+deltalat, lon+deltalon]
                        output.write(movement.format(
                            latestpoint[0],
                            latestpoint[1],
                            height,
                            start_time.strftime("%Y-%m-%dT%H:%M:%S")+"Z", c, s))
                        israndom = False
                    else:
                        if j % random.randint(1, 9 + 1) == 0:
                            israndom = True
                            deltalat = random.uniform(gap1x, gap1y)
                            deltalon = random.uniform(gap1x, gap1y)
                            latr = lat + deltalat
                            lonr = lon + deltalon
                            latestpoint = [latr, lonr]
                            output.write(movement.format(
                                latr,
                                lonr,
                                height,
                                start_time.strftime("%Y-%m-%dT%H:%M:%S")+"Z", c, s))
                        else:
                            latestpoint = [lat, lon]
                            output.write(movement.format(
                                lat,
                                lon,
                                height,
                                start_time.strftime("%Y-%m-%dT%H:%M:%S")+"Z", c, s))
                    start_time += timedelta(seconds=devider)
        output.write(closingbracket)
        print('Генерация завершена.')


# async def main() -> None:
#     await write_gpx(finaldistance=0, devider=5)

# asyncio.run(main())
