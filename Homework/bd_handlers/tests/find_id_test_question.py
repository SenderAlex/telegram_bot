
import asyncpg
import asyncio
from Homework.config.config import *


async def find_id_test_question(question_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT question_id FROM test WHERE question_id=$1''', question_id)
    all_records_question_id = [record['question_id'] for record in query]
    if len(all_records_question_id) != 0 and question_id == all_records_question_id[0]:
        print(f"Запись с question_id = {question_id} существует")
        return question_id
    else:
        print(f"Запись с question_id = {question_id} не существует")
        return False


# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(find_id_test_question(65)))


