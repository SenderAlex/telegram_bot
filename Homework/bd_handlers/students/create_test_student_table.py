
import asyncpg
import asyncio
from Homework.config.config import *


async def creat_test_student_table():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''
    CREATE TABLE IF NOT EXISTS test_student (
    tg_id serial PRIMARY KEY,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    user_id INTEGER
    )
    ''')
    await conn.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(creat_test_student_table())