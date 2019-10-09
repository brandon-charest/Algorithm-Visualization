def sort(arr):
    yield from __quicksort(arr, 0, len(arr) - 1)


def __quicksort(arr, begin, end):
    if begin >= end:
        return
    pivot = __partition(arr, begin, end)
    yield from __quicksort(arr, begin, pivot - 1)
    yield from __quicksort(arr, pivot + 1, end)
    yield arr


def __partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end +1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot
