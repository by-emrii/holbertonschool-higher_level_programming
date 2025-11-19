# Python Objects: Memory, Mutibility and how Python handles Variables

## Introduction
Python hides many low-level details, but understanding how it manages objects, memory, and variable references can make you a stronger programmer. This post explores key concepts such as object identity, type, mutability, and how Python handles variable assignment and function arguments.

## ID and Type
Every object in Python has an identity and a type. The identity is a unique identifier you can see with `id()`, essentially pointing to the object’s location in memory. The type, returned by `type()`, tells you what kind of object you’re dealing with.

```python
x = 42 
print(id(x)) # Returns the unique identifier of the object in memory 
print(type(x)) # Output: <class 'int'>
```

## Mutable Objects
Mutable objects are objects whose content can be changed without creating a new object. Lists, dictionaries, sets, and byte arrays are common examples. Changes to a mutable object through one variable are visible to all aliases.
```python
a = [1, 2, 3] 
b = a # b points to the same list of a
b.append(4) 
print(a) # Output: [1, 2, 3, 4] 
print(id(a) == id(b)) # True, same object in memory
```

## Immutable Objects
Immutable objects cannot be changed once created. Numbers, strings, tuples, frozen sets, and bytes fall into this category. Any “modification” actually creates a new object.
```bash
x = 100 
y = x 
y += 1 # creates a new int object for y 
print(x) # 100 
print(y) # 101 
print(id(x), id(y)) # different IDs
```

## Why It Matters: Mutable vs Immutable
Python treats mutable and immutable objects differently. Assigning a new variable to an immutable object just points it to the same object, but “modifying” it creates a new object. Mutable objects can be updated in place.

**Mutable example**
```python
list = [1, 2] 
list2 = list 
list2.append(3) 
print(list) # [1, 2, 3] - changed in place
```

**Immutable examples**
```python
s = "hello" 
s2 = s 
s2 += " world" 
print(s) # "hello" - original string unchanged 
print(s2) # "hello world"
```

## Function Arguments and Object Behaviour
Python passes arguments by assignment, meaning the function receives a reference to the object. Mutables can be changed inside the function, immutables cannot.
```python
def add_item(my_list): 
    my_list.append(4) 

nums = [1, 2, 3] 
add_item(nums) 
print(nums) # [1, 2, 3, 4] - changed inside function 
    
def increment(n): 
    n += 1 
    return n 

x = 5 
y = increment(x) 
print(x) # 5 - unchanged 
print(y) # 6 - new object
```

## Integer Pre-allocation
Python pre-creates integers from -5 to 256 (`NSMALLNEGINTS` and `NSMALLPOSINTS`) for efficiency. Frequently used small numbers are reused rather than recreated.

```python
a = 100 
b = 100 
print(a is b) # True - same pre-allocated object

c = 1000 
d = 1000 
print(c is d) # False - new objects created
```

## Tuples and Frozen Sets: Special Case
Even though tuples and frozen sets are immutable, they can contain mutable objects. Modifying the inner object does not change the tuple itself.

```python
t = ([1, 2], 3) # tuple containing a list 
t[0].append(3) 
print(t) # ([1, 2, 3], 3) - tuple unchanged, inner list modified
```

## Assignment vs Referencing
Assigning one variable to another does not copy the object; it just creates another reference to the same object.
```python
a = [1, 2] 
b = a 
b.append(3) 
print(a) # [1, 2, 3] - same object 

x = 50 
y = x 
y += 10 
print(x) # 50 - original int unchanged 
print(y) # 60 - new object created
```
