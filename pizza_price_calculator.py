size = str(input("What size do you want? type 'S' for small, 'M' for medium, 'L' for large."))
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

pepperoni = str(input("Do you want pepperoni? type 'Y' for yes, 'N' for no"))

if pepperoni == "Y" and size == "S" :
    bill += 2
elif pepperoni == "Y" and size == "M" or "L":
    bill += 3

extra_cheese = str(input("Do you want extra cheese? type 'Y' for yes, 'N' for no"))

if extra_cheese == "Y":
    bill += 1

print (f"Your final bill is {bill}")
