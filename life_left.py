age_input = input("what is your age?")

age = int(age_input)
years = 90 - age
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {months} months, {weeks} weeks & {days} days left")
