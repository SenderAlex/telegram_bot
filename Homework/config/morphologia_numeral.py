
from num2words import num2words

def get_correct_expression(number, word):
    number_word = num2words(number, lang='ru')  # Преобразуем число в слово
    if number % 10 == 1 and number % 100 != 11:  # Формируем правильную форму слова "балл" в зависимости от числа
        word += ""
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        word += "а"
    else:
        word += "ов"
    result = f"{number_word} {word}"  # Объединяем число и слово
    return result


# score = 11
# result = get_correct_expression(score, "балл")
# print(result)