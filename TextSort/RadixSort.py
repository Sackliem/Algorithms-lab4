from .BaseSort import BaseSort
import matplotlib.pyplot as plt
from math import factorial


class RadixSort(BaseSort):
    def __init__(self):
        super().__init__()
        self.log = []  # Лог для записи состояния корзин на каждом шаге

    def sort(self):
        max_length = max(len(word) for word in self.words)  # Определяем максимальную длину слов

        for i in range(max_length - 1, -1, -1):
            buckets = [[] for _ in range(33)]  # 33 корзины для русского алфавита
            for word in self.words:
                char = word[i] if i < len(word) else ''
                if char:
                    index = ord(char) - ord('а')
                    buckets[index].append(word)
                else:
                    buckets[0].append(word)

            self.log.append([bucket[:] for bucket in buckets])  # Логируем состояние корзин
            self.words = [word for bucket in buckets for word in bucket]

    def count_words(self):
        for word in self.words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1


def lexi_length(word):
    word = list(word)
    length = len(word)
    lexi_length = 0

    for i in range(length):
        # Считаем, сколько символов меньше текущего символа word[i]
        count = 0
        for j in range(i + 1, length):
            if word[j] < word[i]:
                count += 1

        # Добавляем количество перестановок, которые могут быть сформированы
        lexi_length += count * factorial(length - i - 1)

    return lexi_length + 1


def visualize_radix_sort(log):
    colors = plt.cm.tab20.colors  # Используем цветовую палитру

    for step, buckets in enumerate(log):
        plt.clf()
        plt.title(f"Step {step + 1}: Distribution by Buckets")
        all_words = []
        all_colors = []

        for idx, bucket in enumerate(buckets):
            all_words.extend(bucket)
            all_colors.extend([colors[idx % len(colors)]] * len(bucket))

        plt.bar(range(len(all_words)), [lexi_length(word) for word in all_words], color=all_colors)
        plt.xticks(range(len(all_words)), all_words, rotation=90)
        plt.ylabel("Word Length")
        plt.xlabel("Words")
        plt.pause(1)

    plt.show()

# sorter = RadixSort()
# sorter.words = ["мама", "мыло", "рама", "арбуз", "осень", "яблоко", "игра"]
# sorter.sort()
# print("Отсортированные слова:", sorter.words)
# visualize_radix_sort(sorter.log)