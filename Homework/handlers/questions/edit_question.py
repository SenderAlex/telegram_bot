
from aiogram.fsm.state import State, StatesGroup  # библиотека для создания класса в telegram bot
from aiogram import types
from aiogram.fsm.context import FSMContext
from typing import Any, Dict
from Homework.bd_handlers.tests.find_id_test_question import find_id_test_question
from Homework.keyboards import keyboard
from Homework.bd_handlers.tests.edit_test_question import edit_test_question
from Homework.config.config import *
from aiogram import F


class EditRecordQuestion(StatesGroup):
    edit_question_id = State()
    edit_subject = State()
    edit_question = State()
    edit_variant1 = State()
    edit_variant2 = State()
    edit_variant3 = State()
    edit_variant4 = State()
    edit_right_variant = State()
    edit_point_quantity = State()


@router.callback_query(F.data == "edit_test")
async def add_item(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == admin:
        await callback.message.answer(text=f'{callback.from_user.first_name}, напишите ID записи, которую Вы будете редактировать')
        await state.set_state(EditRecordQuestion.edit_question_id)
    else:
        await callback.message.answer('Я тебя не понимаю.')


@router.message(EditRecordQuestion.edit_question_id)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(edit_question_id=message.text)
    id_edit = message.text
    try:
        if isinstance(int(data['edit_question_id']), int) == True:
            id_number = await find_id_test_question(int(id_edit))
            if id_number == int(id_edit):
                await state.set_state(EditRecordQuestion.edit_subject)
                await message.answer('Отредактируйте предмет, по которому будет проводится тестирование')
            else:
                await message.answer('Такой записи не существует!!!')
                await state.set_state(EditRecordQuestion.edit_question_id)
    except ValueError:
        await message.answer('Вы ввели неверный id. ID должен содержать только цифры!!')
        await state.set_state(EditRecordQuestion.edit_question_id)


@router.message(EditRecordQuestion.edit_subject, F.text.isalpha())  # проверка, что символами являются только буквы
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_subject=message.text)
    await state.set_state(EditRecordQuestion.edit_question)
    await message.answer('Отредактируйте тестовый вопрос')


@router.message(EditRecordQuestion.edit_subject)
async def add_item(message: types.Message, state: FSMContext):
    await message.answer('Название предмета должно содержать только буквы. Введите название предмета ещё раз')
    await state.set_state(EditRecordQuestion.edit_subject)


@router.message(EditRecordQuestion.edit_question)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_question=message.text)
    await state.set_state(EditRecordQuestion.edit_variant1)
    await message.answer('Отредактируйте первый вариант ответа')


@router.message(EditRecordQuestion.edit_variant1)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_variant1=message.text)
    await state.set_state(EditRecordQuestion.edit_variant2)
    await message.answer('Отредактируйте второй вариант ответа')


@router.message(EditRecordQuestion.edit_variant2)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_variant2=message.text)
    await state.set_state(EditRecordQuestion.edit_variant3)
    await message.answer('Отредактируйте третий вариант ответа')


@router.message(EditRecordQuestion.edit_variant3)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_variant3=message.text)
    await state.set_state(EditRecordQuestion.edit_variant4)
    await message.answer('Отредактируйте четвертый вариант ответа')


@router.message(EditRecordQuestion.edit_variant4)
async def add_item(message: types.Message, state: FSMContext):
    await state.update_data(edit_variant4=message.text)
    await state.set_state(EditRecordQuestion.edit_right_variant)
    await message.answer('Отредактируйте правильный вариант ответа')


@router.message(EditRecordQuestion.edit_right_variant)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(edit_right_variant=message.text)
    if (data['edit_right_variant'] != data['edit_variant1'] and data['edit_right_variant'] != data['edit_variant2'] and
        data['edit_right_variant'] != data['edit_variant3'] and data['edit_right_variant'] != data['edit_variant4']):
        await message.answer(f'Вы ввели неверный ответ, так как правильный ответ должен совпадать с одним из четырех '
                             f'предложенных вариантов ответов')
        await state.set_state(EditRecordQuestion.edit_right_variant)
    else:
        await state.set_state(EditRecordQuestion.edit_point_quantity)
        await message.answer('Отредактируйте количество баллов, в которое Вы оцениваете Ваш вопрос')


@router.message(EditRecordQuestion.edit_point_quantity)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(edit_point_quantity=message.text)
    if data['edit_point_quantity'].isdigit():
        await state.clear()
        await edit_record(data=data)
        edit_subject = data["edit_subject"]
        edit_question = data["edit_question"]
        edit_variant1 = data["edit_variant1"]
        edit_variant2 = data["edit_variant2"]
        edit_variant3 = data["edit_variant3"]
        edit_variant4 = data["edit_variant4"]
        edit_right_variant = data["edit_right_variant"]
        edit_point_quantity = int(data["edit_point_quantity"])
        edit_question_id = int(data["edit_question_id"])
        await edit_test_question(edit_subject, edit_question, edit_variant1, edit_variant2, edit_variant3, edit_variant4,
                                edit_right_variant, edit_point_quantity, edit_question_id)
        await message.answer('Вопрос успешно отредактирован!', reply_markup=keyboard.admin_menu.as_markup())
    else:
        await message.answer('Вы не верно ввели данные. Количество баллов, которое необходимо оценить вопрос нужно'
                             ' ввести цифрами')
        await state.set_state(EditRecordQuestion.edit_point_quantity)


async def edit_record(data: Dict[str, Any]) -> None:
    edit_question_id = data["edit_question_id"]
    edit_subject = data["edit_subject"]
    edit_question = data["edit_subject"]
    edit_variant1 = data["edit_variant1"]
    edit_variant2 = data["edit_variant2"]
    edit_variant3 = data["edit_variant3"]
    edit_variant4 = data["edit_variant4"]
    edit_right_variant = data["edit_right_variant"]
    edit_point_quantity = data["edit_point_quantity"]
