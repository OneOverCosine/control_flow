# ---- Loops -----

shopping_list = ["bread", "eggs", "milk", "orange"]

# This is tedious. Imagine needing to print 100 items!
# print(shopping_list[0])
# print(shopping_list[1])
# print(shopping_list[2])
# print(shopping_list[3])

# You can do this instead
# for item in shopping_list:
#     print(item)
#     if item == "milk":
#         break

# A dictionary containing other dictionaries
food_bill = {
    1 : {"name" : "Cringe Katalyst", "bill" : "£1"},
    2 : {"name" : "Secant Theta", "bill" : "£2"},
    3 : {"name" : "Alder Stone", "bill" : "£3"}
    }

# Looping through keys
# for key in food_bill.keys():
#     print(key)

# Looping through values
# for value in food_bill.values():
#     print(value)

# Looping through both
# for key, value in food_bill.items():
#     print(f"{key}: {value}")


# for val1 in food_bill.values():
#     for val2 in val1.values():
#         print(val2)

# working with while

# num = 0
# while num < 10:
#     print(num)
#     if num == 4:
#         break
#     num += 1

while True:    
    age = input("Please enter your age: ")
    if age.isdigit():
        break
  
    print("Please enter your age as a whole number!\n")


print(f"Your age: {age}")