
from aiogram.fsm.state import State, StatesGroup  # библиотека для создания класса в telegram bot
from aiogram import types
from aiogram.fsm.context import FSMContext
from Homework.keyboards import keyboard
from Homework.bd_handlers.tests.delete_test_question import delete_test_question
from Homework.bd_handlers.tests.find_id_test_question import find_id_test_question
from Homework.config.config import *
from typing import Any, Dict
from aiogram import F


class DeleteRecordQuestion(StatesGroup):
    delete_question_id = State()


@router.callback_query(F.data == 'delete_test')
async def delete_item(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == admin:
        await callback.message.answer(text=f'{callback.from_user.first_name}, введите id вопроса, который вы хотите удалить')
        await state.set_state(DeleteRecordQuestion.delete_question_id)
    else:
        await callback.message.answer('Я тебя не понимаю.')


@router.message(DeleteRecordQuestion.delete_question_id)
async def add_item(message: types.Message, state: FSMContext):
    data = await state.update_data(delete_question_id=message.text)
    id_delete = message.text
    try:
        if isinstance(int(data['delete_question_id']), int) == True:
            id_number = await find_id_test_question(int(id_delete))
            if id_number == int(id_delete):
                await state.clear()
                await delete_record(data=data)
                delete_question_id = int(data["delete_question_id"])
                await delete_test_question(delete_question_id)
                await message.answer('Вопрос успешно удален!', reply_markup=keyboard.admin_menu.as_markup())
            else:
                await message.answer('Такой записи не существует!!!')
                await state.set_state(DeleteRecordQuestion.delete_question_id)
    except ValueError:
        await message.answer('Вы ввели неверный id. ID должен содержать только цифры!!')
        await state.set_state(DeleteRecordQuestion.delete_question_id)

async def delete_record(data: Dict[str, Any]) -> None:
    delete_question_id = data["delete_question_id"]


