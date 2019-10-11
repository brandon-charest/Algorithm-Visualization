def sort(arr):
    def swap(a,b):
        arr[a], arr[b] = arr[b], arr[a]

    upper = len(arr) - 1
    lower = 0
    swapped = False

    while not swapped and upper - lower > 1:
        swapped = True

        for j in range(lower, upper):
            if arr[j + 1] < arr[j]:
                swap(j + 1, j)
                swapped = False
                yield arr
        upper = upper - 1

        for j in range(upper, lower, -1):
            if arr[j - 1] > arr[j]:
                swap(j - 1, j)
                swapped = False
                yield arr
        lower = lower + 1

    yield arr
