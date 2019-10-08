def sort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A) - 1):
            for j in range(len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    A[j+1], A[j] = A[j], A[j+1]
                    swapped = True
                yield A
