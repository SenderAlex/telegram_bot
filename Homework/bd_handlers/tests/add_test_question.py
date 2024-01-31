
import asyncpg
import asyncio
from Homework.config.config import *


async def add_test_question(subject, question, variant1, variant2, variant3, variant4, right_variant, point_quantity):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO test (subject, question, variant1, variant2, variant3, variant4, right_variant,
                                            point_quantity) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)''',
                       subject, question, variant1, variant2, variant3, variant4, right_variant, point_quantity)
    await conn.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(add_test_question('програм', 'Как?','Py', 'C',
#                                                 'PHP', 'JS', 'Py', 1))