from Visulizer.visual import *
import keyboard


def partition(arr, low, high, comparisons_log, step):
    pivot = arr[high]
    i = low - 1
    check = True
    step_f = 0
    for j in range(low, high):
        comparisons_log.append((arr[j], pivot))
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if check and step == step_f:
            visualize(arr)
            step_f = 0
        step_f += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high, step):

    if low < high:
        comparisons_log = []

        pi = partition(arr, low, high, comparisons_log, step)

        quick_sort(arr, low, pi - 1, step)

        quick_sort(arr, pi + 1, high, step)

        if keyboard.is_pressed('esc'):
            check = False


def sort_with_quick_sort(arr, step):
    quick_sort(arr, 0, len(arr) - 1, step)

    visualize(arr)
