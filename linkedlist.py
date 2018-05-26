#creation of linked list

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class Single_LinkedList:
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

    #to add element in the end
    def add_at_end(self,data):
        new_data = Node(data)
        if self.headval is None:
            self.headval = new_data
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=new_data

    def add_in_between(self,data,mid_data):
        new_data = Node(data)
        if mid_data is None:
            return
        new_data.nextval = mid_data.nextval
        mid_data.nextval = new_data
    


list = Single_LinkedList()
list.headval = Node("1")
e2 = Node("2")
e3 = Node("5")

list.headval.nextval = e2
e2.nextval = e3

list.add_at_begining("6")
list.add_at_end("Thur")

list.list_print()


#using import i.e. exisitng linked list data structure from python
# pip install llist 
#from llist import dllist, dllistnode    