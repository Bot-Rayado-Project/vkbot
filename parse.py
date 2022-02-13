import json
import os
import random


def get_points() -> list:
    os.system('cls||clear')
    try:
        with open("config.json", encoding='UTF-8') as json_data_file:
            data = json.load(json_data_file)
            cmd = str(input(
                "\033[37mВыбрать маршрут из существующих \033[33m{0}\033[37m или создать новый \033[31m{1}\033[37m\n".format("[Y]", "[N]")))
            os.system('cls||clear')
            if cmd.lower() == "y":
                routenames = [j["name"]
                              for j in [data["routes"][i] for i in data["routes"]]]
                routecoordinates = [j["coordinates"]
                                    for j in [data["routes"][i] for i in data["routes"]]]
                print("\033[37mВыберите маршрут из списка:")
                for i in range(len(routenames)):
                    print(str(i) + ". " + routenames[i])
                cmd = int(input())
                os.system('cls||clear')
                return [[float(j[0]), float(j[1])] for j in [i.split(", ") for i in routecoordinates[cmd]]]
            else:
                exit()
    except:
        print("Не найден / Не удается открыть JSON файл.")
        exit()


def get_duration() -> int:
    os.system('cls||clear')
    cmd = str(input(
        "\033[37mИспользовать значение по умолчанию (28-30 мин.) \033[33m{0}\033[37m или задать свое значение \033[31m{1}\033[37m\n".format("[Y]", "[N]")))
    os.system('cls||clear')
    if cmd.lower() == "y":
        return random.randint(1750000, 1800000)
    else:
        try:
            cmd = str(input(
                "\033[37mВведите свое значение времени в минутах, как показано в примере (28-30)\n")).split("-")
            os.system('cls||clear')
            return random.randint(int(cmd[0])*60*1000, int(cmd[1])*60*1000)
        except:
            print("Неверно введено время. Введите в формате (НАЧАЛО-КОНЕЦ) в минутах.\n")
            exit()


def get_length() -> float:
    os.system('cls||clear')
    cmd = str(input(
        "\033[37mИспользовать значение по умолчанию (3 км.) \033[33m{0}\033[37m или задать свое значение \033[31m{1}\033[37m\n".format("[Y]", "[N]")))
    os.system('cls||clear')
    if cmd.lower() == "y":
        return random.uniform(3000.0, 3020.0)
    else:
        try:
            cmd = int(input("\033[37mВведите свое значение в км.\n"))
            os.system('cls||clear')
            return random.uniform(cmd*1000.0, cmd*1000.0+20.0)
        except:
            print("Неверно введена дистанция.\n")
            exit()


if __name__ == '__main__':
    print(get_duration())
