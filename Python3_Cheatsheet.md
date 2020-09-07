#### Useful Build-in Functions
    
    1. zip

    A quick show of what it can do:

```python
a = (“John”, “Charles”)
b = (“Jenny”, “Christy”)
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x)) #print ((‘John’, ‘Jenny’), (‘Charles’, ‘Christy’))
```
    Detailed explanation is available at https://www.w3schools.com/python/ref_func_zip.asp

    2. sorted

    This is useful to sort any collection(list, dictionary). A simple example looks like:
```python
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
In addition, there is an optional parameter “key” which serves as a function that can take one input (it will be one element of the collection) and return whatever you want for sorting purpose. Certainly, I can put a lambda expression there. An example looks like:
>>> sorted([5, 2, 3, 1, 4], key=lambda x:-x)
[5, 4, 3, 2, 1]
#when 5 is used to compare, I actaully make it -5 so it will be the smallest number and hence it will be the first one.
```

    Detailed explanation is available at

    Sorting HOW TO - Python 3.8.5 documentation
    Python lists have a built-in method that modifies the list in-place. There is also a built-in function that builds a…
    docs.python.org

    3. any

    Refer to https://www.programiz.com/python-programming/methods/built-in/any:
    The any() function returns True if any element of an iterable is True. If not, any() returns False.
```python
>>> any([0,1])
True
#since 1 is True
>>> any([1,0])
True
#since 1 is True
>>> any([0,None])
False
#since not element is True
```
    4. enumerate()

    This function is pretty handy when I want to get both index and value for a list (or key and value for a dict).
```python
names    = ['ant', 'maven', 'gradle']
versions = ['1.0', '2.0', '3.0']
for i, v in enumerate(names):
    full_name = v + '-' + versions[i]
    print(full_name)

'''
Output: 
   ant-1.0   
   maven-2.0
   gradle-3.0
'''
```
    In addition, I can add an optional parameter which specifies the starting index, an example from https://book.pythontips.com/en/latest/enumerate.html looks like:
```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
```

#### Lambda Expression

Lambda expression is actaully an anonymous function. It’s pretty handy when I need a small function (one line of code) while I don’t want to take the trouble to write a formal one.
Assume I want a function that can return the value of the input integer minus 2 if input is positive, I can write:
```python
def decreaseByTwo(x):
    return x-2 if x > 0 else x
x = decreaseByTwo(x)
```
While using lambda expression, it will be
```python
decreaseByTwo = lambda x: x-2 if x > 0 else x
x = decreaseByTwo(x)
```
Lambda expression can be very useful wherever a function is needed to be a input parameter.
Detailed explanation is available at
https://www.w3schools.com/python/python_lambda.asp

#### Nested Function

Nested function is a function inside a function. It’s handy when you need to reuse a batch of codes but that reuse only make sense to your current function. At that moment, you can create a nested function inside your current function.
This is an example of a nested function. Inside parent(), a nested function child() is defined and can be invoked after its definition (but still inside parent()).

###### Introducing nonlocal

The function child() can read or assign a variable‘s value like
```python
def parent():
  a = 3
  b = 9
  def child():
    print(a) #will print 3
    print(b) #will print 9
  child()
```
However, there is a situation that child() may want to change the value of a variable that is defined in parent() like below.
```python
def parent():
  a = 3
  def child():
    print(a) #will print 3
    a = 5    
    print(a) # will print 5
  
  child()
  print(a) #will still print 3 although in child() it's set to 5
```
However, in above example, when a=5 is called, Python3 actually creates a local (only valid within child()) variable which is also named ‘a’ and shadows the external a in following executions within child(). But outside child(), a will still refer to outside one.
To ensure the ‘a’ inside child() using the outside one, I need to put “nonlocal” as below.
```python
def parent():
  a = 3
  def child():
    print(a) #will print 3
    nonlocal a
    a = 5    
    print(a) # will print 5
  
  child()
  print(a) #will print 5 since in child() it's set to 5
```
One possible confusing part is what if I want to change an outside 
dict/list/other objects inside a nest function, do I need to claim “nonlocal” first? 
The answer is not since, like child()  in below example shows, 
changing part of variable a is not a new assignment; but in child2(), 
I use “nonlocal”  to completely change outside a instead of partially.
```python
def parent():
  a = {'parent':3}
  def child():
    a['child'] = 2
    print(a) 
  def child2():
    nonlocal a
    a = {1:2}
    print(a) #will print {1:2}
  print(a) #will print {'parent':3}
  child()
  print(a) #will print {'parent':3, 'child': 2}
  child2()
  print(a) #will print {1:2}
  child()
  print(a) #will print {1:2, 'child': 2}
```

### Useful Data Structures

##### 1. Hashmap/Dictionary

In Python 3, a dict actually performs like a hashmap. A dict is composed of multiple key/value pairs in the format of key:value, a comman(,) is used to separate each pair. The dict can be initilized like
```python
a={1:2,’strKey’:’strValue’}
```
Any hashable type can be key. Please note that list (like [1,2,3,4]) and dict (like {‘1’:2}) are not hashabel.
It’s easy to add a key/value pair, just
```python
a[(1,2)]=(3,4)
```
And easy to remove a pair
```python
del a[(1,2)]
```
For time complexity, adding or removing and accessing are all O(1) operations.
Iteration of dict elements:
```python
d = {'parent':3, 'child': 4}
#access keys and then use key to access value
for key in d:
  print(key, d[key]) #each time a key/value pair of d is printed
#access key/value
for key, value in d.items():
  print(key, value) #each time a key/value pair of d is printed
#Typical incorrect ways to access key/value
for key, value in d:
  print(key, value)
for key, value in enumerate(d):
  print(key, value)
```
##### 2. Tuple
According to Python — Tuples — Tutorialspoint:

_A tuple is a collection of objects which ordered and immutable. 
Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples 
cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets._

Tuple is very handy whenI need to just 
group a series of objects, for example, 
I can use a (x,y) tuples to represent a 
two dimension point while (x,y,z) to a 
three dimension point. It looks very logically and elegant.

As mentioned above, a tuple is immutable which means it 
can not be changed once defined. Look at below example:
```python
a = (1,0)
print(a[0]) #this will print 1
a[0] = 2 #this will throw an error
```
##### 3. List/Stack
A list is a collection of objects which are NOT immutable. 
Please compare below codes to the codes in above tuple 
section and note that square brackets ‘[]’ are used here 
in list definition while parentheses ‘()’ are used in tuple 
definition.
```python
a = [1,0]
print(a[0]) #this will print 1
a[0] = 2 
print(a[0]) #this will print 2
```
Very often, list in Python3 is used as a stack. 
Data can be pushed to a stack or popped up. 
The only magic here is the first pushed data 
will be the last one to pop up 
(often referred as “first in last out” FILO). 
The next to-be-popped data stays at the top of stack. 
Normally a peek function is expected to take a look 
at the data at the top of stack without actually 
popping it up. Look at this example to get more 
understanding:
```python
s = []
s.append(1) #here I use append to serve as push
print(s) #this will print [1]
s.append(2) #now s becomes [1,2]
s.append(3) #now s becomes [1,2,3]
a = s.pop()
print(a)  # it will print 3, which last in but first out
print(s)  # since 3 is popped, s is [1,2]
s.append(3) #now s becomes [1,2,3] again
print(s[-1]) # print 3, s[-1] is equal to peek
print(s)  # print [1,2,3], peek(unlike pop) will not change a stack
```
