###Exercises: Predict the output of this code without using 
###           the Python interpreter

### --1--
alist = []
for i in list(range(22, 36, 2)):
    alist.append(i)
print(sum(alist))


### --2--
for i in range(10):
    if i%2==1:  
        continue    
    else:
        print(i)

### --3--
for i in range(10):
    if i%2==1:  
        break    
    else:
    	print(i)

### --4--
i = j = 0
while i<=10:
    while j<=i:
        print("i: ", i, " j: ", j)
        j += 1
    i, j = i+1, 0
### Question: Modify the above program so that it terminates
#       right after printing j=5 and i=3,
#       by just changing the inner while loop

### --5--
MyList = [1, 2, 3, 4, 5]
for i in range(10):
    try:
        print(MyList[i])   
    except IndexError: 
        print("Index Error with i=", i)
# You can remove "IndexError" to handle any Python exception


### --6--

s = "0123456789"
print(s[2:6])
print(s[2:6:2])
print(s[::2])
print(s[::-1])

### --7--

l = [0,1,2,3,4,5,6,7,8,9]
print(l[2:6])
print(list(range(2, 6)))



### List methods
### Visit https://www.programiz.com/python-programming/methods/list for more methods
#### list.append, remove, reverse and sort are procedural methods, 
#    which means they don't return anything but change the list itself


### --8--
l = [1,2,3]+ 2*[4,5]
l = [1,2,3]+ 2**2*[4,5]
print(l)
l = [1,2,3]
l.append(4)
l.pop()
l.pop()
l += [10,11,12,13,14] 
l.insert(2, "a")
l.remove(12)
print(l)



### String methods
### Visit https://www.programiz.com/python-programming/methods/string for more methods

### String methods are mainly functional, which means the method 
##  returns something (a list for example)

### --9--
print("123" + 2**2*"45")

### --10--
s = "\n \t     Course Schedule \n\n"
s = s.strip()  
print(s)    

### --11--
s = '''This course is CMPSC132
    using Python
    and a text editor
'''
l = s.splitlines() 
print(l, len(l), len(s))    
for i in range(len(l)):
    print(i, ":", l[i])  
# What if you do print(i, ":", l[i].strip())? 


### --12--
s = "blue, red, green"
l = s.split(",") 
print(l)

l = list(s) 
print(l)

s2 = "".join(l) # what if s2 = ";".join(l)?
print(s2)


x = s.find("r")     
y = s.find("r", 7)  
print(x, y)


print(s.replace("r", "R"))