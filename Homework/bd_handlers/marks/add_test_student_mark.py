
import asyncpg
import asyncio
from Homework.config.config import *


async def add_test_student_mark(subject, mark, test_student_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO test_student_mark (subject, mark, test_student_id)
                       VALUES ($1, $2, $3)''', subject, mark, test_student_id)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(add_test_student_mark('математика', 10,1))