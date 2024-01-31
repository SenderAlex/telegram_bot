
import asyncpg
import asyncio
from Homework.config.config import *


async def creat_test_student_mark_table():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''
    CREATE TABLE IF NOT EXISTS test_student_mark (
    mark_id serial PRIMARY KEY,
    subject TEXT,
    mark INTEGER,
    test_student_id INTEGER REFERENCES test_student(tg_id)
    )
    ''')
    await conn.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(creat_test_student_mark_table())