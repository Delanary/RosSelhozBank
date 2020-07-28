import sqlite3

try:
    conn = sqlite3.connect("./frontend/user_data/users.db")
except:
    conn = sqlite3.connect("users.db")
curs = conn.cursor()
curs.execute("""DROP TABLE IF EXISTS USERS""")
curs.execute(
    """CREATE TABLE IF NOT EXISTS USERS ( user_id INT PRIMARY KEY, SNLN text, birth_date TEXT, mobile_number TEXT, pass_num TEXT,
                                         email TEXT, credit_sum INT , credit_len INT, education INT, family INT,
                                         main_income INT, sub_income INT, periodic_consumption INT, family_income INT,
                                         job_experience INT )

    """)

conn.commit()
