import sqlite3

from flask import jsonify

from server.settings import DATABASE


def get_data_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'nickname': row[0],
                     'password': row[1],
                     'middle_name': row[2],
                     'surname': row[3],
                     'name': row[4],
                     'post': row[5],
                     'age': row[6],
                     'telegram': row[7],
                     'skill_level': row[8],
                     'experience': row[9],
                     'busy': row[10],
                     'team': row[11],
                     'completed_task': row[12]
                     }
                    for row in rows])


def get_data_hardware():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hardware")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': row[0],
                     'name': row[1],
                     'details': row[2],
                     'type': row[3],
                     'hard': row[4],
                     'country': row[5],
                     'year': row[6],
                     'repair': row[7],
                     }
                    for row in rows])


def get_data_repair_hardware():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM repair_hardware")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': row[0],
                     'nickname': row[1],
                     'start': row[2],
                     'end': row[3],
                     'comment_work': row[4],
                     'comment_applicant': row[5],
                     'id_hardware': row[6],
                     'done': row[7],
                     }
                    for row in rows])


def send_message():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    resp = cursor.execute(
        'SELECT users.telegram, users.nickname FROM repair_hardware INNER JOIN users ON users.nickname = repair_hardware.nickname WHERE repair_hardware.done = 0 and repair_hardware.notification = 0').fetchall()
    for i in resp:
        cursor.execute('update repair_hardware set notification = 1 where nickname = ?', (i[1],)).fetchall()
        conn.commit()
    return jsonify(resp)
