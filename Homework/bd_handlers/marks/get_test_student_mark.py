
import asyncpg
import asyncio
from Homework.config.config import *
import pandas as pd


async def get_test_student_first_name(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT first_name FROM test_student WHERE user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    data = []
    for record in records:
        data.append(record)
    first_name = data[0]
    await conn.close()
    return first_name


async def get_test_student_middle_name(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT middle_name FROM test_student WHERE user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    data = []
    for record in records:
        data.append(record)
    middle_name = data[0]
    await conn.close()
    return middle_name


async def get_test_student_last_name(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT last_name FROM test_student WHERE user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    data = []
    for record in records:
        data.append(record)
    last_name = data[0]
    await conn.close()
    return last_name


async def get_test_student_phone_number(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT phone_number FROM test_student WHERE user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    data = []
    for record in records:
        data.append(record)
    phone_number = data[0]
    await conn.close()
    return phone_number


async def get_test_student_subject(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT subject FROM test_student_mark INNER JOIN test_student ON
     test_student.tg_id = test_student_mark.test_student_id WHERE test_student.user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    subject_data = []
    for record in records:
        subject_data.append(record)
    await conn.close()
    return subject_data


async def get_test_student_mark(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    questions = await conn.fetch('''SELECT mark FROM test_student_mark INNER JOIN test_student ON
     test_student.tg_id = test_student_mark.test_student_id WHERE test_student.user_id = $1''', user_id)
    records = pd.DataFrame(questions)[0]
    mark_data = []
    for record in records:
        mark_data.append(record)
    await conn.close()
    return mark_data

async def get_student_data(user_id):
    subjects = await get_test_student_subject(user_id)
    marks = await get_test_student_mark(user_id)
    subject_mark_data = list(zip(subjects, marks))
    records = []
    for data in subject_mark_data:
        subject, mark = data
        record = f'{subject} -- {mark}'
        records.append(record)
    final_records = "\n".join(str(element) for element in records) # записать список без [] и каждый элемент с новой строки
    return final_records



#loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_test_student_first_name(943227920)))
# print(loop.run_until_complete(get_test_student_middle_name(943227920)))
# print(loop.run_until_complete(get_test_student_last_name(943227920)))
# print(loop.run_until_complete(get_test_student_phone_number(943227920)))
# print(loop.run_until_complete(get_test_student_subject(943227920)))
# print(loop.run_until_complete(get_test_student_mark(943227920)))
#print(loop.run_until_complete(get_student_data(943227920)))
