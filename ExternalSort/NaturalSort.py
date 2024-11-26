import time
import csv
import Visulizer.visual
from Visulizer.visual import visualize_str, show_logs, show_log_merge


class NaturalMergeSort:
    def __init__(self, file_path, key_index, delay):
        self.file_path = file_path
        self.key_index = key_index
        self.delay = delay
        self.log = []
        self.headers, self.data = self.read_file()
        self.natural_merge_sort()
        show_log_merge(self.log)
        self.write_file()

    # Чтение данных из файла
    def read_file(self) -> (list, list):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            data = [row for row in reader]
        return headers, data

    # Запись данных в файл
    def write_file(self):
        with open("sorted.csw", 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data)

    # Естественное слияние
    def natural_merge_sort(self):
        self.log.clear()
        n = len(self.data)
        while True:
            runs = []
            run = [self.data[0]]

            for i in range(1, n):
                if self.data[i][self.key_index] >= self.data[i - 1][self.key_index]:
                    run.append(self.data[i])
                else:
                    runs.append(run)
                    run = [self.data[i]]
            runs.append(run)

            if len(runs) == 1:
                break

            merged = []
            while len(runs) > 1:
                run1 = runs.pop(0)
                run2 = runs.pop(0)
                merged.append(self.merge(run1, run2, self.key_index, self.delay))

            if runs:
                merged.append(runs.pop(0))

            self.data = [item for sublist in merged for item in sublist]
            time.sleep(self.delay)

    # Функция для слияния двух списков
    def merge(self, run1, run2, key_index, delay):
        result = []
        i = j = 0
        while i < len(run1) and j < len(run2):
            comparison = f"Сравнение: {run1[i][key_index]} и {run2[j][key_index]}"
            self.log.append(comparison)
            if run1[i][key_index] <= run2[j][key_index]:
                result.append(run1[i])
                self.log.append(f"Добавлено: {run1[i]}")
                i += 1
            else:
                result.append(run2[j])
                self.log.append(f"Добавлено: {run2[j]}")
                j += 1
            time.sleep(delay)
        result.extend(run1[i:])
        result.extend(run2[j:])
        return result



