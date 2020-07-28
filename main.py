from backend.requests_to_backend import send_info_to_backend
from frontend.handling import *
from frontend.keyboards import for_behind_markup, cancel_markup, educational_markup, family_markup
from frontend.user_data.requests_save import *
from frontend.keyboards import get_keyboard_for_user
from frontend.wrappers import cancel_check
from frontend.enums import educational_choice, family_choice
from bot import bot


@bot.message_handler(commands=['start'])
def start(message):
    create_user(message.from_user.id)
    markup = get_keyboard_for_user(message.from_user.id)
    bot.send_message(message.from_user.id,
                     "Это бот для получения потребительских кредитов от РХБ, вам нужно заполнить все поля формы "
                     "перед тем, как её отправить\n"
                     "", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if "Мобильный телефон" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите свой мобильный телефон\n", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_mobile_number)
    if "ФИО" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите своё ФИО\n", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_name)
    if "Дата рождения" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите свою дату рождения\n", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_birth_date)
    if "Email" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите свой email\n", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_email)
    if "Сумма кредита" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите сумму, необходимую для кредитования\n", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_credit_sum)
    if "Основной доход" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, """ПОДТВЕРЖДЕННЫЕ ДОХОДЫ \n
(исходя из Ваших собственных расчетов за вычетом
налога) в рублях""", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_main_income)
    if "Образование" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Укажите своё образование\n", reply_markup=educational_markup)
        bot.register_next_step_handler(send, send_education)
    if "Семейное положение" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Укажите своё семейное положение\n", reply_markup=family_markup)
        bot.register_next_step_handler(send, send_family)
    if "Семейный доход" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, """ДОХОД СЕМЬИ
(средний доход семьи с учетом доходов супруги/
супруга, проживающей (его) совместно с Вами, в том
числе в гражданском браке)""", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_family_income)
    if "Второстепенный доход" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, """ДОПОЛНИТЕЛЬНЫЕ ДОХОДЫ
(доходы, не отраженные в предоставленных документах,
подтверждающих Ваше финансовое состояние. Например:
доход от сдачи в аренду недвижимости, дивиденды от ценных бумаг и т.п.) в рублях""", reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_sub_income)
    if "Периодические траты" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, """РАСХОДЫ, НОСЯЩИЕ
ПЕРИОДИЧЕСКИЙ ХАРАКТЕР\n
(выплачиваемые алименты, плата за образование,
арендные платежи, выплаты по исполнительным документам, страховые выплаты и т.п., а также Ваша доля
в общих расходах семьи по собственной оценке. В этом поле не указываются: налог на доходы физических
лиц, расходы на погашение долговых обязательств, расходы на проживание (питание, одежду и т.п.))""",
                                reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_periodic_consumption)
    if "Рабочий стаж" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите свой общий трудовой стаж за последние 5 лет в месяцах\n",
                                reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_job_experience)
    if "Номер паспорта" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите номер своего паспорта\n",
                                reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_pass_num)
    if "Срок кредитования" in message.text:
        user_id = message.from_user.id
        send = bot.send_message(user_id, "Введите ожидаемый срок кредитования\n",
                                reply_markup=cancel_markup)
        bot.register_next_step_handler(send, send_credit_len)

    if "Отправить заявку" in message.text:
        user_id = message.from_user.id
        send_info_to_backend()
        if not all(get_checked_dict(user_id).values()):
            bot.send_message(user_id, "Вы заполнили не всё, добейтесь появления галочек на всех иконках",
                             reply_markup=get_keyboard_for_user(message.from_user.id))
        else:
            bot.send_message(user_id,
                             "Бот сделал вид, что отправил заявку, он пока так не умеет, но может быть когда-нибудь сможет.",
                             reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_name(message):
    user_id = message.from_user.id
    try:
        name = handle_name(message.text)
        send = bot.send_message(user_id, f"Вы успешно ввели ФИО: {' '.join(name)}\n"
                                         f"Осталось ввести ", reply_markup=get_keyboard_for_user(message.from_user.id))
        set_name(user_id, *name)
    except ValueError as exc:
        pass


@cancel_check
def send_birth_date(message):
    birth_date = handle_birth_date(message.text)
    set_birth_date(message.from_user.id, birth_date)
    send = bot.send_message(message.from_user.id, f"Вы успешно ввели дату рождения: {birth_date}",
                            reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_mobile_number(message):
    user_id = message.from_user.id
    mobile_number = handle_mobile_number(message.text)
    set_mobile_number(user_id, mobile_number)
    send = bot.send_message(user_id, f"Вы успешно ввели мобильный телефон: {mobile_number}\n"
                                     f"Теперь нужно ввести электронную почту",
                            reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_email(message):
    user_id = message.from_user.id
    email = handle_email(message.text)
    set_email(user_id, email)
    send = bot.send_message(user_id, f"Вы успешно ввели электронную почту: {email}\n",
                            reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_pass_num(message):
    pass_num = handle_passport(message.text)
    set_pass_num(message.from_user.id, pass_num=pass_num)
    bot.send_message(message.from_user.id, f"Вы успешно ввели номер паспорта",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_credit_sum(message):
    user_id = message.from_user.id
    credit_sum = int(message.text)
    set_credit_sum(user_id, credit_sum=credit_sum)
    bot.send_message(message.from_user.id, f"Вы успешно ввели сумму кредита",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_credit_len(message):
    user_id = message.from_user.id
    credit_len = int(message.text)
    set_credit_len(user_id, credit_len=credit_len)
    bot.send_message(user_id, "Вы успешно ввели срок кредитования",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_education(message):
    user_id = message.from_user.id
    education = educational_choice[message.text]
    set_education(user_id, education=education)
    bot.send_message(user_id, "Вы успешно ввели ваше образование",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_family(message):
    user_id = message.from_user.id
    family = family_choice[message.text]
    set_family(user_id, family=family)
    bot.send_message(user_id, "Вы успешно ввели ваше семейное положение",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_main_income(message):
    user_id = message.from_user.id
    main_income = int(message.text)
    set_main_income(user_id, main_income=main_income)
    bot.send_message(user_id, "Вы успешно ввели ваш основной доход",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_sub_income(message):
    user_id = message.from_user.id
    sub_income = int(message.text)
    set_sub_income(user_id, sub_income=sub_income)
    bot.send_message(user_id, "Вы успешно ввели ваш второстепенный доход",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_periodic_consumption(message):
    user_id = message.from_user.id
    periodic_consumption = int(message.text)
    set_periodic_consumption(user_id, periodic_consumption=periodic_consumption)
    bot.send_message(user_id, "Вы успешно ввели ваши периодические расходы",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_family_income(message):
    user_id = message.from_user.id
    family_income = int(message.text)
    set_family_income(user_id, family_income=family_income)
    bot.send_message(user_id, "Вы успешно ввели ваш семейный доход",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


@cancel_check
def send_job_experience(message):
    user_id = message.from_user.id
    job_experience = int(message.text)
    set_job_experience(user_id, job_experience=job_experience)
    bot.send_message(user_id, "Вы успешно ввели ваш опыт работы",
                     reply_markup=get_keyboard_for_user(message.from_user.id))


bot.polling()
