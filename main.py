import warnings
import math
import universal
import db

warnings.filterwarnings("ignore")


def get_sircles():
    radius = input('radius: ')
    if radius.isdigit():
        print('Площадь круга: ', math.pi * int(radius) ** 2)
        print('Длина окружности: ', math.pi * 2 * int(radius))
        print('Диаметр круга: ', 2 * int(radius))
        print('Радиус: ', radius)
        db.save_result('Площадь круга: ', math.pi * int(radius) ** 2)
        db.save_result('Длина окружности: ', math.pi * 2 * int(radius))
        db.save_result('Диаметр круга:  ', 2 * int(radius))
        db.save_result('Радиус: ', radius)
    return


def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Найти, результат сохранить в MySQL.
3. Сохранить все данные из MySQL в Excel.
4. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, get_sircles,
                            db.save_db_to_xlxs)
    return


if __name__ == '__main__':
    main()
