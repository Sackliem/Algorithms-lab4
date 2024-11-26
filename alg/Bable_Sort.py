from Visulizer.visual import *
import keyboard


def bubble_sort(arr, step):
    check = True
    step_f = 0
    n = len(arr)

    comparisons_log = []
    swaps_log = []

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons_log.append((arr[j], arr[j + 1]))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps_log.append((j, j + 1))
        if check and step == step_f:
            visualize(arr)
            step_f = 0
        if keyboard.is_pressed('esc'):
            check = False
        step_f += 1
    visualize(arr)

    show_logs(comparisons_log, swaps_log)

    return arr












