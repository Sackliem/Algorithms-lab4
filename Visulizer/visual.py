import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QPushButton


def show_logs(comparisons_log, swaps_log):
    comparisons_str = "\n".join([f"Comparing: {comp[0]} and {comp[1]}" for comp in comparisons_log])
    swaps_str = "\n".join([f"Swapping indices: {swap[0]} and {swap[1]}" for swap in swaps_log])

    dialog = QDialog()
    dialog.setWindowTitle("Sorting Logs")
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText("Comparisons made:\n" + comparisons_str + "\n\nSwaps made:\n" + swaps_str)

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)

    dialog.exec_()


def show_log_merge(log: list):
    comparisons_str = "\n".join(log)
    dialog = QDialog()
    dialog.setWindowTitle("Sorting Logs")
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText(comparisons_str)

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)

    dialog.exec_()



def visualize(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.xlim(-1, len(arr))
    plt.ylim(0, max(arr) + 1)
    plt.title("Sorting Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.5)


def visualize_str(words):
    plt.clf()
    plt.bar(range(len(words)), [len(word) for word in words], color='blue')
    plt.xticks(range(len(words)), words, rotation=45, ha='right')  # Установка слов на оси X
    plt.ylim(0, max(len(word) for word in words) + 1)  # Ограничение по Y
    plt.title(f"Sorting Visualization")
    plt.ylabel("Length of Words")
    plt.xlabel("Words")
    plt.pause(0.5)
