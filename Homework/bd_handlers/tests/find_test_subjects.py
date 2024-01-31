#pip install sqlalchemy==2.0.23

import asyncpg
import asyncio
from Homework.config.config import *

async def find_subjects():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    query = await conn.fetch('''SELECT subject FROM test''')
    all_records_subjects = [record['subject'] for record in query]
    list_subjects = []
    if len(all_records_subjects) != 0:
        for all_records_subject in all_records_subjects:
            if all_records_subject in list_subjects:
                continue
            else:
                list_subjects.append(all_records_subject)
        return list_subjects


async def creat_subject_test_buttons():
    subjects = await find_subjects()
    keys = ['text', 'callback_data']
    list_of_buttons = [{key: subject for key in keys} for subject in subjects]
    return list_of_buttons


# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(find_subjects()))
# print(loop.run_until_complete(creat_subject_test_buttons()))
























#################################################################################################
# import asyncio
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker
# from aiogram import types
# import logging
# from aiogram import Router, F
# from Homework.keyboards import keyboard
# from Homework.config.config import *
#
#
# engine = create_engine(POSTGRES_URI)  # соединение с postgresql
# session = scoped_session(sessionmaker(bind=engine))  #создаёт сессию для работы с базой данных.
# Base = declarative_base()  # ???????
#
# class Test(Base):
#     __table__name = 'test'
#     question_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
#     subject = Column(String, nullable=True)
#     question = Column(String, nullable=True)
#     variant1 = Column(String, nullable=True)
#     variant2 = Column(String, nullable=True)
#     variant3 = Column(String, nullable=True)
#     variant4 = Column(String, nullable=True)
#     right_variant = Column(String, nullable=True)
#     point_quantity = Column(Integer, nullable=True)
#
#
#     def __init__(self, subject, question, variant1, variant2, variant3, variant4, right_variant, point_quantity):
#         self.subject = subject
#         self.question = question
#         self.variant1 = variant1
#         self.variant2 = variant2
#         self.variant3 = variant3
#         self.variant4 = variant4
#         self.right_variant = right_variant
#         self.point_quantity = point_quantity
#
#
#
# @router.message(F.text.lower() == 'btns')
# async def btns(message: types.Message):
#     tests = session.query(Test).all()
#     main = keyboard.main
#     for test in tests:
#         (types.InlineKeyboardButton(text=test.subject, url='https://google.com'))
#     await message.answer('hi', reply_markup=main.as_markup())
#
#
# async def main():
#     dp.include_routers(router)
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())




# select_all = await btns()
# print(select_all)

# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_test_question(2)))