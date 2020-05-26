# Implemetation of Double Linked List class:
# Insertions at the Head or Tail, specifc Position, Before or After a node, Removal of a given node,
# Search of node with value, Display, Menu of commands with a small error handling.
# the comments are just in case i may forget something in the future.  

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and position != currentPosition:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # important! Double linked listgs are prone to errors. The position of each line is important for bindings and releases
    # first we link the new node then we will detach the old bindings.
    def insertBefore(self, node, new_node):
        if new_node == self.head and new_node == self.tail:
            return
        self.remove(new_node)
        if node.prev is None:       # check if we go to insert at the header node
            self.head = new_node    # undate header first
            new_node.next = node
            node.prev = new_node    # then point prev node to point to the new.
        else:
            new_node.next = node
            new_node.prev = node.prev
            node.prev = new_node    # Set the binding of next node after new_node to look point to the new node.
            new_node.prev.next = new_node   # Firstly the new node is not the header. Grab the pointer gtom the prv node to point to the new node.
        return

    def insertAfter(self, node, new_node):
        if new_node == self.head and new_node == self.tail:
            return
        self.remove(new_node)
        if node.next is None:       # check if we go to insert at the tail
            self.tail = new_node    # update tail first
            new_node.prev = node
            node.next = new_node
        else:
            new_node.prev = node
            new_node.next = node.next
            new_node.next.prev = new_node   # Firstly the new node is not the header. Grab the pointer gtom the prv node to point to the new node.
            node.next = new_node    # Set the binnding of next node after newnode to look point to the new node.


    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node # does not work without this.Why ?  Because remove will not find the current node but the next node.
            node = node.next # if we move this after remove() is wrong.Why ? Because we will loose pointers from/to the neightbor nodes.
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
        # Nasty mistakes to avoid:
        # while node is not None:
        #     if node.value == value:
        #         self.remove(nodeToRemove)
        #         node = node.next

    def containsNodeWithValue(self, value):
            node_position = 0
            node = self.head
            while node is not None and node.value != value:
                node = node.next
                node_position += 1
            if node is not None:
                return node_position
            else:
                return None

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.helperRemoveBindings(node)
        return

    def helperRemoveBindings(self, node):
        if node.prev is None:
            node.next = None
            return
        if node.next is None:
            node.prev = None
            return
        # set the bindings.
        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -- ')
            current = current.next


def menu(a_dllist):
    while True:
        try :
            print('The list: ', end='')
            a_dllist.display()
            print()
            do = input('What would you like to do? ').split()

            operation = do[0].strip().lower()
            if operation == 'insert':
                data = int(do[1])
                position = do[3].strip().lower()
                new_node = Node(data)
                suboperation = do[2].strip().lower()
                if suboperation == 'at':
                    if position == 'beg':
                        a_dllist.setHead(new_node)
                    elif position == 'end':
                        a_dllist.setTail(new_node)
                    elif position == 'pos':
                        position_node = do[3].strip().lower()
                        a_dllist.insertAtPosition(position_node,new_node)
                else:
                    index = int(position)
                    ref_node = a_dllist.get_node(index)
                    if ref_node is None:
                        print('No such index.')
                        continue
                    if suboperation == 'after':
                        a_dllist.insertAfter(ref_node, new_node)
                    elif suboperation == 'before':
                        a_dllist.insertBefore(ref_node, new_node)

            elif operation == 'remove':
                if len(do) == 3 :
                    print("len = ", len(do))
                    suboperation = do[2].split()
                    if suboperation[0] == 'value':
                        data = int(do[1])
                        print("data = ", data)
                        a_dllist.removeNodesWithValue(data)

            elif operation == 'search':
                data = int(do[1])
                status = a_dllist.containsNodeWithValue(data)
                if status is not None:
                    print('Value is at position:', status)
                else:
                    print('The value is not in the list.')

            elif operation == 'quit':
                break

            else:
                index = int(do[1])
                node = a_dllist.get_node(index)
                if node is None:
                    print('No such index.')
                    continue
                a_dllist.remove(node)
        except IndexError or ValueError:
            print('Wrong command. Follow the menu\'s commands.')
            break


if __name__ == '__main__':
    a_dllist = DoublyLinkedList()

    print('-- Menu of commands--')
    print('insert <value> after <index>')
    print('insert <value> before <index>')
    print('insert <value> at pos <position>')
    print('insert <value> at beg')
    print('insert <value> at end')
    print('remove <index>')
    print('remove <value> value')
    print('search <value>')
    print('quit')
    print('----')

    menu(a_dllist)
