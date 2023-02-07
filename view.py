def input_data():
    temp = int(input("Выберете пункт:\n 1 - Добавить предмет;\n 2 - Добавить оценку;\n 3 - Показать список учеников;\n 4 - Добавить ученика;\n 5 - Оценки ученика;\n 6 - Выход\n №: "))
    return temp

def number_1():
    temp = input("Добавить предмет: ")
    # print("bobavili - ",temp)
    return temp

def number_4():
    temp = str(input("Введите Фамилию и Имя\n ФИ: "))
    return temp

def number_2():
    temp_f = input("Введите ФИ ученика: ")
    temp_l = input("Введите предмет: ")
    temp_m = input("Введите оценку: ")
    return temp_f, temp_l, temp_m

def number_5():
    temp = input("Введите Фамилию и Имя для просмотра оцецнок\n ФИ: ")
    return temp
