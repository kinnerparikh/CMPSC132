# HW5
# Due Date: 11/19/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, content):
        self.value : ContentItem = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class ContentItem:
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    def __hash__(self):
        retVal = 0
        for letter in self.header:
            retVal += ord(letter)
        
        return retVal % 3


class CacheList:
    def __init__(self, size):
        self.head : Node = None
        self.maxSize = size
        self.remainingSpace = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSpace, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        return self.numItems
    
    def put(self, content: ContentItem, evictionPolicy: str):
        if content.size > self.maxSize:
            return 'Insertion not allowed'
        if content.cid in self:
            return f'Content {content.cid} already in cache, insertion not allowed'
        
        # evicting till space becomes available
        while self.remainingSpace < content.size:
            if evictionPolicy == 'lru':
                self.lruEvict()
            elif evictionPolicy == 'mru':
                self.mruEvict()
        
        # inserting new node into list
        temp = Node(content)
        temp.next = self.head
        self.head = temp

        # adjusting fields
        self.remainingSpace -= content.size
        self.numItems += 1
        return f'INSERTED: {content}'
        

    def __contains__(self, cid):
        prev, curr = None, self.head
        # loop till end
        while curr is not None:
            if curr.value.cid == cid:
                # checking if a move is required
                if prev is not None:
                    # moving node to front of list
                    prev.next = curr.next
                    curr.next = self.head
                    self.head = curr
                return True
            prev, curr = curr, curr.next
        
        # loop ends when it reaches end of linked list
        return False


    def update(self, cid, content: ContentItem):
        if cid not in self or self.remainingSpace + self.head.value.size < content.size:
            return 'Cache miss!'

        # adjusting fields
        self.remainingSpace += self.head.value.size - content.size
        self.head.value = content
        return f'UPDATED: {content}'



    def mruEvict(self):
        # empty case
        if self.head is None:
            return
        
        # adjusting fields
        self.remainingSpace += self.head.value.size
        self.numItems -= 1

        # deleting first node
        temp = self.head
        self.head = temp.next
        temp = None


    
    def lruEvict(self):
        # empty case
        if self.head is None:
            return

        # finding the last value
        prev, curr = None, self.head
        while curr.next is not None:
            prev, curr = curr, curr.next
        
        # adjusting fields
        self.remainingSpace += curr.value.size
        self.numItems -= 1

        if prev is None:
            self.head = None
        else:
            prev.next = None

    
    def clear(self):
        while (self.head.next is not None): #traversing the list and deleting the vals
            temp = self.head.next
            self.head = None
            self.head = temp
            
        self.head = None
        self.remainingSpace = self.maxSize
        self.numItems = 0
        return 'Cleared cache!'


class Cache:
    def __init__(self):
        self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__


    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    
    def insert(self, content: ContentItem, evictionPolicy: str):
        return self.hierarchy[hash(content)].put(content, evictionPolicy)


    def __getitem__(self, content: ContentItem):
        if content.cid in self.hierarchy[hash(content)]:
            return self.hierarchy[hash(content)].head.value
        return "Cache miss!"


    def updateContent(self, content: ContentItem):
        return self.hierarchy[hash(content)].update(content.cid, content)

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(Cache, globals(), name='HW3',verbose=True)