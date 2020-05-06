# Problem: Given a target integer find the closest number in the BST

# pip install binarytree
from binarytree import bst

target = 10
closest = float("inf")
tree = bst()        #generates random binary trees
print(" -generate a random tree from python lib -")
print(tree)

# Solution 1
# On Average: time O(logn), space O(1)
# Worst Case: time O(n), soace O(n)
def findClosestValueInBst(tree, target, closest):
    while tree is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        elif target > tree.value:
            tree = tree.right
        else:
            break
    return closest


print(findClosestValueInBst(tree, target, closest))

# Solution 2
# On AVG case:T(n) = O(logn), Space: O(logn) due to recursion calling the call stack O(logn) times to use the stack frames of the subroutines.
# On worst Case:  T(n) = O(n) , Space: O(n) due to falling into a linear list.
def findClosestValueInBst(tree, target, closest):
     if tree is None:
        return closest
     if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
     if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
     elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
     else:
        return closest

print(findClosestValueInBst(tree, target, closest))
