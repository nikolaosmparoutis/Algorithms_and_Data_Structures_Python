# Calculate the Product sum of an given an array of integers.
# The Product sums of [x, [y,[z]],w] is x + 2 *[y + 3*[z]] + w
# the product sum of  [5, 2, [7, -1], 3, [6, [-13, 8],4]] is 5 + 2 + 2 * (7 + (- 1)) + 3 + 2*(6 + 3*(-13 + 8)+4) = 12
# of [[[[5]]]] is 2*(3*(4*(5*(5)))) = 600

def productSum(array):
    return helperProductSum(array, position=1)

# T(n) = O(n+k) where n is the len of array, k is number of subarrays
# Space = O(p) where p is num of max nested subarrays. The recoursion stores in the call stack.
def helperProductSum(array, position):
    if array is None:
        return
    sums = 0
    for i in array:
        if type(i) is str:
            return Exception
        if type(i) is not list:
            sums += i
        elif type(i) is list:
            sums += helperProductSum(i, position + 1) * (position + 1)
            position = 1
    return sums


# print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))