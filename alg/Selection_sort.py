
import matplotlib.pyplot as plt


def selection_sort(arr):
    n = len(arr)
    log = []  # Лог для записи шагов сортировки

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            log.append((arr[:], i, min_idx, j))  # Логируем сравнение
            if arr[j] < arr[min_idx]:
                min_idx = j
                log.append((arr[:], i, min_idx, j))  # Логируем выбор нового минимального элемента

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        log.append((arr[:], i, min_idx, -1))  # Логируем обмен

    return arr, log


def visualize_selection_sort(log):
    for state, i, min_idx, j in log:
        colors = [
            "green" if x == i else
            "red" if x == min_idx else
            "purple" if x == j else
            "blue"
            for x in range(len(state))
        ]
        plt.bar(range(len(state)), state, color=colors)
        plt.pause(0.3)
        plt.clf()






