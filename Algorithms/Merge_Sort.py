def sort(arr):
    yield from __merge_sort(arr, 0, len(arr) - 1)


def __merge_sort(arr, start, end):
    if end <= start:
        return

    middle = start + ((end - start + 1) // 2) - 1
    yield from __merge_sort(arr, start, middle)
    yield from __merge_sort(arr, middle + 1, end)
    yield from __merge(arr, start, middle, end)
    yield arr


def __merge(arr, start, mid, end):
    right_index = mid + 1
    left_index = start
    merged = []

    while left_index <= mid and right_index <= end:
        if arr[left_index] < arr[right_index]:
            merged.append(arr[left_index])
            left_index += 1
        else:
            merged.append(arr[right_index])
            right_index += 1

    while left_index <= mid:
        merged.append(arr[left_index])
        left_index += 1

    while right_index <= end:
        merged.append(arr[right_index])
        right_index += 1

    for i, val in enumerate(merged):
        arr[start + i] = val
        yield arr
