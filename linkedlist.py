#creation of linked list

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def list_print(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval    

    def add_at_begining(self,data):
        new_data = Node(data)
        new_data.nextval = self.headval
        self.headval = new_data

    def add_at_end(self,data):
        new_data = Node(data)
        if self.headval is None:
            self.headval = new_data
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=new_data
        
    

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.add_at_begining("Sun")
list.add_at_end("Thur")

list.list_print()


#using import i.e. exisitng linked list data structure from python
# pip install llist 
#from llist import dllist, dllistnode    