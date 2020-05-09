
'''	Question:
	Implement the depthFirstSearch method, which takes and empty array, 
	stores all the nodes and returns it. 
'''
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array

'''
* Time complexity:
Main idea is that Depth first search is based on the adjecenchy list which in Python is a dictionary
of linked lists.

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
    A
   / \
  B   C
 / \   \
D   E - F

Vetices = the keys in the dictionary 
Edges  = the nodes in these lists.

T(n) = O(V+E) but lets analyze it why 

The keys are : A,B,C,D,E,F where each one has a list.

For every list we traverse all the nodes and this creates subroutines in each recursion.
Each recursion creates a new stack frame. On top of the stack we have the return address from the
last called subroutine.
When we are at D vertex has no children 
the last subroutine in call stack is the parent of the D node, B, hop back to B subroutine.
'E' is not visited so it hops on node 'E',
from 'E' to 'F' F has no children so returns to Subrouitines from B, B cleaned and returns to its parent A for the 'C' key.
and so on and so forth.
So the subroutines are V and each one hops back x number of times were in total are E.
So T(n) = O(V+E)


* Space complexity:
On a AVG case
	Every subrouitne is an *object* 
	The adjecency list creates 3 heap frames one per sublist and all of them belong at the same hashtable.
	O(height) = O(3)
	
	In the worst case if a tree falls to a list is O(V).
	Vertice A cannot not resolve until every vertex resolved.
	O(6) = O(V)  same a Bredth First Search
	We also has + O(V) for the array to store the nodes.
	So is O(2V) ~= O(V)

Useful sources
https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
https://www.shmoop.com/computer-science/lists/call-stack.html
'''
