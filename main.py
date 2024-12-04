import sys
from Visulizer.visual import *

from alg import Bable_Sort, Heap_sort, QuickSort, Selection_sort
from TextSort import RadixSort, SelectionSort, BaseSort
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QFileDialog
from random import randint
from threading import *
from ExternalSort.NaturalSort import NaturalMergeSort


class SortVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сортировка с визуализацией')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Выберите метод сортировки:')
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(['bubble', 'selection', 'heapsort', 'quicksort', 'textsort/radixSort',
                             'textsort/selectSort', 'externalsort/NaturalMergeSort'])
        layout.addWidget(self.combo)

        self.steps_label = QLabel('Введите количество шагов в визуализации:')
        layout.addWidget(self.steps_label)
        self.steps_input = QLineEdit()
        layout.addWidget(self.steps_input)

        self.size_label = QLabel('Введите количество данных в массиве:')
        layout.addWidget(self.size_label)
        self.size_input = QLineEdit()
        layout.addWidget(self.size_input)

        self.file_button = QPushButton('выбрать файл')
        self.file_button.clicked.connect(self.get_file)
        layout.addWidget(self.file_button)

        self.key_index = QLabel('По какому полю сортируем файл:')
        layout.addWidget(self.key_index)
        self.key_index_in = QLineEdit()
        layout.addWidget(self.key_index_in)

        self.sort_deley = QLabel('Введите задержку:')
        layout.addWidget(self.sort_deley)
        self.sort_deley_in = QLineEdit()
        layout.addWidget(self.sort_deley_in)

        self.sort_button = QPushButton('Запустить сортировку')
        self.sort_button.clicked.connect(self.thread)
        layout.addWidget(self.sort_button)

        self.setLayout(layout)

    def get_file(self):
        self.filepath = str(QFileDialog.getOpenFileName(self, 'Select a File')[0])

    def run_sorting(self):
        sort_method = self.combo.currentText()
        try:
            step = int(self.steps_input.text())
            delay = int(self.sort_deley_in.text())
            key = int(self.key_index_in.text())
            size = int(self.size_input.text())
            data = [randint(100, 1000) for _ in range(size)]  # Use user-defined size
            plt.ion()

            if sort_method == "bubble":
                _, log = Bable_Sort.bubble_sort(data.copy())
                plt.figure(figsize=(10, 5))
                Bable_Sort.visualize_bubble_sort(log)
                plt.show()
                show_log_merge(log)
            elif sort_method == "selection":
                sorted_arr, log = Selection_sort.selection_sort(data.copy())
                plt.figure(figsize=(10, 5))
                Selection_sort.visualize_selection_sort(log)
                plt.show()
                show_log_selection_sort(log)
            elif sort_method == "heapsort":
                log = Heap_sort.heapsort(data.copy())
                plt.figure(figsize=(10, 5))
                Heap_sort.visualize_heapsort(log)
                plt.show()
                show_log_heapsort(log)
            elif sort_method == "quicksort":
                log = []
                QuickSort.quicksort(data.copy(), 0, len(data) - 1, log)
                plt.figure(figsize=(10, 5))
                QuickSort.visualize_quicksort(log)
                plt.show()
                show_log_quicksort(log)
            elif sort_method == 'textsort/radixSort':
                sorter = RadixSort.RadixSort()
                sorter.words = ["мама", "мыло", "рама", "арбуз", "осень", "яблоко", "игра"]
                sorter.sort()
                RadixSort.visualize_radix_sort(sorter.log)
                show_log_radix_sort(sorter.log)
            elif sort_method == 'textsort/selectSort':
                sorter = SelectionSort.SelectionSort()
                sorter.words = ["мама", "мыло", "рама", "арбуз", "осень", "яблоко", "игра"]
                sorter.sort()
                SelectionSort.visualize_selection_sort(sorter.log)
                show_log_selection_sort(sorter.log)
            elif sort_method == 'externalsort/NaturalMergeSort':
                sorter = NaturalMergeSort('test.csv', 0, 0)
                show_log_natural_merge_sort(sorter.log)
            else:
                print("Неверный метод сортировки.")

        except ValueError:
            print("Пожалуйста, введите корректное число шагов и количество данных.")

    def thread(self):
        t1 = Thread(target=self.run_sorting())
        t1.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SortVisualizer()
    ex.show()
    sys.exit(app.exec_())
