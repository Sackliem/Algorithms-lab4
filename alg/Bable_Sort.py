import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    log = []  # Лог для хранения шагов сортировки

    for i in range(n):
        for j in range(0, n - i - 1):
            # Сохраняем текущее состояние массива
            log.append((arr[:], j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                log.append((arr[:], j, j + 1))  # Логируем после обмена

    return arr, log


def visualize_bubble_sort(log):
    for state, i, j in log:
        plt.bar(range(len(state)), state, color=["red" if x == i or x == j else "blue" for x in range(len(state))])
        plt.pause(0.3)
        plt.clf()














