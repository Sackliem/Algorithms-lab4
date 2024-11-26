from tabnanny import check

from .BaseSort import BaseSort
from utils.Timer import timer
from Visulizer.visual import visualize_str, show_logs
import keyboard


class SelectionSort(BaseSort):

    @timer
    def sort(self):
        n = len(self.words)
        comparisons_log = []  # Лог сравнений
        swaps_log = []  # Лог перестановок
        check = True  # Флаг для отображения шагов

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                # Лог сравнения
                comparisons_log.append((self.words[j], self.words[min_idx]))
                if self.words[j] < self.words[min_idx]:
                    min_idx = j

            # Лог перестановки, если найден элемент меньше текущего
            if min_idx != i:
                swaps_log.append((i, min_idx))
                self.words[i], self.words[min_idx] = self.words[min_idx], self.words[i]

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