print("Welcome to the tip calculator.")

bill = input("What in your bill ammount? ")
tip = input("What percent tip would you like to give? ")
split = input("How many people are splitting the bill? ")

float_bill = float(bill)
int_tip = ((int(tip)) / 100) * float_bill
int_split = int(split)

total = (float_bill + int_tip) / 6

message = f"Each person should pay ${total:.2f}"

print(message)
