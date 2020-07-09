# Implementation of breadth first search using queue. Add children then BFS the tree
# from left to right. Input an empty array where the return from the BFS will fill it with the nodes.

# T=O(V+E) traverse the nodes + for each node traverse its edges(children),
# space O(V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self # return reference to the instance object it was called(the class object).Used for chaining in unittest.

    def breadthFirstSearch(self, array):
        queue = [self]  # reference of the instance object of the class, Node(name)
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        print(array)
        return array

