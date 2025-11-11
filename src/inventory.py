# Assignment 4: Grocery Store Inventory Manager
# Objective: Complete the missing parts to manage store inventory using lists, loops, and conditions.

# Starter Data
items = ["milk", "bread", "eggs", "apples", "rice", "coffee"]
prices = [3.5, 2.0, 4.0, 1.5, 5.0, 6.0]
stock = [10, 20, 15, 25, 8, 12]

# -------------------------------
# Task 1: Display all items with price and stock
# Print output like: milk - $3.5 - 10 in stock
# -------------------------------

# TODO: Write a loop to print each item with its price and stock


# -------------------------------
# Task 2: Check if an item exists in inventory
# -------------------------------

item_name = input("Enter the item you want to buy: ").lower()

# TODO: Check if item_name exists in items list
# If it exists, print its price and stock
# Else, print "Sorry, that item is not available."


# -------------------------------
# Task 3: Process a purchase
# -------------------------------

# TODO: If item exists, ask user how many they want to buy
# Use if-else to check:
#   - If enough stock: calculate total cost and update stock
#   - If not enough stock: print "Not enough stock available."


# -------------------------------
# Task 4: Add a new product
# -------------------------------

# TODO: Ask if user (manager) wants to add a new product (yes/no)
# If yes:
#   - Take new product name, price, and stock as input
#   - Append them to the respective lists
#   - Print updated inventory


# -------------------------------
# Task 5 (Bonus): Multiple customers
# -------------------------------
# TODO: Wrap the above logic in a loop that runs until user enters "exit"
# After all purchases:
#   - Display total sales made
#   - Print remaining stock for each item