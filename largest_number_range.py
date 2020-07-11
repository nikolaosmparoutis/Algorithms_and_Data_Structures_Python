# example:
# [-3,-2, 5, 6, 7, -4, -5, 14, 13, 15 ] the first largest existing range of numbers
# is [-5, -3] = [-5,-4,-3,-2] .The other two ranges have three numbers [5,6,7], [13, 14, 15]

# The profound easy solution is sorting, takes O(NlogN),
# although using hashmap it takes T(n) = O(N), space O(N)

def largestRange(array):
    bestRange = []
    hashMap = {}
    longestLen = 0
    # initialize hashmap. Non visited keys in the array have not traversed from the array.
    # Non visited initialised and marked as False
    # Visited assigned to True to avoid to repeat a number in array we  already have in a list.
    for i in array:
        hashMap[i] = False
    for num in array:
        if hashMap[num] is True:
            continue
        hashMap[num] = True
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in hashMap:
            hashMap[left] = True
            left -= 1
            currentLength += 1
        while right in hashMap:
            hashMap[right] = True
            right += 1
            currentLength += 1
        if currentLength > longestLen:
            longestLen = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange

