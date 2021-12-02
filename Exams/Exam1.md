# Exam 1

## Multiple Choice Questions

### Question 1

#### Which of the following statements is False?
    a) With slices, the new sequence’s elements refer to the same objects as the original sequence’s elements, rather than to separate copies. 
    b) For the list numbers = [2, 3, 5, 7, 11, 13, 17, 19], when you specify a slice and omit the starting index, 0 is assumed. So, the slice numbers[:6] is equivalent to the slice numbers[0:6]. If you omit the ending index, Python assumes the sequence’s length. 
    c) Slice operations modify the original sequence
    d) Omitting both the start and end indices on a slice copies the entire sequence. 

    Answer: c)

### Question 2

#### Which statement can be used in Python to handle some of the runtime errors in a program?
    a) a try/except statement
    b) a try statement 
    c) an exception statement 
    d) a return statement 

    Answer: a)

### Question 3

#### Which of these is not a fundamental principle of Object-Oriented Programming?
    a) Instantiation
    b) Encapsulation
    c) Polymorphism 
    d) Inheritance

    Answer: a)

### Question 4

#### Encapsulation is an object-oriented programming principle that provides:
    a) Polymorphism
    b) Information hiding
    c) Procedural Programming
    d) Inheritance

    Answer: c)
_____

## Short Answer Questions

### Question 5

#### What is the difference between is and == operators? 
    Sample Solution: 
    The is operator compares objects by memory block, while the operator == invokes the __eq__ method  in the object's class to determine if 2 objects are equal (this generally, but not always, compares objects by contents)

    My Solution: 
    The "is" operator compares the identities two objects while the "==" operator compares equality of two objects. For example, if I create a string x and assign it to "abc" and then create string y and also assign it to "abc", the equality operator will return true while the is operator will return false because the "abc" sequence is stored at two separate identities in the heap. On the other hand, if I create string x and assign it to "abc" and set y equal to x, then the is operator will return true because now y just points to the same identifier as x does, therefore it is the same object. 


### Question 6

#### Suppose that the Foo class has an attribute named items, which is a list of integers. If the Foo class has an __eq__ method defined as self.items==other.items:
#### a) what happens when the expression x==y; is evaluated for two Foo objects?
#### b) This will attempt to invoke the equality method however it will throw an AttributeError because a list does not have the attribute .items associated with it.
    Sample Solution:
    a) The expression returns True
    b) The expression raises an exception (runtime error) because a Python list does not have an attribute called items

    My Solution: 
    a) This will invoke the equality method, __eq__(), and will check if the items in the x object are equal to the items in the y object.
    b) This will attempt to invoke the equality method however it will throw an AttributeError because a list does not have the attribute .items associated with it.

### Question 7
#### How many instances can be created for an abstract class? Briefly justify your answer
    Sample Solution:
    Zero instances will be created for an abstract class. An abstract class contains methods with no implementation, so there is no point on instantiating instances of an abstract class

    My Solution: No instances can be created for an abstract class. The point of an abstract class is to create a backbone for which other objects can build off of, therefore there is no constructor for an abstract class.

### Question 8
#### What are three things you find in every recursive function?
    Sample Solution: 
    1) Base Case  (stopping condition, termination condition, etc)
    2) A way to reduce the problem into a smaller problem of the same type
    3) Function calling itself using the solution of the smaller problem to solve the original (large) problem

    My Solution:
    A base case, must change state and move towards the base case, and function must call itself recursively
----
## Coding Questions
### Question 9
#### Write the Python code for the function getEvenCount(num), where num is an integer. The function returns the number of even-valued digits in num. 0, 2, 4, 6, and 8 are even digits. You are not allowed to use str(num), lists or tuples. The argument num is guaranteed to be an integer only, so num//10 will not behave as you expect it when num is negative.  145//10 = 14 but  -145//10 returns -15. Make sure your code code handles negative numbers correctly. You cannot use recursion.
#### Examples:
```py
    getEvenCount(937825172500016) -> returns 7
    getEvenCount(11351) -> returns 0
    getEvenCount(-527888123) -> returns 5
```
Solutions:
``` py
Sample Solution: 
def getEvenCount(num): 
    num=abs(num)
    count = 0 

    while num > 0:
        digit = num % 10 
        num = num // 10 
        if (digit % 2 == 0): 
            count += 1 

    return count 

My Solution:
def getEvenCount(num):
    if num < 0:
        num = num * (-1)
    counter = 0

    while num > 0:
        if num % 2 == 0:
        counter += 1 
        num = num // 10

    return counter 
```

### Question 10
#### Write the Python code to implement the class  Shape. This class contains a constructor with two fields for storing the values of width and height of the geometric shape. It also contains the methods to provide a legible representation for its instances in the forma of 'w = {value}, h = {value}'
#### Also, wirte the code for the class Rectangle. This class is  subclass of Shape that takes the side lengths as arguments with methods that compute area and perimeter. These methods should behave like attributes when called in the interpreter, meaning they are property methods.  The perimeter of a rectangle is defined as 2*w + 2*h, and the area is defined as w*h

#### Example: 
```py
>>> x = Shape(4,5)
>>> print(x)
w = 4 , h = 5
>>> y = Rectangle(5, 3)
>>> print(y)
w = 5, h = 3
>>> y.area
15
>>> y.perimeter
16
```

Solutions:

```py
Sample Solution:
class Shape:
    def __init__(self, width, height):
            self.width = width
            self.height = height

    def __str__(self):
            return 'w = {}, h= {}'.format(self.width, self.height)

class Rectangle(Shape):
    def __init__(self,width, height):  # The constructor is not required since there is no need to override the parent's constructor
            super().__init__(width, height)

    @property
    def perimeter(self):
            return (2*self.height)+(2*self.width)

    @property
    def area(self):
            return self.height *self.width

My Solution:
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def __str__(self):
        return f'w = {self.w}, h = {self.h}'


class Rectangle(Shape):
    def __init__(self, w, h): 
        super().__init__(w, h)
    @property
    def area(self):
        return self.w * self.h
    @property
    def perimeter(self):
        return (2 * self.w) + (2 * self.h)
```


### Question 11
#### Write the implementation of the recursive function decrypt(message), where message is a string of only lower case letters. The input was previously encrypted by repeating only vowels in the message. For example, encrypting  'mouse' results in  'moouusee', encrypting  'look' results in  'looook', and so on. This function returns a new string where message is restored to its original form
#### Examples:
    decrypt('moouusee') -> return 'mouse'
    decrypt('looook') -> returns 'look'

#### You are not allowed to use for/while loops or global variables. No credit will be given if the function uses them or is not recursive. You can assume the input follows the described conditions, in other words, after each vowels comes its repetition.

Solutions: 

```py
Sample solution:
def decrypt(message):
    if len(message) == 0:
        return message

    if  message[0] in 'aeiou':
        return  message[0] + decrypt(message[2:])  # First letter is a vowel, delete the next vowel

    return  message[0] + decrypt(message[1:])  # letter is not a vowel, continue

My Solution:
def decrypt(message):
    if len(message) <= 1:
        return message

    if message[0] in 'aeiou':
        return message[0] + decrypt(message[2:])

    return message[0] + decrypt(message[1:])
```


