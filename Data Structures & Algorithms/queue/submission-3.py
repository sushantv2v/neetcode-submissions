class Node:

    def __init__(self,value):

        self.value = value
        self.next = None
        self.prev = None 

class Deque:
    
    def __init__(self):

        self.head   = None
        self.tail = None
        self.length = 0


    def isEmpty(self) -> bool:

        if self.length ==0:
            return True
        return False    
        

    def append(self, value: int) -> None:

        new_node = Node(value)

        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            

        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length +=1     

        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)


        if self.length ==0:
            self.head = new_node
            self.tail = new_node 

        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node



        self.length +=1    
        

    def pop(self) -> int:


        if self.length ==0:
            return -1

        popped = self.tail
        val = popped.value
        if self.length ==1:

            self.head = None
            self.tail = None

            self.length -=1    

        else:

            self.tail = popped.prev
            self.tail.next = None
            popped.prev = None

            self.length -=1 

        return val
             
        

    def popleft(self) -> int:

        if self.length ==0:
            return -1
        
        popped = self.head 
        val = popped.value
        if self.length ==1:

            self.head = None
            self.tail = None

            self.length -=1

        else:


            self.head = popped.next
            self.head.prev = None
            
            self.length -=1
        
        return val
