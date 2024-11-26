from Visulizer.visual import *
import keyboard


def heapify(arr, n, i, comparisons_log, swaps_log):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons_log.append((arr[largest], arr[left]))
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparisons_log.append((arr[largest], arr[right]))
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swaps_log.append((i, largest))

        heapify(arr, n, largest, comparisons_log, swaps_log)


def heap_sort(arr, step):
    check = True
    step_f = 0
    n = len(arr)

    comparisons_log = []
    swaps_log = []

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, comparisons_log, swaps_log)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swaps_log.append((0, i))

        heapify(arr, i, 0, comparisons_log, swaps_log)

        if check and step == step_f:
            visualize(arr)
            step_f = 0

        if keyboard.is_pressed('esc'):
            check = False

        step_f += 1

    visualize(arr)

    show_logs(comparisons_log, swaps_log)

    return arr