print("Welcome to the tip calculator.")

bill = input("What in your bill ammount? ")
tip = input("What percent tip would you like to give? ")
split = input("How many people are splitting the bill? ")

float_bill = float(bill)
int_tip = ((int(tip)) / 100) * float_bill
int_split = int(split)

total = (float_bill + int_tip)

total_per = (float_bill + int_tip) / 6

message1 = f"The total bill is ${total:.2f}"
message2 = f"Each person should pay ${total_per:.2f}"

print(message1)
print(message2)
