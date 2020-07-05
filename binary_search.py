# T(n)= O(logN) we cut in half the array after each iteration,space O(1)
def binarySearch(array, target):
    leftPtr = 0
    rightPtr = len(array) - 1

    while leftPtr <= rightPtr:
        middlePtr = (leftPtr + rightPtr) // 2
        if array[middlePtr] < target:
            leftPtr = middlePtr + 1
        elif array[middlePtr] > target:
            rightPtr = middlePtr - 1
        else:
            return middlePtr
    return -1
