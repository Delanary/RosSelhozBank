from bot import bot
from frontend.keyboards import get_keyboard_for_user
from logs.log import log_err


def cancel_check(function_to_cancel_check):
    """

    :param function_to_cancel_check:
    :return:
    """

    def wrapper(*args, **kwargs):
        try:
            text = args[0].text
            user_id = args[0].from_user.id
            if text != "Отмена":
                function_to_cancel_check(*args, **kwargs)
            else:
                bot.send_message(user_id, "Действие отменено", reply_markup=get_keyboard_for_user(user_id))
        except Exception as exc:
            log_err(exc)

    return wrapper
