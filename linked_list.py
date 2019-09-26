class Node:
    def __init__(self, data):
        self.data = data # a Node with a given data property
        self.next = None # a Node also has a .next property initialized to None

class LinkedList:
    def __init__(self):
        self.head = None # a Linked List starts with a "head" property intialized as null

    def addNode(self, data):
        new_node = Node(data) # create a new node with the given data
        new_node.next = self.head # point it's `next` to head
        self.head = new_node # set head to the newly created node
        
    def pop(self):
        prev = None
        current = self.head

        while current.next != None:
            prev = current
            current = current.next

        prev.next = None # removes the reference to the last node - thereby 'deleting' it
        return current # returns the deleted item
        
    def removeFromFront(self):
        removed_node = self.head # remove the head node from the list and return it
        self.head = self.head.next # the next node in the list is the new head node
        return removed_node
        
    def insertAt(self, X, data):
        new_node = Node(data)
        if X == 0 or self.head == None: # if adding to the head
            self.addNode(data)
            return
        prev = None
        current = self.head
        count = 0

        while current != None and count < X:
            prev = current
            current = current.next # traverse thru the linked list
            count += 1

        # If we exited the while loop - the X value is larger than the length of our llist
        # So just append to the end.
        prev.next = new_node
        new_node.next = current

    def removeAt(self, X):
        if self.head == None:
            return False
        if X == 0:
            removed_node = self.head
            self.head = self.head.next
            return removed_node

        prev = None
        current = self.head
        currentIdx = 0
        while current.next != None and currentIdx < X:
            prev = current
            current = current.next
            currentIdx += 1
        
        prev.next = current.next
        # current.next = None
        return current # return the node that has been removed
        # remove the Xth node from the list, considering 0 to be the first node
        

    def search(self, data):
        prev = None
        current = self.head
        i = 0

        # traverse the linked list
        while current != None: # searches the list for a node with the given data
            if current.data == data: #check for match
                print(f"{data} was found at 'index': {i}")
                return i # if it is found, return the "index" of the node, considering 0 to be the first node
            else: 
                i += 1
                prev = current
                current = current.next
            
        print("Your search was not found")
        return -1 # if not, return -1
        
    def print(self):
        current = self.head
        count = 1

        while current != None:
            print(f"{count}) Data: {current.data}, Memory Address: {current}")
            count += 1
            current = current.next # this is how we traverse the linked list
    
llist = LinkedList()
llist.addNode('a')
llist.addNode('b')
llist.addNode('c')
llist.addNode('dinosaur')
llist.insertAt(0, 'First!')
llist.insertAt(3, 'Middle!')
llist.insertAt(99999, 'Last!')

# llist.removeAt(0)
# llist.removeAt(1)
# llist.removeAt(8)
# llist.removeAt(999)

llist.print()