from datetime import datetime, timedelta
from calendar import month_name
from operator import length_hint
from geopy import distance
#from utils.terminal_codes import print_error
import math
import json
import locale
import random
INFO_CODE = "\033[38;5;255m[\033[38;5;40mINFO\033[38;5;255m]\033[0;0m     \033[38;5;254m{0}\033[0;0m"
WARNING_CODE = "\033[38;5;255m[\033[38;5;226mWARNING\033[38;5;255m]\033[0;0m  \033[38;5;254m{0}\033[0;0m"
ERROR_CODE = "\033[38;5;255m[\033[38;5;196mERROR\033[38;5;255m]\033[0;0m    \033[38;5;196m{0}\033[0;0m"


def print_info(string: str) -> None:
    print(INFO_CODE.format(string))


def print_warning(string: str) -> None:
    print(WARNING_CODE.format(string))


def print_error(string: str) -> None:
    print(ERROR_CODE.format(string))


def set_current_time() -> tuple | None:
    '''Задает параметры локализации на русский язык, создает объект времени time_obj и 2 строки времени на вывод:
     current_time (25 февр. 2022 г. 16:40:11), creation_time (2022-02-25T16:45:11.145Z)'''
    # Перевод названий месяцев на русский язык
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    try:
        # Текущее время по МСК (utc+3)
        time_obj = datetime.today().utcnow() + timedelta(hours=3)
        # Время в название (25 февр. 2022 г. 16:40:11)
        current_time = str(time_obj.day) + " " + month_name[time_obj.month][:4].lower() + ". " + time_obj.strftime("%Y г. %H:%M:%S")
        # Время создания (2022-02-25T16:45:11.145Z)
        creation_time = time_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        return time_obj, current_time, creation_time
    except:
        print_error("Ошибка в задании времени.")
        return None


def set_custom_time(time_str: str) -> tuple | None:
    '''Позволяет задать свое собстенное время начала в формате (26.03.2022 10:03:51)
     Задает параметры локализации на русский язык, создает объект времени time_obj и 2 строки времени на вывод:
     current_time (25 февр. 2022 г. 16:40:11), creation_time (2022-02-25T16:45:11.145Z)'''
    # Перевод названий месяцев на русский язык
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    try:
        # Объект заданного времени
        time_obj = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S") + timedelta(microseconds=random.randint(a=0, b=1000000))
        # Время в название (25 февр. 2022 г. 16:40:11)
        current_time = str(time_obj.day) + " " + month_name[time_obj.month][:4].lower() + ". " + time_obj.strftime("%Y г. %H:%M:%S")
        # Время создания (2022-02-25T16:45:11.145Z)
        creation_time = time_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        return time_obj, current_time, creation_time
    except:
        print_error("Ошибка в задании времени.")
        return None


def set_points(route_number: int) -> list | None:
    '''Парсит config.json на наличие маршрутов по индексу. Возвращает массив из точек'''
    with open("geobot/config.json", encoding='UTF-8') as json_data_file:
        data = json.load(json_data_file)
        try:
            return [[float(j[0]), float(j[1])] for j in [i.split(", ") for i in [j["coordinates"] for j in [data["routes"][i] for i in data["routes"]]][route_number]]]
        except IndexError:
            print_error("Ошибка в задании точек. Маршрут не найден.")
            return None
        except ValueError:
            print_error("Ошибка в задании точек. Неверно заданы координаты.")
            return None


def set_length(length: int, ignore: bool = False, offset: float = 10.0) -> float | None:
    '''Устанавливает длину в метрах. В случае, если переданный параметр меньше 10 - принимает за километры.
    Возвращает случайное значение float.'''
    try:
        length = int(length)
        if not ignore:
            if length < 10:
                print_warning(f"Длина маршрута задана как {length} м. Предположительно подразумевались километры. Перевод в метры. Передайте ignore=True для игнорирования предупреждения.")
                return random.uniform(length * 1000, length * 1000 + offset)
            return random.uniform(length, length + offset)
        else:
            return random.uniform(length, length + offset)
    except ValueError:
        print_error(f"Ошибка в задании длины. На вход дана строка - '{length}'")
        return None


def set_duration(duration: int, offset: int = 20000) -> int | None:
    '''Устанавливает протяженность маршрута в милисекундах (передавать в минутах). offset в милисекундах'''
    try:
        duration = int(duration)
        return duration * 60 * 1000 + random.randint(-offset, offset)
    except ValueError:
        print_error(f"Ошибка в задании протяженности маршрута. На вход дана строка - '{duration}'")
        return None


def set_average_speed(speed: float) -> float | None:
    '''Задает и переводит среднюю скорость из км/ч в м/с'''
    try:
        speed = float(speed)
        return speed/3.6
    except ValueError:
        print_error(f"Ошибка в задании средней скорости. На вход дана строка - '{speed}'")


def set_coordinates_shift(points: list, devider: int, avg_speed: float) -> tuple:
    distances = [distance.geodesic(points[i], points[i+1], ellipsoid='WGS-84').m for i in range(len(points)-1)]+[distance.geodesic(points[0], points[-1], ellipsoid='WGS-84').m]  # Расстояние между точками
    # За сколько секунд надо пройти отрезок distances со скоростью avg_speed
    timings = [float(i/avg_speed) for i in distances]
    counters = [[math.floor(i/devider), i % devider] for i in timings]
    return distances, timings, counters


def write_gpx(is_current_time: bool, route_number: int, length: int, duration: int, speed: float, time_str: str = None) -> None:
    '''Производит все основные расчеты и делает запись в файл .GPX.
    Является главной функцией модуля.'''
    start_time = datetime.now()
    time_tuple = set_current_time() if is_current_time else set_custom_time(time_str)
    points = set_points(int(route_number))
    length_ = set_length(int(length))
    duration_ = set_duration(int(duration))
    avg_speed = set_average_speed(float(speed))
    print(time_tuple, points, length_, duration_, avg_speed)
    print(datetime.now()-start_time)


if __name__ == "__main__":
    write_gpx(is_current_time=True, route_number=5, length=3000, duration=30, speed=6)
