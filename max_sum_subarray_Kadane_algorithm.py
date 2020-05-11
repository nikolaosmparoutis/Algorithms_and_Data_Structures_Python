'''
Dynamic Programming problem of Kadane's solution
in O(n) for the "find the max subsequence which has the max sum".
Applied in business analytics to find period with max profit or the min profit.
and it's value.
'''

def kadanesAlgorithm(array):
    maxEndingHere, maxSoFar = array[0], array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[i], array[i])
        maxSoFar = max(maxEndingHere, maxSoFar)
    print("max sum = ", maxSoFar)
    return maxSoFar


kadanesAlgorithm([5, 10, -10, 5, 10, -100, -3, 10, 15, -2, 1])

# max sum = 25

#T(n) = O(n)
#Space = O(1)
