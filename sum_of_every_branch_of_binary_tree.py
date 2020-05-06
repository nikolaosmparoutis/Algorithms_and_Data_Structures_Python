'''Problem: Write a function that takes in a Binary Tree and returns a list of its branch
sums ordered from leftmost branch sum to rightmost branch sum.
A branch sum is the sum of all values in a Binary Tree branch. A Binary
Tree branch is a path of nodes in a tree that starts at the root node and ends 
at any leaf node"
'''

'''Method:
Using Depth first search i traverse the tree, the preorder 
is the desired method because it traverses 
the root or parent node -> left -> right  
In contrast inorder and postorder start from the leafs.

** Time complexity:

T(n) = 2*T(n/2) + f(1) = O(n) + O(1) = O(n) where n = number of nodes
	T(n/2) = each subproblem size (left and right subtree) 
	O(1) for other operations no participating in the recursion: 
	like comparison between left,right,parent and other operations like printing.
	
** Space complexity:  
	
	AVG:
	  2^0 = 1 Total nodes = 1
	+ 2^1 = 2 Total nodes = 3
	+ 2^2 = 4 Total nodes = 7
	+ 2^3 = 8 Total nodes = 15

	--log each side to get the depth_levels
	log_2(2^(depth_levels)) = log_2(Total nodes)
	=>  depth_levels = log_2(total nodes) = log_2(15) = 3.9
	
	Space = O(2^depth_levels) = O(2^4) = O(16) = O(n-1)
	 
	Worst case where the tree is flattened to a list: 
	O(n), n= number of node m = number of edges or keys.
'''
# Delete the prints for better code readability, they stayed for the grasp of the concept and future reusability

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums_ls = []
    branchSumsHelper(root, 0, sums_ls)
    return print("final array sums_ls:", sums_ls)


def branchSumsHelper(node, currentSum, sums_ls):
    print("node=", node)
    if node is None:
        print("node is None")
        return

    newCurrentSum = node.value + currentSum
    print("node.value=", node.value)
    print("currentSum=", currentSum)
    print("newCurrentSum=", newCurrentSum)
    if node.left is None and node.right is None:
        print('leaf->', node.value)
        sums_ls.append(newCurrentSum)
        print('sums_ls :', sums_ls)
    print('node.value=', node.value)
    print("node.left=", node.left)
    print("node.right=", node.right)
    preorder(node, newCurrentSum, sums_ls)

# *Import*:
# Recursion creates Subroutines and this stores EVERY variable's state in stack frame, so in every node the currentSum is saved.
def preorder(node, newCurrentSum, sums_ls):
    branchSumsHelper(node.left, newCurrentSum, sums_ls)
    print("i turn right...")
    branchSumsHelper(node.right, newCurrentSum, sums_ls)
    return

branchSums(tree)
