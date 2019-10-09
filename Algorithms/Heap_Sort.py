def sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        yield from __heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        yield from __heapify(arr, 0, i)


def __heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        yield from __heapify(arr, largest, heap_size)
    yield arr




