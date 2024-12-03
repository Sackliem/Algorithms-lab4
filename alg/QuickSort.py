from Visulizer.visual import *
import keyboard


def quicksort(arr,step):
    low = 0
    high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high,step)

        quicksort(arr, low, pi - 1,step)
        quicksort(arr, pi + 1, high,step)
    return [arr,pi]

def partition(arr, low, high,step):
    pivot = arr[high]
    check = True
    step_f = 0
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if check and step == step_f:
            visualize_q(arr, high, j)
            step_f = 0
        if keyboard.is_pressed('esc'):
            check = False
        step_f += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualize_q(arr, high, i + 1)  # Визуализация размещения опорного элемента
    return i + 1
