# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

meal_cost = float(raw_input())
tip_rate = int(raw_input())
tax_rate = int(raw_input())

tip = meal_cost * tip_rate/100
tax = meal_cost * tax_rate/100

total_cost = meal_cost + tip + tax

print "The total meal cost is " + str(int(round(total_cost))) + " dollars."