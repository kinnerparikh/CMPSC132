# LAB2
# Due Date: 09/17/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''


    def __init__(self):
        self.items = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.balance = 0

    def purchase(self, item, qty=1):
        if item not in self.items.keys():
            return 'Invalid item'
        
        if not self.isStocked:
            return 'Machine out of stock'
        
        currentStock = self.items[item][1]
        if currentStock == 0:
            return 'Item out of stock'
        
        if currentStock < qty:
            return f"Current {item} stock: {currentStock}, try again"
        
        totalPrice = qty * self.items[item][0]
        if totalPrice > self.balance:
            return f"Please deposit ${totalPrice - self.balance}"

        self.items[item][1] -= qty
        change = self.balance - totalPrice
        self.balance = 0
        if change == 0:
            return "Item dispensed"

        if change > 0:
            return f"Item dispensed, take your ${change} back"    

    def deposit(self, amount):
        if self.isStocked:
            self.balance += amount
            return f"Balance: ${self.balance}"
        
        return f"Machine out of stock. Take your ${amount} back"


    def _restock(self, item, stock):
        if item not in self.items.keys():
            return "Invalid item"
        self.items[item][1] += stock
        return f"Current item stock: {self.items[item][1]}"

    @property
    def isStocked(self):
        for x in self.items.values():
            if x[1] != 0:
                return True
        
        return False

    @property
    def getStock(self):
        return self.items

    def cancelTransaction(self):
        if self.balance == 0:
            return None
        
        remaining = self.balance
        self.balance = 0
        return f"Take your ${remaining} back"

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        return (self.x == o.x) and (self.y == o.y)

    def __mul__(self, val):
        return Point2D(self.x * val, self.y * val)

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    #--- YOUR CODE STARTS HERE
    def getDistance(self):
        xComponent = self.point2.x - self.point1.x
        yComponent = self.point2.y - self.point1.y
        x = round((xComponent**2 + yComponent**2)**0.5, 3)       
        return x
    
    #--- YOUR CODE STARTS HERE
    def getSlope(self):
        xComponent = self.point2.x - self.point1.x
        yComponent = self.point2.y - self.point2.y
        if xComponent == 0:
            return math.inf
        
        x = round(yComponent/xComponent, 3)
        return x


    #--- YOUR CODE CONTINUES HERE
    def __str__(self) -> str:
        if math.isinf(self.getSlope()):
            return "Undefined"

        yIntercept = self.point1.y - self.getSlope()*self.point1.x
        
        if self.getSlope() == 0:
            return f"y = {yIntercept}"
        
        return f"y = {self.getSlope()}x + {yIntercept}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Line):
            return False
        return self.point1 == o.point1 and self.point2 == o.point2
    
    def __mul__(self, value):
        if not isinstance(value, int):
            return None
        
        return Line(self.point1 * value, self.point2 * value)
    
    def __rmul__(self, value):
        return self.__mul__(self, value)


if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(VendingMachine, globals(), name='HW1',verbose=True)
'''john_vendor = Vendor('John Doe')
west_machine = john_vendor.install()
print(west_machine.getStock)'''