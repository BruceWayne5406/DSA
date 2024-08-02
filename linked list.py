#linked list is a data structure that wraps the data stored in it in the form of a node.
#each node in the linked list contains some data, and reference or knowledge of the data in the next node.
#the initial element in the linked list is commonly known as the head

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head = Node()
    
    def append(self,data):
        new_node=Node(data)
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_node
    
    def length(self):
        current=self.head
        total=0
        while current.next!=None:
            total+=1
            current=current.next
            return total
    
    def display(self):
        elements=[]
        current=Node()
        while current!=None:
            current=current.next
        print(elements.append(current.data))


    def get(self,index):
        current=self.head
        cur_index=0
        if index>=self.length:
            print("ERROR")
        
        while True:
            current=current.next
            if cur_index==index:
                return current.data
            cur_index+=1





my_list=linked_list()
my_list.display()

my_list.append(1)
my_list.append(2)

my_list.display()