import random


class FlashCards():
    d = {}

    def __init__(self):
        pass

    def play(self) -> str:
        if len(FlashCards.d.items()) == 0:
            return (f"В словаре нет слов!")
        else:
            s = 0
            for russian, english in random.sample([*FlashCards.d.items()], len([*FlashCards.d.items()])):
                print(russian)
                answer = input()
                if (answer.lower() == english):
                    s += 1
            return (f"Готово! Правильно {s} из {len(FlashCards.d.items())} слов")

    def add_word(self, russian: str, english: str) -> str:
        if isinstance(russian, (str)) and isinstance(english, (str)):
            if russian in FlashCards.d:
                return ("Такое слово уже есть в словаре")
            else:
                FlashCards.d.update({russian: english})
                return ('Добавлено слово' + ' ' + str(russian))
        else:
            return ('Неправильный тип ввода!')

    def delete_word(self, russian: str) -> str:
        if isinstance(russian, (str)):
            if russian in FlashCards.d:
                del FlashCards.d[russian]
                return ('Удалено слово' + ' ' + str(russian))
            else:
                return ('Такого слова нет в словаре')
        else:
            return ('Неправильный тип ввода!')

    @property
    def words(self):
        return ([*FlashCards.d.keys()])