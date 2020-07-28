import sqlite3
from frontend.enums import IntNames

try:
    conn = sqlite3.connect("./frontend/user_data/users.db", check_same_thread=False)
except:
    conn = sqlite3.connect("users.db")
cur = conn.cursor()


def set_name(user_id: int, surname, first_name, last_name=None):
    snln = surname + first_name + str(last_name)
    cur.execute("UPDATE USERS SET SNLN = ? WHERE (user_id = ?)",
                (snln, user_id))
    conn.commit()


def get_flag(user_id: int):
    cur.execute("SELECT flags FROM TABLE USERS WHERE (user_id = ?)", (user_id,))


def set_flag(user_id: int, flag: int):
    cur.execute("UPDATE USERS SET (flags = ?) WHERE (user_id = ?)",
                (flag, user_id))
    conn.commit()


def set_email(user_id: int, email: str):
    cur.execute("UPDATE USERS SET email = ? WHERE (user_id = ?)",
                (email, user_id))
    conn.commit()


def set_mobile_number(user_id: int, mobile_number: str):
    cur.execute("UPDATE USERS SET mobile_number = ? WHERE (user_id = ?)",
                (mobile_number, user_id))
    conn.commit()


def set_birth_date(user_id: int, birth_date: str):
    cur.execute("UPDATE USERS SET birth_date = ? WHERE (user_id = ?)",
                (birth_date, user_id))
    conn.commit()


def set_credit_sum(user_id: int, credit_sum: int):
    cur.execute("UPDATE USERS SET credit_sum = ? WHERE (user_id = ?)",
                (credit_sum, user_id))
    conn.commit()

def set_pass_num(user_id: int, pass_num: int):
    cur.execute("UPDATE USERS SET pass_num = ? WHERE (user_id = ?)",
                (pass_num, user_id))
    conn.commit()



def set_credit_len(user_id: int, credit_len: int):
    cur.execute("UPDATE USERS SET credit_len = ? WHERE (user_id = ?)",
                (credit_len, user_id))
    conn.commit()


def set_education(user_id: int, education: int):
    cur.execute("UPDATE USERS SET education = ? WHERE (user_id = ?)",
                (education, user_id))
    conn.commit()


def set_family(user_id: int, family: int):
    cur.execute("UPDATE USERS SET family = ? WHERE (user_id = ?)",
                (family, user_id))
    conn.commit()


def set_main_income(user_id: int, main_income: int):
    cur.execute("UPDATE USERS SET main_income = ? WHERE (user_id = ?)",
                (main_income, user_id))
    conn.commit()


def set_sub_income(user_id: int, sub_income: int):
    cur.execute("UPDATE USERS SET sub_income = ? WHERE (user_id = ?)",
                (sub_income, user_id))
    conn.commit()


def set_periodic_consumption(user_id: int, periodic_consumption: int):
    cur.execute("UPDATE USERS SET periodic_consumption = ? WHERE (user_id = ?)",
                (periodic_consumption, user_id))
    conn.commit()


def set_family_income(user_id: int, family_income: int):
    cur.execute("UPDATE USERS SET family_income = ? WHERE (user_id = ?)",
                (family_income, user_id))
    conn.commit()


def set_job_experience(user_id: int, job_experience: int):
    cur.execute("UPDATE USERS SET job_experience = ? WHERE (user_id = ?)",
                (job_experience, user_id))
    conn.commit()


def is_user_in(user_id: int):
    cur.execute("SELECT user_id FROM USERS WHERE (user_id = ?)", (user_id,))
    return len(cur.fetchall()) >= 1


def create_user(user_id: int):
    if is_user_in(user_id):
        return
    cur.execute("INSERT INTO USERS(user_id) VALUES (?)",
                (user_id,))
    conn.commit()


def get_checked_dict(user_id: int):
    cur.execute("""SELECT * FROM USERS WHERE user_id = ?""", (user_id,))
    lst = list(cur.fetchall())
    dct = {i: bool(lst[0][i]) for i in range(len(lst[0]))}
    return dct
