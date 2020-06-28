# T(n) = O(nlong+mlogm) from the two sorts | space = O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort() # does not create a copy but overwrites
    arrayTwo.sort()
    index_one = 0
    index_two = 0
    current = float("inf")
    smallest = float("inf")
    smallest_pair = []
    while index_one < len(arrayOne) and index_two < len(arrayTwo):
        first_num = arrayOne[index_one]
        second_num = arrayTwo[index_two]
        current_dif = abs(arrayOne[index_one] - arrayTwo[index_two])
        if current_dif < current:
            current = current_dif
        if arrayOne[index_one] < arrayTwo[index_two]:
            index_one += 1
        elif arrayOne[index_one] > arrayTwo[index_two]:
            index_two += 1
        else:
            return [arrayOne[index_one], arrayTwo[index_two]]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair

res1 = smallestDifference([-1, -5, 2,-10, 3, 100, 4], [1, 5, -2, 10, 3, 100,4])
res2 = smallestDifference([-1, -5, 2,-10, 3, 100, 4], [1, 5, -2, 10, -3, 102,-4])
print(res1)  #[3, 3]
print(res2)  # [-5, -4]