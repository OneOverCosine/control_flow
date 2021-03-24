age = int(input("Enter your age: "))
# if the user is above the age of 15 allow them to buy a ticket

ratings = ['U', 'PG', '12', '15', '18']

if age >= 18:
    print(f"At {age}, you can watch moives reated {ratings[4]} and lower.")
elif age >= 15:
    print(f"At {age}, you can watch movies rated {ratings[3]} and lower.")
elif age >= 12:
    print(f"At {age}, you can watch movies rated {ratings[2]} lower.")
elif age < 12:
    print(f"At {age}, you can watch moives rated {ratings[1]}, but it's reccomended that an adult accompany you.\nYou can watch movies rated {ratings[0]} without accompaniment.")
else:
    print("Something went wrong...") # this will execute if none of the other conditions are met

