
from aiogram.fsm.state import State, StatesGroup  # библиотека для создания класса в telegram bot
from aiogram import types
from aiogram.fsm.context import FSMContext
from typing import Any, Dict
from Homework.keyboards import keyboard
from Homework.bd_handlers.tests.add_test_question import add_test_question
from Homework.config.config import *
from aiogram import F


class AddRecordQuestion(StatesGroup):
    add_subject = State()
    add_question = State()
    add_variant1 = State()
    add_variant2 = State()
    add_variant3 = State()
    add_variant4 = State()
    add_right_variant = State()
    add_point_quantity = State()


@router.callback_query(F.data == "add_test")
async def add_item(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == admin:
        await callback.message.answer(text=f'{callback.from_user.first_name}, напишите название предмета')
        await state.set_state(AddRecordQuestion.add_subject)
    else:
        await callback.message.answer('Я тебя не понимаю.')


@router.message(AddRecordQuestion.add_subject, F.text.isalpha())  # проверка, что символами являются только буквы
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_subject=message.text)
    await state.set_state(AddRecordQuestion.add_question)
    await message.answer('Напишите название вопроса')


@router.message(AddRecordQuestion.add_subject)
async def add_item(message: types.Message, state: FSMContext):
    await message.answer('Название предмета должно содержать только буквы. Введите название предмета ещё раз')
    await state.set_state(AddRecordQuestion.add_subject)


@router.message(AddRecordQuestion.add_question)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_question=message.text)
    await state.set_state(AddRecordQuestion.add_variant1)
    await message.answer('Напишите первый вариант ответа')


@router.message(AddRecordQuestion.add_variant1)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_variant1=message.text)
    await state.set_state(AddRecordQuestion.add_variant2)
    await message.answer('Напишите второй вариант ответа')


@router.message(AddRecordQuestion.add_variant2)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_variant2=message.text)
    await state.set_state(AddRecordQuestion.add_variant3)
    await message.answer('Напишите третий вариант ответа')


@router.message(AddRecordQuestion.add_variant3)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_variant3=message.text)
    await state.set_state(AddRecordQuestion.add_variant4)
    await message.answer('Напишите четвертый вариант ответа')


@router.message(AddRecordQuestion.add_variant4)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(add_variant4=message.text)
    await state.set_state(AddRecordQuestion.add_right_variant)
    await message.answer('Напишите правильный вариант ответа')


@router.message(AddRecordQuestion.add_right_variant)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(add_right_variant=message.text)
    if (data['add_right_variant'] != data['add_variant1'] and data['add_right_variant'] != data['add_variant2'] and
        data['add_right_variant'] != data['add_variant3'] and data['add_right_variant'] != data['add_variant4']):
        await message.answer(f'Вы ввели неверный ответ, так как правильный ответ должен совпадать с одним из четырех '
                             f'предложенных вариантов ответов')
        await state.set_state(AddRecordQuestion.add_right_variant)
    else:
        await state.set_state(AddRecordQuestion.add_point_quantity)
        await message.answer('Напишите количество баллов, в которое Вы оцениваете Ваш вопрос')


@router.message(AddRecordQuestion.add_point_quantity)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(add_point_quantity=message.text)
    if data['add_point_quantity'].isdigit():  # проверка, являются введённые символы цифрами
        await state.clear()
        await add_record(data=data)  #??????
        add_subject = data["add_subject"]
        add_question = data["add_question"]
        add_variant1 = data["add_variant1"]
        add_variant2 = data["add_variant2"]
        add_variant3 = data["add_variant3"]
        add_variant4 = data["add_variant4"]
        add_right_variant = data["add_right_variant"]
        add_point_quantity = int(data["add_point_quantity"])
        await add_test_question(add_subject, add_question, add_variant1, add_variant2, add_variant3, add_variant4,
                                add_right_variant, add_point_quantity)
        await message.answer('Вопрос успешно создан!', reply_markup=keyboard.admin_menu.as_markup())
    else:
        await message.answer('Вы не верно ввели данные. Количество баллов, которое необходимо оценить вопрос нужно'
                             ' ввести цифрами')
        await state.set_state(AddRecordQuestion.add_point_quantity)  # если не цифры остаемся в том же состоянии


async def add_record(data: Dict[str, Any]) -> None: #??????
    add_subject = data["add_subject"]
    add_question = data["add_subject"]
    add_variant1 = data["add_variant1"]
    add_variant2 = data["add_variant2"]
    add_variant3 = data["add_variant3"]
    add_variant4 = data["add_variant4"]
    add_right_variant = data["add_right_variant"]
    add_point_quantity = data["add_point_quantity"]

