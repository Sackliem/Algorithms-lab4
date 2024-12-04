from tabnanny import check

from .BaseSort import BaseSort
import matplotlib.pyplot as plt


class SelectionSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.log = []  # Лог для записи шагов сортировки

    def sort(self):
        n = len(self.words)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.log.append((self.words[:], i, min_idx, j))  # Логируем сравнение
                if self.words[j] < self.words[min_idx]:
                    min_idx = j
                    self.log.append((self.words[:], i, min_idx, j))  # Логируем выбор нового минимального элемента

            if min_idx != i:
                self.words[i], self.words[min_idx] = self.words[min_idx], self.words[i]
                self.log.append((self.words[:], i, min_idx, -1))  # Логируем обмен

    def count_words(self):
        for word in self.words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1


def visualize_selection_sort(log):
    for state, i, min_idx, j in log:
        colors = [
            "green" if x == i else
            "red" if x == min_idx else
            "purple" if x == j else
            "blue"
            for x in range(len(state))
        ]
        plt.bar(range(len(state)), [len(word) for word in state], color=colors)
        plt.xticks(range(len(state)), state, rotation=90)  # Подписи на оси X
        plt.title(f"Step: Comparing '{state[j]}' and min '{state[min_idx]}'")
        plt.pause(0.5)
        plt.clf()

