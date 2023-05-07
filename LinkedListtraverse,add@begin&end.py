class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head=self.head.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            while self.head is not None:
                self.head=self.head.ref
            self.head.ref=new_node
ll1=LinkedList()
ll1.add_end(334)
ll1.add_begin(43)


ll1.print_ll()