
import asyncpg
import asyncio
from Homework.config.config import *


async def add_test_student(first_name, middle_name, last_name, phone_number, user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO test_student (first_name, middle_name, last_name, phone_number, user_id)
                       VALUES ($1, $2, $3, $4, $5)''', first_name, middle_name, last_name, phone_number, user_id)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(add_test_student('Людмила', 'Михайловна','Сендер',
#                                          '+375336190156', 943227921))