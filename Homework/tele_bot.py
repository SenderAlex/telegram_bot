# https://t.me/exam_test23_bot

import asyncio
from aiogram import F
from aiogram import types
from aiogram.filters import StateFilter, Command
from aiogram.types import InputFile, Message
from Homework.config.config import *
from Homework.keyboards.keyboard import generate_student_markup, generate_admin_markup, admin_menu
from Homework.handlers.questions import add_question, edit_question, delete_question
from Homework.bd_handlers.tests.find_test_subjects import find_subjects
from Homework.quiz import viktorina


@router.message(Command(commands=['start']))  # [2]
async def command_start(message: Message):
    if message.from_user.id == admin:
        admin_mark_up = await generate_admin_markup(await find_subjects(), 1)
        await message.answer(text=f'Здравствуйте, {message.from_user.first_name}!!! Вы зашли в систему как администратор',
                             reply_markup=admin_mark_up.as_markup())
    else:
        student_mark_up = await generate_student_markup(await find_subjects(), 1)
        await message.answer(
            text=f'Здравствуйте, {message.from_user.first_name}!!! Вы зашли в систему как студент!! Выберите одной из '
                 f'вариантов, предложенных ниже тестов', reply_markup=student_mark_up.as_markup())


@dp.callback_query(F.data == "admin")
async def command_admin(callback: types.CallbackQuery):
    if callback.from_user.id == admin:
        await callback.message.answer(text=f'{callback.from_user.first_name}, теперь вы можете'
                                           f' добавлять/редактировать/удалять вопросы кнопками, указанными ниже 👇',
                                      reply_markup=admin_menu.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "cancel_admin_menu")
async def send_random_value(callback: types.CallbackQuery):
    if callback.from_user.id == admin:
        admin_mark_up = await generate_admin_markup(await find_subjects(), 1)
        await callback.message.answer(text=f'{callback.from_user.first_name}, Вы отменили свое действия и возвращаетесь'
                                           f' в главное меню', reply_markup=admin_mark_up.as_markup())
    await callback.answer()


async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
