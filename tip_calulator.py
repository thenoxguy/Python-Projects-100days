a_bill = input("what is your total bill?")
a_tip = input("What is the percentage of tip you wanna give?")
a_number_of_friends = input("In how many people you wanna divide the bill?")

bill = float(a_bill)
tip = int(a_tip)
number_of_friends = int(a_number_of_friends)

final_bill = (bill + (bill * (tip/100)))
splitted_bill = (final_bill/number_of_friends)

rounded_bill = round (splitted_bill, 2)

print (f"You have to pay {rounded_bill}")
