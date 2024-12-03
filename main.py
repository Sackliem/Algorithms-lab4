import sys
from Visulizer.visual import *

from alg import Bable_Sort, Heap_sort, QuickSort, Selection_sort
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QFileDialog
from random import randint
from threading import *
from TextSort import tests


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
                Bable_Sort.bubble_sort(data.copy(), step)
            elif sort_method == "selection":
                Selection_sort.selection_sort(data.copy(), step)
            elif sort_method == "heapsort":
                Heap_sort.heap_sort(data.copy(), step)
            elif sort_method == "quicksort":
                arr = QuickSort.quicksort(data.copy(),step)
                visualize_q(arr[0], arr[1], len(arr[0]) - 1)
            elif sort_method == 'textsort/radixSort':
                tests.run_Radix(size)
            elif sort_method == 'textsort/selectSort':
                tests.run_Selection(size)
            elif sort_method == 'externalsort/NaturalMergeSort':
                from ExternalSort.NaturalSort import NaturalMergeSort
                NaturalMergeSort(self.filepath, key, delay)
            else:
                print("Неверный метод сортировки.")

            plt.ioff()
            plt.show()

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
