import matplotlib.pyplot as plt


def quicksort(arr, low, high, log):
    if low < high:
        pivot_index = partition(arr, low, high, log)
        quicksort(arr, low, pivot_index - 1, log)
        quicksort(arr, pivot_index + 1, high, log)


def partition(arr, low, high, log):
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1

    for j in range(low, high):
        log.append((arr[:], low, high, j, i, high))  # Логируем текущее состояние
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            log.append((arr[:], low, high, j, i, high))  # Логируем после обмена

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    log.append((arr[:], low, high, high, i + 1, high))  # Логируем обмен с опорным
    return i + 1


def visualize_quicksort(log):
    for state, low, high, j, i, pivot_index in log:
        colors = [
            "red" if x == j else  # Current index being compared
            "green" if x == i + 1 else  # Index where the next smaller element will go
            "purple" if x == pivot_index else  # Pivot element
            "gray" if state[x] < state[pivot_index] else  # Elements less than the pivot
            "blue"  # All other elements
            for x in range(len(state))
        ]

        plt.bar(range(len(state)), state, color=colors)
        plt.title(f"Low: {low}, High: {high}, Pivot: {state[pivot_index]}")
        plt.pause(0.3)
        plt.clf()

    plt.show()


