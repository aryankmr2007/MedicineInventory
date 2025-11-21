# --- 1. Dummy Data Storage ---

# The inventory is stored in a simple dictionary (Medicine Name: Quantity)
# This data will reset every time the script is run.
medical_inventory = {
    "Paracetamol (500mg)": 50,
    "Band-Aids (Assorted)": 150,
    "Antiseptic Wipes": 75,
    "Cough Syrup (Bottle)": 10,
    "Pain Relief Spray": 25,
    "Gauze Rolls": 0
}

# Define a low stock threshold
LOW_STOCK_THRESHOLD = 15 

# --- 2. Core Project Functions ---

def view_inventory():
    """Prints a formatted list of all available medicines, including low stock alerts."""
    print("\n--- Current Medicine Inventory ---")
    
    if not medical_inventory:
        print("Inventory is currently empty.")
        print("-----------------------------------")
        return

    low_stock_items = []
    
    # Iterate through the dictionary items (key-value pairs), sorted by name
    for medicine, quantity in sorted(medical_inventory.items()):
        status = ""
        if quantity <= 0:
            status = " (OUT OF STOCK)"
        elif quantity <= LOW_STOCK_THRESHOLD:
            status = " (LOW STOCK)"
            low_stock_items.append(medicine)
        
        # Display the medicine name and quantity
        print(f"**{medicine}:** {quantity}{status} available")
        
    print("-----------------------------------")
    
    if low_stock_items:
        print(f"ACTION REQUIRED: The following items are low on stock: {', '.join(low_stock_items)}")


def update_stock():
    """Adds a new medicine or updates the quantity of an existing one."""
    print("\n--- Add/Update Stock ---")
    # .strip().title() cleans up input and capitalizes names for consistency
    med_name = input("Enter medicine name to add/update (e.g., Antacid): ").strip().title()
    
    try:
        stock_qty = int(input("Enter quantity to ADD: "))
        
        if stock_qty <= 0:
            print("Quantity to add must be a positive number.")
            return

        if med_name in medical_inventory:
            medical_inventory[med_name] += stock_qty
            print(f"Updated stock for **{med_name}**. New quantity: {medical_inventory[med_name]}")
        else:
            medical_inventory[med_name] = stock_qty
            print(f"Added new medicine: **{med_name}** with quantity: {stock_qty}")
                 
    except ValueError:
        print("Invalid quantity input. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def remove_stock():
    """Decreases the quantity of a medicine (dispensing)."""
    print("\n--- Remove/Dispense Stock ---")
    med_name = input("Enter medicine name to dispense: ").strip().title()

    if med_name not in medical_inventory:
        print(f"Error: **{med_name}** is not found in the inventory.")
        return

    try:
        dispense_qty = int(input(f"Enter quantity of {med_name} to remove: "))
        
        if dispense_qty <= 0:
            print("Quantity to remove must be a positive number.")
            return

        current_qty = medical_inventory[med_name]
        
        if current_qty < dispense_qty:
            print(f"Warning: Cannot dispense {dispense_qty}. Only {current_qty} available.")
        else:
            medical_inventory[med_name] -= dispense_qty
            new_qty = medical_inventory[med_name]
            print(f"Dispensed {dispense_qty} of **{med_name}**. Remaining quantity: {new_qty}")

            if new_qty <= LOW_STOCK_THRESHOLD:
                 print("ALERT: This item is now low on stock!")

    except ValueError:
        print("Invalid quantity input. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- 3. Main Program Loop ---

def main():
    """The main function to run the inventory system."""
    print("\n*** WELCOME TO THE COLLEGE MEDICAL ROOM INVENTORY SYSTEM ***")
    
    while True:
        print("\n--- Menu ---")
        print("1. **View** Inventory")
        print("2. **Add/Update** Stock")
        print("3. **Remove/Dispense** Stock")
        print("4. **Exit**")
        print("------------")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_inventory()
            
        elif choice == '2':
            update_stock()
            
        elif choice == '3':
            remove_stock()
