# Control Flow
- if, else, elif
- for loops
- while loops

## Conditional Statements
Use conditionals to run code you only want to execute under certain conditions. They are used to control the flow of your programme.
```python
age = 15 # if the user is above the age of 15 allow them to buy a ticket

if age > 15:
    print("You purchased a ticket!")
elif age <= 15:
    print("You're too young to buy a ticket.")
else:
    print("Something went wrong...") # this will execute if none of the other conditions are met

```
Outputs ``You're too young to buy a ticket.``

## Loops!
Loops are used to reduce the amount of code one needs to write. Let's say you have a list of 100 you want to print the names of. Without a loop, that would need 100 ``print()`` statements!  
With loops, you only need one.  
Example:
```python
shopping_list = ["bread", "eggs", "milk", "orange"]

# This is tedious. Imagine needing to print 100 items!
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])

# You can do this instead
for item in shopping_list:
    print(item)
```

### For Loops
In Python, you can use a ``for`` loop to iterate through any iterable object.  
``for`` loops are useful for when you wnat to run code against each item in a list. 

```python
for letter in "fruits":
    print(letter)
```
Output:
```
f
r
u
i
t
s
```

There are times when you might want to skip over an item or end the loop partway through. You can use the ``break`` keyword to end a loop early.

```python
shopping_list = ["bread", "eggs", "milk", "orange"]

for item in shopping_list:
    print(item)
    if item == "milk": # as soon as "milk" is reached, the loop ends and "orange" isn't printed
        break
```

You can loop through dictionaries too. The syntax is slightly different.

```python
food_bill = {
    1 : {"name" : "Cringe Katalyst", "bill" : "£1"},
    2 : {"name" : "Secant Theta", "bill" : "£2"},
    3 : {"name" : "Alder Stone", "bill" : "£3"}
    }

# Looping through keys
for key in food_bill.keys():
    print(key)

# Looping through values
for value in food_bill.values():
    print(value)

# Looping through both
for key, value in food_bill.items():
    print(f"{key}: {value}")

```

### While Loops