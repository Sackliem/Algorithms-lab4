from Visulizer.visual import *
import keyboard


def selection_sort(arr, step):
    check = True
    step_f = 0
    n = len(arr)

    comparisons_log = []
    swaps_log = []

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons_log.append((arr[min_idx], arr[j]))
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps_log.append((i, min_idx))

        if check and step == step_f:
            visualize(arr)
            step_f = 0

        if keyboard.is_pressed('esc'):
            check = False

        step_f += 1

    visualize(arr)

    show_logs(comparisons_log, swaps_log)

    return arr


