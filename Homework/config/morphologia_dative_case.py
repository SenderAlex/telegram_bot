
import pymorphy2
from pyphrasy.inflect import PhraseInflector


def convert_to_dative_case(text: str):
    morph = pymorphy2.MorphAnalyzer()
    inflector = PhraseInflector(morph)
    form = 'datv'
    return inflector.inflect(text, form)

# print(convert_to_dative_case('математика'))


# nominative_case = parsed_word.inflect({'nomn'}).word
# genitive_case = parsed_word.inflect({'gent'}).word
# dative_case = parsed_word.inflect({'datv'}).word
# accusative_case = parsed_word.inflect({'accs'}).word
# ablative_case = parsed_word.inflect({'ablt'}).word
# prepositional_case = parsed_word.inflect({'loct'}).word
#
# print(f"Именительный падеж: {nominative_case}")
# print(f"Родительный падеж: {genitive_case}")
# print(f"Дательный падеж: {dative_case}")
# print(f"Винительный падеж: {accusative_case}")
# print(f"Творительный падеж: {ablative_case}")
# print(f"Предложный падеж: {prepositional_case}")

