#Lab #7
#Due Date: 11/12/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        return self._heap[0]
    
    def _parent(self,index):
        targetIndex = (index // 2) - 1 # index of parent
        # negative index case
        if targetIndex < 0:
            return None
        # takes care of IndexOutOfBounds
        try:
            return self._heap[targetIndex]
        except Exception:
            return None

    def _leftChild(self,index):
        try:
            return self._heap[(index * 2) - 1]
        except Exception:
            return None


    def _rightChild(self,index):
        try:
            return self._heap[index * 2]
        except Exception:
            return None


    def insert(self,item):
        self._heap.append(item)
        currIndex = len(self)
        # percolation up
        while (currIndex > 1 and self._parent(currIndex) > item):
            # target in heap index
            target = (currIndex // 2)
            
            # swap places
            self._heap[currIndex - 1] = self._heap[target - 1] 
            self._heap[target - 1] = item

            currIndex = target
            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            retVal = self._heap[0]
            temp = self._heap.pop(len(self) - 1)
            self._heap[0] = temp
            tempIndex = 1 #heap index
            left, right = self._leftChild(tempIndex), self._rightChild(tempIndex)

            # looping until desired place, percolate down
            while (left is not None and right is not None and (temp > left or temp > right)):
                newIndex = tempIndex * 2
                # move to the right
                if left > right:
                    newIndex += 1
                
                self._swap(newIndex - 1, tempIndex - 1)
                tempIndex = newIndex
                left, right = self._leftChild(tempIndex), self._rightChild(tempIndex)
            
            # one last swap if right is None and left is greater than temp
            if left is not None and temp > left:
                self._swap(tempIndex - 1, (tempIndex * 2) - 1)
        return retVal
    
    def _swap(self, index1, index2):
        temp = self._heap[index1]
        self._heap[index1] = self._heap[index2]
        self._heap[index2] = temp
        

def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    # YOUR CODE STARTS HERE
    heap = MinBinaryHeap()

    # add nums to heap
    for num in numList:
        heap.insert(num)
    
    retList = []
    # pop off heap, loop till heap is empty
    for _ in range(len(heap)):
        retList.append(heap.deleteMin())
    
    return retList