#Day 2 Udemy, Tip Calculator

print("Welcome to the tip calculator.")

bill_total = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))


tip = bill_total * (tip_percent / 100)
bill_with_tip = bill_total + tip
individual_bill = bill_with_tip / num_people

#truncate decimal points, but remember, must have 0 if rounds to, for example, 19.6
truncated_result = "{:.2f}".format(individual_bill)

print(f"Each person should pay: ${truncated_result}")
