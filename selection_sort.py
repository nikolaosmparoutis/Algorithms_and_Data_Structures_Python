# Selection Sort algorithm
# time complexity O(n^2), space O(n).
# Suitable for cases when the memory writes
# is much more important than the speed
def selectionSort(array):
    for i in range(0, len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j # update the index pointing the min element
        array[i], array[min_idx] = array[min_idx], array[i]
    return (array)
