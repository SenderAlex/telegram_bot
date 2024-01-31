
import asyncpg
import asyncio
from Homework.config.config import *


async def edit_test_student(first_name, middle_name, last_name, phone_number, user_id, tg_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''UPDATE test_student SET first_name=$1, middle_name=$2, last_name=$3, phone_number=$4,
                       user_id=$5 WHERE tg_id=$6''', first_name, middle_name, last_name, phone_number, user_id, tg_id)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(edit_test_student('Александр', 'Николаевич', 'Сендер',
#                                           '+375297938546', 943227920, 1))