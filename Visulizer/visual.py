import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton

def show_log_natural_merge_sort(log: list):
    natural_merge_sort_log_str = "\n".join(f"Step {i + 1}: {entry}" for i, entry in enumerate(log))

    dialog = QDialog()
    dialog.setWindowTitle("Natural Merge Sort Logs")
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText(natural_merge_sort_log_str.strip())  # Remove trailing newline

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)
    dialog.exec_()

def show_log_selection_sort(log: list):
    # Prepare a string to hold the formatted log entries
    selection_sort_log_str = ""

    for step, (current_state, i, min_idx, j) in enumerate(log):
        # Format each log entry
        selection_sort_log_str += f"Step {step + 1}:\n"
        selection_sort_log_str += f"Array state: {current_state}\n"
        selection_sort_log_str += f"Current index (i): {i}, Minimum index (min_idx): {min_idx}, Comparing index (j): {j}\n\n"

    dialog = QDialog()
    dialog.setWindowTitle("Selection Sort Logs")
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText(selection_sort_log_str.strip())  # Remove trailing newline

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)

    dialog.exec_()

def show_log_radix_sort(log: list):
    # Prepare a string to hold the formatted log entries
    radix_sort_log_str = ""

    for step, buckets in enumerate(log):
        # Format each log entry
        radix_sort_log_str += f"Step {step + 1}:\n"
        for idx, bucket in enumerate(buckets):
            radix_sort_log_str += f"Bucket {idx}: {bucket}\n"
        radix_sort_log_str += "\n"  # Add a newline for better separation between steps

    dialog = QDialog()
    dialog.setWindowTitle("Radix Sort Logs")
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText(radix_sort_log_str.strip())  # Remove trailing newline

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)

    dialog.exec_()


def show_log_generic(log: list, title: str, format_func) -> None:
    log_str = format_func(log)

    dialog = QDialog()
    dialog.setWindowTitle(title)
    dialog.setGeometry(100, 100, 600, 400)

    layout = QVBoxLayout()

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setPlainText(log_str.strip())  # Remove trailing newline

    layout.addWidget(text_edit)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    layout.addWidget(ok_button)

    dialog.setLayout(layout)

    dialog.exec_()


def format_log_merge(log: list) -> str:
    return "\n".join(
        f"Step {step + 1}: Comparing indices {index1} and {index2}\n"
        f"Array state: {current_state}\n"
        for step, (current_state, index1, index2) in enumerate(log)
    )


def format_log_heapsort(log: list) -> str:
    return "\n".join(
        f"Step {step + 1}:\n"
        f"Array state: {current_state}\n"
        f"n: {n}, i: {i}, left: {left}, right: {right}, largest: {largest}\n"
        for step, (current_state, n, i, left, right, largest) in enumerate(log)
    )


def format_log_selection_sort(log: list) -> str:
    return "\n".join(
        f"Step {step + 1}:\n"
        f"Array state: {current_state}\n"
        f"Current index (i): {i}, Minimum index (min_idx): {min_idx}, Comparing index (j): {j}\n"
        for step, (current_state, i, min_idx, j) in enumerate(log)
    )


def format_log_quicksort(log: list) -> str:
    return "\n".join(
        f"Step {step + 1}:\n"
        f"Array state: {current_state}\n"
        f"Low index: {low}, High index: {high}, Current index (j): {j}, Swap index (i): {i}, Pivot index: {pivot_index}\n"
        for step, (current_state, low, high, j, i, pivot_index) in enumerate(log)
    )


def show_log_merge(log):
    show_log_generic(log, "Sorting Logs", format_log_merge)


def show_log_heapsort(log):
    show_log_generic(log, "Heapsort Logs", format_log_heapsort)


def show_log_selection_sort(log):
    show_log_generic(log, "Selection Sort Logs", format_log_selection_sort)


def show_log_quicksort(log):
    show_log_generic(log, "Quicksort Logs", format_log_quicksort)