
import asyncpg
import asyncio
from Homework.config.config import *


async def creat_test_table():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''
    CREATE TABLE IF NOT EXISTS test (
    question_id serial,
    subject TEXT,
    question TEXT,
    variant1 TEXT,
    variant2 TEXT,
    variant3 TEXT,
    variant4 TEXT,
    right_variant TEXT,
    point_quantity INTEGER
    )
    ''')
    await conn.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(creat_test_table())