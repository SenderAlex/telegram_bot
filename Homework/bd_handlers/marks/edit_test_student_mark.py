
import asyncpg
import asyncio
from Homework.config.config import *


async def edit_test_student_mark(subject, mark, test_student_id, mark_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''UPDATE test_student_mark SET subject=$1, mark=$2, test_student_id=$3, mark_id=$4''',
                       subject, mark, test_student_id, mark_id)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(edit_test_student_mark('программирование', 9,1, 1))