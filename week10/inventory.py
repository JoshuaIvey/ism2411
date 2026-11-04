
# Self Assesment Questions
# 1. The most suprising thing about how lists work in Python is how easy I found it to be to add and remove items. It looked complex to me, but I didn't expect to be able to change lists so easily. 
# 2. I work at a restaurant, and I could use a python list to help my boss keep track of inventory. It would be easier than manually inputting it into Excel and Python would be able to organize the items quickly. 

# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4

inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5

coords = (40.7128, -74.0060)
print(coords)
print("Tuples are useful for coordinates because they can't be changed.")

# Exercise 6

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.9, 2)
    discounted.append(new_price)
print(prices)
print(discounted)

# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print("Average", round(sum(high_sales) / len(high_sales), 2))