from enum import IntEnum, auto, Enum


class IntNames(IntEnum):
    user_id = 0
    snln = 1
    birth_date = 4
    mobile_number = 5
    email = 6
    credit_sum = 7
    credit_len = 8
    education = 10
    family = 11
    main_income = 12
    sub_income = 13
    periodic_consumption = 14
    family_income = 15
    job_experience = 16


class RuNames(Enum):
    user_id = "Номер юзера"
    snln = "ФИО"
    birth_date = "Дата рождения"
    mobile_number = "Мобильный телефон"
    pass_num = "Номер паспорта"
    email = "Email"
    credit_sum = "Сумма кредита"
    credit_len = "Срок кредитования"
    education = "Образование"
    family = "Семейное положение"
    main_income = "Основной доход"
    sub_income = "Второстепенный доход"
    periodic_consumption = "Периодические траты"
    family_income = "Семейный доход"
    job_experience = "Рабочий стаж"


names = ["Учёная степень \\ MBA", "Несколько высших", "Среднее", "Среднее специальное", "Незаконченное высшее",
         "Высшее", "Ниже среднего", "Отмена", ""]
educational_choice = {names[i]: i for i in range(len(names))}

names = ["Женат \\ Замужем", "Холост \\ Не замужем", "Вдовец \\ Вдова", "Гражданский брак", "Разведён \\ Разведена"]
family_choice = {names[i]: i for i in range(len(names))}
