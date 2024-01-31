
import asyncpg
import asyncio
from Homework.config.config import *

async def creat_subject_question(subject):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT question FROM test WHERE subject=$1''', subject)
    list_of_questions = [record['question'] for record in query]
    if len(list_of_questions) != 0:
        return list_of_questions


async def creat_subject_variants(subject):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT variant1, variant2, variant3 , variant4 FROM test WHERE subject=$1''', subject)
    variants = []
    for record in query:
        variant_list = [record['variant1'], record['variant2'], record['variant3'], record['variant4']]
        variants.append(variant_list)
    return variants


async def creat_subject_right_variant(subject):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT right_variant FROM test WHERE subject=$1''', subject)
    list_of_right_variant = [record['right_variant'] for record in query]
    if len(list_of_right_variant) != 0:
        return list_of_right_variant


async def creat_subject_point_quantity(subject):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT point_quantity FROM test WHERE subject=$1''', subject)
    list_of_point_quantity = [record['point_quantity'] for record in query]
    if len(list_of_point_quantity) != 0:
        return list_of_point_quantity



###########################################################################################################
async def creat_subject_test(subject):
    questions = await creat_subject_question(subject)
    variants = await creat_subject_variants(subject)
    right_answer = await creat_subject_right_variant(subject)
    point_quantity = await creat_subject_point_quantity(subject)

    combined_lists = []
    for i in range(len(questions)):
        combined_lists.append(questions[i])
        combined_lists.append(variants[i])
        combined_lists.append(right_answer[i])
        combined_lists.append(point_quantity[i])

    keys = ['question', 'answers', 'right_answer', 'point_quantity']
    list_of_quizlets = []
    while combined_lists:
        dict_items = {}
        for key in keys:
            if combined_lists:
                dict_items[key] = combined_lists.pop(0)  # структура стэка: элемент взял поместил в словарь и удалил из combined_lists
        list_of_quizlets.append(dict_items)
    return list_of_quizlets



#loop = asyncio.get_event_loop()
#print(loop.run_until_complete(creat_subject_question('математика')))
#print(loop.run_until_complete(creat_subject_variants('математика')))
#print(loop.run_until_complete(creat_subject_right_variant('математика')))
#print(loop.run_until_complete(creat_subject_point_quantity('математика')))
#print(loop.run_until_complete(creat_subject_test('математика')))
