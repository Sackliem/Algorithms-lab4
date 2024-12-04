import csv
import time

class NaturalMergeSort:
    def __init__(self, file_path, key_index, delay):
        self.file_path = file_path
        self.key_index = key_index
        self.delay = delay
        self.headers, self.data = self.read_file()
        self.log = []  # Лог для записи всех шагов
        self.natural_merge_sort()
        self.write_file()
        self.show_log()

    # Чтение данных из файла
    def read_file(self) -> (list, list):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            data = [row for row in reader]
        return headers, data

    # Запись данных в файл
    def write_file(self):
        with open("sorted.csv", 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data)

    # Естественное слияние с логированием
    def natural_merge_sort(self):
        n = len(self.data)
        step = 1
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

            self.log.append(f"Step {step}: Initial runs: {runs}")
            step += 1

            if len(runs) == 1:
                self.log.append("Sorted data: Single run remains.")
                break

            merged = []
            while len(runs) > 1:
                run1 = runs.pop(0)
                run2 = runs.pop(0)
                merged_run = self.merge(run1, run2, self.key_index, self.delay)
                self.log.append(f"Merging runs: {run1} + {run2} -> {merged_run}")
                merged.append(merged_run)

            if runs:
                remaining_run = runs.pop(0)
                self.log.append(f"Remaining run: {remaining_run}")
                merged.append(remaining_run)

            self.data = [item for sublist in merged for item in sublist]
            self.log.append(f"End of step {step - 1}, merged data: {self.data}")
            time.sleep(self.delay)

    # Функция для слияния двух списков с логированием
    def merge(self, run1, run2, key_index, delay):
        result = []
        i = j = 0
        while i < len(run1) and j < len(run2):
            if run1[i][key_index] <= run2[j][key_index]:
                result.append(run1[i])
                i += 1
            else:
                result.append(run2[j])
                j += 1
            time.sleep(delay)
        result.extend(run1[i:])
        result.extend(run2[j:])
        return result

    # Вывод логов
    def show_log(self):
        for entry in self.log:
            print(entry)


# # Пример использования:
# sorter = NaturalMergeSort('../test.csv', 0, 0)
