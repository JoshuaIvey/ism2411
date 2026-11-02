# AI USE: Debugger (helped me fix the last print statement for Exercise 3)

# Self Assessment Questions
# 1. The first bug I spotted was the missing : in the for loop. I found it from the traceback. This tells me that I am getting better at using error messages.
# 2. The apply_discount uses the price and a customer tier and returns the price after the discount. I do think a colleague could use it because the names explain what it does.
# 3. I used Ai to help me fix my last print statement for Exercise 3. It helped me understand how to correctly format the statement and display the final price instead of just giving me the answer. 


# Exercise 1

def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.1
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)
print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

# Exercise 3

discounted = apply_discount(200, "gold")
print (f"After gold discount: ${discounted:.2f}")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After tax: ${total:.2f}")
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')



# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # I fixed the total so it correctly adds each sale
    total += sale
print(f"Total: ${total}")

count = 0
# I added a missing : to the for loop
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Removed the = so it doesn't run an extra time. 
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? 100 because it is just printing the x which is set to 100
print(double_it()) # what prints here? 1998 because the double_it is set to 999 and then the function multiplies it to 2
print(x)           # has x changed? It still prints 100 because the x in the function is seperate
