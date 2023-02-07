import view



def data_base():
    data_base = {} # общая база
    student_database = [] # база студентов
    base_lessons = []  # база предметов
    while True:
        team_number = view.input_data()
        print("выбран номер",team_number)
        print("общая база",data_base)
        if team_number == 1:
            lessons = view.number_1()
            
            if lessons not in base_lessons:
                base_lessons.append(lessons)
                for name in student_database:
                    data_base[name] [lessons] = []

        if team_number == 4:
            fi = view.number_4()
            if fi not in student_database:
                student_database.append(fi)
                # print('студенты ', student_database)
                data_base[fi] = {}
                for les in base_lessons:
                    data_base[fi][les] = {}

        if team_number == 2:
            temp_f, temp_l, temp_m = view.number_2()
            data_base[temp_f][temp_l].append(temp_m)
        
        if team_number == 3:
            print("Список учеников ", student_database)

        if team_number == 5:
            temp = view.number_5()
            print(data_base[temp])

        if team_number == 6:
            print("конец")
            break