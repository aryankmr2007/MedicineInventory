# MedicineInventory
This project is a small, command-line application built in Python designed to manage the inventory of medicines and supplies within a college medical room or first-aid station. It provides a simple, menu-driven interface for staff to track which medicines are available



🏥 College Medical Room Inventory System

Project Title

Simple Python-Based Medical Inventory Tracker

Overview of the Project

This project is a small, command-line application built in Python designed to manage the inventory of medicines and supplies within a college medical room or first-aid station. It provides a simple, menu-driven interface for staff to track which medicines are available, how many are in stock, and to update quantities when items are received or dispensed.

Since this version uses a dummy dataset, the inventory resets every time the program is closed, making it ideal for a quick prototype or a learning exercise focused on Python logic (dictionaries, functions, and loops).

Features

The application provides the following core functionalities through a simple menu:

View Inventory: Displays a complete, formatted list of all medicines and their current stock quantities.

Low Stock Alert: Automatically flags any medicine whose quantity falls at or below a defined threshold (15 in the current configuration).

Add/Update Stock: Allows the user to enter a medicine name and add a specific quantity to its stock. If the medicine is new, it is added to the inventory.

Remove/Dispense Stock: Allows the user to select a medicine and subtract a specific quantity (mimicking dispensing to a student/patient). Includes a check to prevent dispensing more than what is available.

Exit: Gracefully closes the application.

Technologies/Tools Used

Language: Python 3.x

Data Structure: Python Dictionary (used for in-memory data storage)

Environment: Command Line Interface (CLI)

Steps to Install & Run the Project

Prerequisites

You need to have Python 3.x installed on your system.

Installation & Setup

Save the Code: Create a new file named inventory_project.py.

Copy the Code: Copy the entire Python code we developed (the final version without emojis) into this file.

Run the Script: Open your terminal or command prompt and navigate to the directory where you saved inventory_project.py.

python inventory_project.py


Instructions for Testing

When the application starts, you will see the main menu. Follow these instructions to test the key features:

Test Case

Steps

Expected Outcome

View Initial Inventory

Select option 1 from the main menu.

Displays all dummy items (e.g., Paracetamol: 50, Band-Aids: 150). You should see "(LOW STOCK)" next to Cough Syrup (10).

Add New Item

1. Select option 2 (Add/Update Stock). 2. Enter "New Antibiotic" as the name. 3. Enter 100 as the quantity.

Output confirms "Added new medicine: New Antibiotic with quantity: 100". Check inventory (option 1) to confirm it is listed.

Dispense/Remove Stock

1. Select option 3 (Remove/Dispense Stock). 2. Enter "Paracetamol (500mg)" as the name. 3. Enter 5 as the quantity.

Output confirms "Dispensed 5 of Paracetamol (500mg). Remaining quantity: 45".

Trigger Low Stock

1. Select option 3 (Remove/Dispense Stock). 2. Enter "Pain Relief Spray" (current stock 25). 3. Enter 15 as the quantity.

Output confirms dispensing. The remaining stock will be 10. You should see an "ALERT: This item is now low on stock!" message.

Exit

Select option 4 from the main menu.

The application prints "Exiting the system. Goodbye!" and closes.

Screenshots (Recommended)

While running the command-line application, you will see output similar to this:

*** WELCOME TO THE COLLEGE MEDICAL ROOM INVENTORY SYSTEM ***

--- Menu ---
1. **View** Inventory
2. **Add/Update** Stock
3. **Remove/Dispense** Stock
4. **Exit**
------------
Enter your choice (1-4): 1

--- Current Medicine Inventory ---
**Antiseptic Wipes:** 75 available
**Band-Aids (Assorted):** 150 available
**Cough Syrup (Bottle):** 10 (LOW STOCK) available
**Gauze Rolls:** 0 (OUT OF STOCK) available
**Pain Relief Spray:** 25 available
**Paracetamol (500mg):** 50 available
-----------------------------------
ACTION REQUIRED: The following items are low on stock: Cough Syrup (Bottle)
<img width="867" height="702" alt="image" src="https://github.com/user-attachments/assets/747e15f2-4638-41eb-bbe0-6b5a7eee135b" />



