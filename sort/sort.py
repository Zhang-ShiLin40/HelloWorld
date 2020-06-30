import math


def bubble_sort(arr0):
    for i in range(1, len(arr0)):
        for j in range(0, len(arr0) - i):
            if arr0[j] > arr0[j + 1]:
                arr0[j], arr0[j + 1] = arr0[j + 1], arr[j]
    return arr0


def selection_sort(arr1):
    for i in range(0, len(arr1) - 1):
        minIndex = i
        for j in range(i + 1, len(arr1)):
            if arr1[j] < arr1[minIndex]:
                minIndex = j
        if i != minIndex:
            arr1[i], arr1[minIndex] = arr1[minIndex], arr1[i]
    return arr1


def insertion_sort(arr2):
    for i in range(1, len(arr2)):
        preIndex = i - 1
        current = arr2[i]
        while preIndex >= 0 and arr2[preIndex] >= current:
            arr2[preIndex + 1] = arr2[preIndex]
            preIndex -= 1
        arr2[preIndex + 1] = current
    return arr2


arr = [4, 7, 3, 0, 12, 34, 13, 25, 16, 43]

# print(bubble_sort(arr))
# print(selection_sort(arr))
print(insertion_sort(arr))
