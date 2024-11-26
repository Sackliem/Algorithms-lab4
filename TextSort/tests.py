from TextSort.BaseSort import BaseSort
from TextSort.RadixSort import RadixSort
from TextSort.SelectionSort import SelectionSort
import re
import random

"""
методы возвращают по типу

{
    "sorted_text": "слово1 слово2 слово3",
    "word_count": {
        "слово1": 1,
        "слово2": 1,
        "слово3": 1
    },
    "time": 0.1 # в миллисекундах
}

"""
# Пример использования
"""
Tester(RadixSort()).manual_test()
Tester(RadixSort()).auto_test()
Tester(SelectionSort()).manual_test()
Tester(SelectionSort()).auto_test()
"""



class Tester:

    def __init__(self, algorithm: BaseSort):
        self.algorithm = algorithm
        self.text_lenght = None
        self.text = None
        self.times = None

    @staticmethod
    def random_word_generator(num_words=10, min_length=3, max_length=8):
        """
        Генератор случайных слов.

        :param num_words: Количество слов для генерации.
        :param min_length: Минимальная длина слова.
        :param max_length: Максимальная длина слова.
        :return: Список случайных слов.
        """
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        words = []

        for _ in range(num_words):
            word_length = random.randint(min_length, max_length)
            word = ''.join(random.choice(alphabet) for _ in range(word_length))
            words.append(word)

        return words

    def auto_test(self, lenght=100):
        self.text_lenght = lenght
        self.text = self.random_word_generator(num_words=self.text_lenght)
        self.algorithm.words = self.text
        self.times = self.algorithm.sort()
        self.algorithm.count_words()
        return {
            "sorted_text": ' '.join(self.algorithm.words),
            "word_count": self.algorithm.word_count,
            "time": self.times
        }

    def manual_test(self):
        self.text = input("Enter text: ").lower()
        self.text = re.sub(r'[^а-я\s]+', '', self.text).strip()
        self.text = re.sub(" +", " ", self.text)
        self.algorithm.words = self.text.split(" ")
        self.times = self.algorithm.sort()
        self.algorithm.count_words()
        return {
            "sorted_text": ' '.join(self.algorithm.words),
            "word_count": self.algorithm.word_count,
            "time": self.times
        }


def run_Radix(count: int = 100):
    res = Tester(RadixSort()).auto_test(count)
    print(res)


def run_Selection(count: int = 100):
    res = Tester(SelectionSort()).auto_test(count)
    print(res)
