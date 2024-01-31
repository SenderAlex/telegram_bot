
import asyncpg
import asyncio
from Homework.config.config import *


async def find_first_name_student(first_name): # это лишнее
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT first_name FROM test_student WHERE first_name=$1''', first_name)
    all_records_first_name = [record['first_name'] for record in query]
    if len(all_records_first_name) != 0 and first_name == all_records_first_name[0]:
        print(f"Запись с first_name = {first_name} существует")
        return first_name
    else:
        print(f"Запись с first_name = {first_name} не существует")
        return False


async def find_middle_name_student(middle_name): # это лишнее
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT middle_name FROM test_student WHERE middle_name=$1''', middle_name)
    all_records_middle_name = [record['middle_name'] for record in query]
    if len(all_records_middle_name) != 0 and middle_name == all_records_middle_name[0]:
        print(f"Запись с middle_name = {middle_name} существует")
        return middle_name
    else:
        print(f"Запись с middle_name = {middle_name} не существует")
        return False


async def find_last_name_student(last_name): # это лишнее
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT last_name FROM test_student WHERE last_name=$1''', last_name)
    all_records_last_name = [record['last_name'] for record in query]
    if len(all_records_last_name) != 0 and last_name == all_records_last_name[0]:
        print(f"Запись с last_name = {last_name} существует")
        return last_name
    else:
        print(f"Запись с last_name = {last_name} не существует")
        return False


async def find_phone_number_student(phone_number):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT phone_number FROM test_student WHERE phone_number=$1''', phone_number)
    all_records_phone_number = [record['phone_number'] for record in query]
    if len(all_records_phone_number) != 0 and phone_number == all_records_phone_number[0]:
        print(f"Запись с phone_number = {phone_number} существует")
        return phone_number
    else:
        print(f"Запись с phone_number = {phone_number} не существует")
        return False


async def find_user_id_student(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT user_id FROM test_student WHERE user_id=$1''', user_id)
    all_records_user_id = [record['user_id'] for record in query]
    if len(all_records_user_id) != 0 and user_id == all_records_user_id[0]:
        print(f"Запись с user_id = {user_id} существует")
        return user_id
    else:
        print(f"Запись с user_id = {user_id} не существует")
        return False


# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(find_first_name_student('Александр')))
# print(loop.run_until_complete(find_middle_name_student('Николаевич')))
# print(loop.run_until_complete(find_last_name_student('Сендер')))
# print(loop.run_until_complete(find_phone_number_student('375297938546')))
# print(loop.run_until_complete(find_user_id_student(943227920)))