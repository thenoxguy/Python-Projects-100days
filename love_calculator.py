name1 = str(input("What is your name?"))
name2 = str(input("What is your partner's name?"))

name1 = name1.lower()
name2 = name2.lower()

number_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
number_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

final_result = (number_true * 10) + number_love

print (f"Your love score is {final_result}")
