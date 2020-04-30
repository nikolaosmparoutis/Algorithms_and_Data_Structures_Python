# Find a pair, assume there is at most one pair which has sum equals to targetSum 

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
hash_map = {}

def twoNumberSum(array, targetSum):
	for x in array:
		y = targetSum - x
		if y in hash_map:
			return [x, y] 
		else:
            hash_map[x] = 'T'
	return []


print(twoNumberSum(array, targetSum))

# (O(n) from the list traverse "for x in array:" + O(1) from "if y in hash_map:"
# T(n) = O(n) + O(1) = O(n)  
# Space = O(2n)


'''
Attention: The below solution does not take advantage the use of hash maps in O(1) 
because we made a nasty mistake, used hash_map.values() but this is O(n).
Instead we use hash_map storing the values as keys.
Be aware that even the dict.keys() is O(n) it generates a list and then iterates over it.
TODO a check in "Time Complexities of the Dictionary’s Functions": 
https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_II_Dictionaries.html

T(n) = O(n^2) where n = array_length
Space = O(2n)
'''
# digits_return = []
# def twoNumberSum(array, targetSum):
# 	for x in range(0, len(array)):
# 		y = targetSum - array[x]
# 		if y in hash_map.values():
# 			digits_return.append(array[x])
# 			digits_return.append(y)
# 		else:
#             hash_map[x] = array[x]
# 	return digits_return
