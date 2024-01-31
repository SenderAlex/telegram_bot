from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from Homework.config.morphologia_dative_case import convert_to_dative_case

# главное меню админа
async def generate_admin_markup(texts: list, row_width: int) -> InlineKeyboardBuilder:  #???????????????????????????
    admin_markup = InlineKeyboardBuilder()
    for num, text in enumerate(texts):
        admin_markup.row(InlineKeyboardButton(text=f"{num+1}. Тест по {convert_to_dative_case(text)}",
                         callback_data=f"register {text}"), width=row_width)
    admin_markup.row(InlineKeyboardButton(text='Админ-панель', callback_data='admin'))
    return admin_markup


# главное меню студента
async def generate_student_markup(texts: list, row_width: int) -> InlineKeyboardBuilder:  #???????????????????????????
    student_markup = InlineKeyboardBuilder()
    for num, text in enumerate(texts):
        student_markup.row(InlineKeyboardButton(text=f"{num+1}. Тест по {convert_to_dative_case(text)}",
                           callback_data=f"register {text}"), width=row_width)
    return student_markup


# меню администратора
admin_menu = InlineKeyboardBuilder()
admin_menu.row(
               types.InlineKeyboardButton(text='Добавить вопрос', callback_data='add_test'),
               types.InlineKeyboardButton(text='Редактировать вопрос', callback_data='edit_test'),
               types.InlineKeyboardButton(text='Удалить вопрос', callback_data='delete_test'),
               types.InlineKeyboardButton(text='Отмена', callback_data='cancel_admin_menu'),
               width=1
)


# кнопки для викторины
async def generate_quiz_markup(answers: list, row_width: int) -> InlineKeyboardBuilder:
    quiz_markup = InlineKeyboardBuilder()
    for number, answer in enumerate(answers):
        quiz_markup.row(InlineKeyboardButton(text=f"{answer}", callback_data=f"quiz {number} {answer}"),
                        width=row_width)
    return quiz_markup



