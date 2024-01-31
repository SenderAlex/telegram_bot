
import asyncpg
import asyncio
from Homework.config.config import *


async def delete_test_question(question_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''DELETE FROM test WHERE question_id = $1''', question_id)
    print(f'Запись с id = {question_id} удалена!!!')
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(delete_test_question(21))
