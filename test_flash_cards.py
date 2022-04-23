import unittest
from unittest.mock import Mock, patch, call
from flash_cards import FlashCards


class FCTestCase(unittest.TestCase):

    def setUp(self):
        self.fc = FlashCards()

    def test_flashcards_wrong_type_add_word(self):
        self.assertEqual('Неправильный тип ввода!', self.fc.add_word(123, 432))

    def test_flashcards_wrong_type_delete_word(self):
        self.assertEqual('Неправильный тип ввода!', self.fc.delete_word(432))

    def test_flashcards_no_words(self):
        self.fc.delete_word('груша')
        self.assertEqual('В словаре нет слов!', self.fc.play())

    def test_flashcards_add_ok_word(self):
        self.assertEqual('Добавлено слово груша', self.fc.add_word('груша', 'pear'))
        self.fc.delete_word('груша')

    def test_flashcards_del_ok_word(self):
        self.fc.add_word('груша', 'pear')
        self.assertEqual('Удалено слово груша', self.fc.delete_word('груша'))

    def test_flashcards_del_non_exist_word(self):
        self.assertEqual('Такого слова нет в словаре', self.fc.delete_word('папайя'))

    @patch('builtins.input', return_value='pear')
    def test_answer_when_words(self, input):
        self.fc.add_word('груша', 'pear')
        self.fc.add_word('петрушка', 'parsley')
        self.fc.add_word('мама', 'mum')
        self.assertEqual(self.fc.play(), 'Готово! Правильно 1 из 3 слов')
        self.fc.delete_word('груша')
        self.fc.delete_word('петрушка')
        self.fc.delete_word('мама')
        self.assertEqual(self.fc.play(), 'В словаре нет слов!')

    @patch('builtins.input', return_value='pear')
    def test_added_words(self, input):
        self.fc.add_word('папа', 'dad')
        self.fc.add_word('груша', 'pear')
        self.fc.add_word('петрушка', 'parsley')
        self.fc.add_word('папа', 'dad')
        self.assertEqual(3, len(self.fc.words))
        self.fc.delete_word('груша')
        self.fc.delete_word('петрушка')
        self.fc.delete_word('папа')
        self.assertEqual(0, len(self.fc.words))


if __name__ == '__main__':
    unittest.main()
