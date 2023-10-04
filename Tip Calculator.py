#Melvin's Tip N Split Calculator

print("Welcome to the 'Tip N Split' Calculator!")

total = input("What was the total bill? $")
total_float = float(total)

tip_precentage = input("what percentage tip would you like to give? 10, 12, or 15? ")
tip_precentage_float = float(tip_precentage)
tip = total_float * (tip_precentage_float / 100)

split = input("how many people to split the bill? ")
split = int(split)

tfe = (tip +  total_float) / split
tfe = round(tfe, 2)
print("Each person has to pay $" + str(tfe))
