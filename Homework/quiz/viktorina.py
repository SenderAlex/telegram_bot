
import os
from aiogram import types
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from Homework.config.config import *
from Homework.bd_handlers.students.add_test_student import add_test_student
from Homework.keyboards import keyboard
from Homework.bd_handlers.tests.find_test_subjects import find_subjects
from Homework.bd_handlers.tests.create_subject_test import creat_subject_test
from Homework.bd_handlers.students.get_test_student import get_user_id_test_student
from Homework.bd_handlers.students.find_record_test_student import (find_phone_number_student, find_user_id_student)
from Homework.bd_handlers.students.get_test_student import get_test_student_id
from Homework.bd_handlers.marks.add_test_student_mark import add_test_student_mark
from Homework.config.morphologia_numeral import get_correct_expression
from Homework.bd_handlers.marks.get_test_student_mark import (get_test_student_first_name, get_test_student_middle_name,
get_test_student_last_name, get_test_student_phone_number, get_student_data)



class AddContactData(StatesGroup):
    first_name = State()
    middle_name = State()
    last_name = State()
    phone_number = State()

scores = {}
question_number = {}
subject = ''


@router.callback_query(F.data.startswith('register'))
async def register_of_users(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data.split(' ')[1]
    global subject
    subject = data
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    if user_id != await find_user_id_student(user_id):
        await bot.answer_callback_query(callback_query.id, 'Регистрация тестируемого')
        await callback_query.message.answer(text=f'Напишите своё Имя')
        await state.set_state(AddContactData.first_name)
    else:
        await bot.send_message(user_id, '<b>Вы уже зарегистрированы</b>')
        scores[callback_query.message.chat.id] = 0
        question_number[callback_query.message.chat.id] = 0
        await bot.send_message(callback_query.message.chat.id, text='Добро пожаловать на тестирование! Ответьте на'
                                                                    ' следующие вопросы')
        await start_quiz(chat_id)


@router.message(AddContactData.first_name, F.text.isalpha())
async def add_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(AddContactData.middle_name)
    await message.answer('Напишите свое Отчество')


@router.message(AddContactData.first_name)
async def add_first_name(message: types.Message, state: FSMContext):
    await message.answer('Имя должно содержать только буквы. Введите Имя ещё раз')
    await state.set_state(AddContactData.first_name)



@router.message(AddContactData.middle_name, F.text.isalpha())
async def add_middle_name(message: types.Message, state: FSMContext):
    await state.update_data(middle_name=message.text)
    await state.set_state(AddContactData.last_name)
    await message.answer('Напишите свою Фамилию')


@router.message(AddContactData.middle_name)
async def add_first_name(message: types.Message, state: FSMContext):
    await message.answer('Отчество должно содержать только буквы. Введите Отчество ещё раз')
    await state.set_state(AddContactData.middle_name)


@router.message(AddContactData.last_name, F.text.isalpha())
async def add_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(AddContactData.phone_number)
    await message.answer('Напишите свой номер телефона в международном формате без знака +')


@router.message(AddContactData.last_name)
async def add_first_name(message: types.Message, state: FSMContext):
    await message.answer('Фамилия должна содержать только буквы. Введите Имя ещё раз')
    await state.set_state(AddContactData.last_name)


@router.message(AddContactData.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    data = await state.update_data(phone_number=message.text)
    if data['phone_number'].isdigit():
        await state.clear()
        await state.get_data()
        first_name = data["first_name"]
        middle_name = data["middle_name"]
        last_name = data["last_name"]
        phone_number = data["phone_number"]
        user_id = message.from_user.id
        if (phone_number != await find_phone_number_student(phone_number)):
            await add_test_student(first_name, middle_name, last_name, phone_number, user_id)
            student_mark_up = await keyboard.generate_student_markup(await find_subjects(), 1)
            await message.answer('Контактные данные успешно сохранены', reply_markup=student_mark_up.as_markup())
        else:
            student_mark_up = await keyboard.generate_student_markup(await find_subjects(), 1)
            await message.answer('Вы уже зарегистрированы', reply_markup=student_mark_up.as_markup())
    else:
        await message.answer('Вы не верно ввели номер телефона. Номер телефона нужно ввести цифрами')
        await state.set_state(AddContactData.phone_number)

async def start_quiz(chat_id: int):
    questions = await creat_subject_test(subject) #!!!!
    current_question_number = question_number[chat_id]
    if current_question_number >= len(questions):
        await show_score(chat_id, len(questions))
        return
    question = questions[current_question_number]['question']
    answers = questions[current_question_number]['answers']
    quiz_mark_up = await keyboard.generate_quiz_markup(answers, 1)
    await bot.send_message(chat_id=chat_id, text=question, reply_markup=quiz_mark_up.as_markup())


@router.callback_query(F.data.startswith('quiz'))
async def check_user_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    current_question_number = question_number[chat_id]
    user_answer = callback_query.data.split()[2]
    questions = await creat_subject_test(subject) #!!!!
    right_answer = questions[current_question_number]['right_answer']
    point_quantity = questions[current_question_number]['point_quantity']
    if user_answer == right_answer:
        scores[chat_id] += point_quantity
        await bot.answer_callback_query(callback_query.id, text=f'Вы верно ответили на вопрос. Вы набрали уже '
                    f'{get_correct_expression(scores[chat_id], "балл")}', show_alert=False)
    else:
        scores[chat_id] += 0
        await bot.answer_callback_query(callback_query.id, text=f'Вы неверно ответили на вопрос. На данный момент у Вас'
            f' только {get_correct_expression(scores[chat_id], "балл")}', show_alert=False)
    question_number[chat_id] += 1
    await start_quiz(chat_id)


async def show_score(chat_id: int, total_questions: int):
    score = scores[chat_id]
    await bot.send_message(chat_id, f'Тест завершен. Количество верных ответов: <b>{score}</b> из <b>{total_questions}</b>')
    if chat_id != admin:
        if 8 <= score <= 10:
            await bot.send_photo(chat_id=chat_id,
                                 photo='https://ss.sport-express.ru/userfiles/materials/184/1849317/volga.jpg')
            await add_test_student_mark(subject, score, await get_test_student_id(chat_id))  # не всегда chad_id совпадает с user_id!!
            await bot.send_message(chat_id, f"Ваше Имя -- <b>{await get_test_student_first_name(chat_id)}</b>\n"
                                            f"Ваше Отчество -- <b>{await get_test_student_middle_name(chat_id)}</b>\n"
                                            f"Ваша Фамилия -- <b>{await get_test_student_last_name(chat_id)}</b>\n"
                                            f"Ваш номер телефона -- <b>{await get_test_student_phone_number(chat_id)}</b>\n"
                                            f"Ваши данные по пройденным тестам \n<b>{await get_student_data(chat_id)}</b>")
            student_mark_up = await keyboard.generate_student_markup(await find_subjects(), 1)
            await bot.send_message(chat_id, text=f'Вы просто НОМЕР ОДИН во всём!!!!')
            await bot.send_message(chat_id, text=f'Ваши результаты тестирования успешно сохранены',
                                   reply_markup=student_mark_up.as_markup())

        elif 4 <= score <= 7:
            await bot.send_photo(chat_id=chat_id,
                                 photo='https://cdn.segodnya.ua/i/image_728x410/media/image/61e/866/bda/61e866bda35db.jpg.webp')
            await add_test_student_mark(subject, score,
                                        await get_test_student_id(chat_id))  # не всегда chad_id совпадает с user_id!!
            await bot.send_message(chat_id, f"Ваше Имя -- <b>{await get_test_student_first_name(chat_id)}</b>\n"
                                            f"Ваше Отчество -- <b>{await get_test_student_middle_name(chat_id)}</b>\n"
                                            f"Ваша Фамилия -- <b>{await get_test_student_last_name(chat_id)}</b>\n"
                                            f"Ваш номер телефона -- <b>{await get_test_student_phone_number(chat_id)}</b>\n"
                                            f"Ваши данные по пройденным тестам \n<b>{await get_student_data(chat_id)}</b>")
            student_mark_up = await keyboard.generate_student_markup(await find_subjects(), 1)
            await bot.send_message(chat_id, text=f'Вы неплохо справились с заданиями!!!!')
            await bot.send_message(chat_id, text=f'Ваши результаты тестирования успешно сохранены',
                                   reply_markup=student_mark_up.as_markup())

        elif 0 <= score <= 3:
            await bot.send_photo(chat_id=chat_id,
                                 photo='https://static.ua-football.com/img/upload/21/2a6555.jpeg')
            await add_test_student_mark(subject, score,
                                        await get_test_student_id(chat_id))  # не всегда chad_id совпадает с user_id!!
            await bot.send_message(chat_id, f"Ваше Имя -- <b>{await get_test_student_first_name(chat_id)}</b>\n"
                                            f"Ваше Отчество -- <b>{await get_test_student_middle_name(chat_id)}</b>\n"
                                            f"Ваша Фамилия -- <b>{await get_test_student_last_name(chat_id)}</b>\n"
                                            f"Ваш номер телефона -- <b>{await get_test_student_phone_number(chat_id)}</b>\n"
                                            f"Ваши данные по пройденным тестам \n<b>{await get_student_data(chat_id)}</b>")
            student_mark_up = await keyboard.generate_student_markup(await find_subjects(), 1)
            await bot.send_message(chat_id, text=f'Вы просто ЛУЗЕР!!!!')
            await bot.send_message(chat_id, text=f'Ваши результаты тестирования успешно сохранены',
                                   reply_markup=student_mark_up.as_markup())

    else:
        admin_mark_up = await keyboard.generate_admin_markup(await find_subjects(), 1)
        await bot.send_message(chat_id, text=f'Дорогой, админ! Вы успешно проверили тест, но Ваши результаты в базу'
                                             f' данных сохраняться не будут', reply_markup=admin_mark_up.as_markup())







