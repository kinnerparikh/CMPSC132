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
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 9.78
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
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            curr = self.head
            while curr.value < value and curr.next is not self.tail:
                curr = curr.next
            if curr.next is self.tail:
                self.tail.next = Node(value)
                self.tail = self.tail.next
            elif curr is self.head:
                temp = self.head
                self.head = Node(value)
                self.head.next = temp
            else:
                temp = 
            

    def replicate(self):
        # --- YOUR CODE STARTS HERE
        pass


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        pass

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(SortedLinkedList, globals(), name='HW1',verbose=True)