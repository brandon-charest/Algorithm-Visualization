def sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1]
            position -= 1
            yield arr

        arr[position] = current
        yield arr
    yield arr
