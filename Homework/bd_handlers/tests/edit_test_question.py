
import asyncpg
import asyncio
from Homework.config.config import *


async def edit_test_question(subject, question, variant1, variant2, variant3, variant4, right_variant, point_quantity,
                             question_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''UPDATE test SET subject=$1, question=$2, variant1=$3, variant2=$4, variant3=$5, variant4=$6,
                        right_variant=$7, point_quantity=$8 WHERE question_id=$9''',
                       subject, question, variant1, variant2, variant3, variant4, right_variant, point_quantity,
                       question_id)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(edit_test_question('програм', 'Как?','Py', 'C',
#                                                'PHP', 'JS', 'Py', 1, 21))