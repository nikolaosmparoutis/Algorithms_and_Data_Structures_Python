# I found an elegant way to bypass the time O(N^2) or O(N) in
# T(n) = O(n/2) | space O(1)
# using the symmetry to search on the half of the input

# Remember that len and range need a marriage in types and
# string slicing starts from 0 indexing while len do not.

def isPalindrome(string):
    lenStr = int(len(string))
    # fundamental checks on string
    if lenStr == 1:
        return True
    if lenStr == 0:
        return False

    for i in range(0, (lenStr // 2)):  # // is the lower floor division
        if string[i] == string[lenStr - 1 - i]:
            continue
        else:
            return False
    return True
