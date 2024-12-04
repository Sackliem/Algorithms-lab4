

import matplotlib.pyplot as plt


def heapify(arr, n, i, log):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    log.append((arr[:], n, i, left, right, largest))  # Логируем до сравнения

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        log.append((arr[:], n, i, left, right, largest))  # Логируем после обмена
        heapify(arr, n, largest, log)


def heapsort(arr):
    n = len(arr)
    log = []

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, log)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Обмен корня с последним элементом
        log.append((arr[:], n, 0, -1, -1, i))  # Логируем после обмена корня
        heapify(arr, i, 0, log)

    return log


def visualize_heapsort(log):
    for state, n, i, left, right, largest in log:
        colors = [
            "red" if x == i else
            "green" if x == largest else
            "purple" if x == left or x == right else
            "blue"
            for x in range(len(state))
        ]
        plt.bar(range(len(state)), state, color=colors)
        plt.pause(0.3)
        plt.clf()





