# LAB4
# Due Date: 10/08/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None 

    def __len__(self):
        count=0
        current=self.head
        while current: #loop until current is None
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        newNode = Node(value)
        if self.head is None: #empty linked list
            self.head = newNode
            self.tail = newNode
        elif value <= self.head.value: #value is less than head value
            newNode.next = self.head
            self.head = newNode
        elif value >= self.tail.value: #value is greater than tail value
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            curr = self.head
            while curr.next is not None and curr.next.value <= value: #loop until appropriate   
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
            

    def replicate(self):
        newList = SortedLinkedList() #create a new list
        if self.head is None: #empty list condition
            return None
        curr = self.head
        while curr is not None: #looping till end of list
            repeat = curr.value
            if isinstance(curr.value, float) or curr.value <= 0: #float or negative case
                repeat = 2
            for i in range(0, repeat):
                newList.add(curr.value) #adding to new list
            curr = curr.next
        
        return newList


    def removeDuplicates(self):
        curr = self.head
        while curr is not None: #looping till end of list
            while curr.next is not None and curr.value == curr.next.value: #removing duplicates
                curr.next = curr.next.next
            curr = curr.next

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(SortedLinkedList, globals(), name='HW1',verbose=True)