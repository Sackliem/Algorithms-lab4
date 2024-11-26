from .BaseSort import BaseSort
from utils.Timer import timer
from Visulizer.visual import visualize_str, show_logs
import keyboard


class RadixSort(BaseSort):
    @timer
    def sort(self):
        comparisons_log = []  # Лог сравнений
        swaps_log = []  # Лог перестановок
        check = True  # Флаг для отображения шагов

        # Определяем максимальную длину слов
        max_length = max(len(word) for word in self.words)

        # Проход по всем разрядам с конца
        for i in range(max_length - 1, -1, -1):
            buckets = [[] for _ in range(33)]  # 33 корзины для символов русского алфавита

            # Распределение слов по корзинам
            for word in self.words:
                char = word[i] if i < len(word) else ''

                if char:
                    index = ord(char) - ord('а')
                    comparisons_log.append((char, f"разряд {i + 1}"))  # Лог символа и разряда
                    swaps_log.append((word, f"корзина {index}"))  # Лог перемещения слова
                    buckets[index].append(word)
                else:
                    comparisons_log.append((word, f"разряд {i + 1} -> пустой символ"))
                    swaps_log.append((word, "корзина 0"))  # Лог перемещения в корзину 0
                    buckets[0].append(word)

            # Сбор отсортированных данных из корзин
            self.words = [word for bucket in buckets for word in bucket]

            # Визуализация текущего состояния
        #     if check:
        #         visualize_str(self.words)
        #     if keyboard.is_pressed('esc'):
        #         check = False
        #
        # # Финальная визуализация
        # visualize_str(self.words)

        # Передача логов в функцию вывода
        show_logs(comparisons_log, swaps_log)

    def count_words(self):
        for word in self.words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

