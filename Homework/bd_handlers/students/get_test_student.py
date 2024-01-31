
import asyncpg
import asyncio
from Homework.config.config import *


async def get_user_id_test_student(tg_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT user_id FROM test_student WHERE tg_id = $1''', tg_id)
    all_records_tg_id = [record['user_id'] for record in query]
    if len(all_records_tg_id) != 0:
        student_user_id = all_records_tg_id[0]
        return student_user_id


async def get_test_student_id(user_id: int):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT tg_id FROM test_student WHERE user_id = $1''', user_id)
    all_records_user_id = [record['tg_id'] for record in query]
    if len(all_records_user_id) != 0:
        student_id = all_records_user_id[0]
        return student_id


# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_user_id_test_student(6)))
# print(loop.run_until_complete(get_test_student_id(943227920)))