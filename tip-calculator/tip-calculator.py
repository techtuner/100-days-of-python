print("=== Tip Calculator ===")
print("welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_choice = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people are splitting the bill? "))

per_person_payment = round((total_bill / number_of_people) * (1 + tip_choice/100),2)
print(f"Each person should pay: ${per_person_payment}")
