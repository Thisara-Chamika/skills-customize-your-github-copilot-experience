# 📘 Assignment: Inventory Tracker with Dictionaries

## 🎯 Objective

Practice using Python dictionaries to store, update, and look up simple inventory data. By the end of the assignment, students will build a small program that tracks items and their quantities.

## 📝 Tasks

### 🛠️ Create the Inventory Data

#### Description
Set up a dictionary to store a store inventory with item names as keys and quantities as values.

#### Requirements
Completed program should:

- Create a dictionary with at least three inventory items
- Use item names as keys and quantities as values
- Print the inventory in a readable format

### 🛠️ Update Item Quantities

#### Description
Write a function that adds new items to the inventory or updates the quantity of existing items.

#### Requirements
Completed program should:

- Define a function called `update_inventory()`
- Accept an item name and a quantity value
- Add the item if it does not exist
- Increase the quantity if the item already exists

### 🛠️ Find Items and Check Stock

#### Description
Write a function that looks up an item in the inventory and reports whether it is available.

#### Requirements
Completed program should:

- Define a function called `check_stock()`
- Return the quantity for a given item name
- Return a helpful message if the item is not in the inventory
- Optionally identify items that are running low
