#Problem: Sort with bubblesort an array.
#This is a slow sorting algorithm of O(n^2) but without breaking its logic try to improve it. 

def bubbleSort(array):
	count = 0
    isSorted = False
	if len(array) <= 1:
		return array
    while isSorted is False:
        i = 0
        limit_array = len(array) - 1 - count
        for i in range (limit_array):
            if (array[i] > array[i+1]):
                tmp1 = array[i]
                tmp2 = array[i+1]
                array[i+1] = tmp1
                array[i] = tmp2
                isSorted = False
            else:
                i += 1
        count += 1
        if (limit_array == 1):
            isSorted = True
    return array

print(bubbleSort([2, 9, 5, 6, 3]))

'''
* Time Complexity:

T(n) = O( (n^2)-(n+1)/2 ) < O(n^2).  
where (n+1)/2 is the median value of an increasing or decreasing sequence  

Example of the algorithm

[9, 5, 6, 3] initial
[5, 9, 6, 3] swap
[5, 6, 9, 3] swap
[5, 6, 3, |9] last swap. Now every num before 9 is smaller so we decrease the search limit by 1
[5,3,|6,9] every num before 6 is smaller so we decrease the search limit by 1
[3,|5,6,9]

* Space = O(n), for the array

'''