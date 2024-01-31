
import asyncpg
import asyncio
from Homework.config.config import *


async def delete_test_student(tg_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''DELETE FROM test_student WHERE tg_id = $1''', tg_id)
    print(f'Запись с id = {tg_id} удалена!!!')
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(delete_test_student(6))