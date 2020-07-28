from telebot import types
from frontend.enums import IntNames, RuNames
from frontend.user_data.requests_save import get_checked_dict

yes_no_markup = types.ReplyKeyboardMarkup()
button_yes = types.KeyboardButton("Yes")
button_no = types.KeyboardButton("No")
yes_no_markup.add(button_yes, button_no)

for_behind_markup = types.ReplyKeyboardMarkup()
button_for = types.KeyboardButton("Вперёд")
button_behind = types.KeyboardButton("Назад")
for_behind_markup.add(button_for, button_behind)

cancel_markup = types.ReplyKeyboardMarkup()
cancel_markup.add(types.KeyboardButton("Отмена"))
default_markup = types.ReplyKeyboardMarkup()


def get_keyboard_for_user(user_id: int):
    return_markup = types.ReplyKeyboardMarkup()
    dct = get_checked_dict(user_id)
    lst = [types.KeyboardButton(""), types.KeyboardButton(""), types.KeyboardButton("")]
    for i, name in enumerate(RuNames):
        if i == 0:
            continue

        lst[i % 3] = types.KeyboardButton(name.value + "✔" * int(dct[i]))

        if i % 3 == 0:
            return_markup.add(*lst)
            lst = [types.KeyboardButton(""), types.KeyboardButton(""), types.KeyboardButton("")]
    return_markup.add(*lst)
    return_markup.add(types.KeyboardButton("Отправить заявку"))
    return return_markup


educational_markup = types.ReplyKeyboardMarkup()
names = ["Учёная степень \\ MBA", "Несколько высших", "Среднее", "Среднее специальное", "Незаконченное высшее",
         "Высшее", "Ниже среднего", "Отмена", ""]
for i in range(len(names) // 3):
    button1 = types.KeyboardButton(names[i * 3])
    button2 = types.KeyboardButton(names[i * 3 + 1])
    button3 = types.KeyboardButton(names[i * 3 + 2])
    educational_markup.add(button1, button2, button3)

family_markup = types.ReplyKeyboardMarkup()
names = ["Женат \\ Замужем", "Холост \\ Не замужем", "Вдовец \\ Вдова", "Гражданский брак", "Разведён \\ Разведена",
         "Отмена"]
for i in range(len(names) // 3):
    button1 = types.KeyboardButton(names[i * 3])
    button2 = types.KeyboardButton(names[i * 3 + 1])
    button3 = types.KeyboardButton(names[i * 3 + 2])
    family_markup.add(button1, button2, button3)
