# Name: Vu Tran
# Student ID: 2233511

class ItemToPurchase:
    # Constructor for the ItemToPurchase class
    def __init__(self, name="none", price=0, quantity=0):
        # Initialize the attributes of the class
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    # Method to print the cost of an item
    def print_item_cost(self):
        # Print the output in the desired format
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


# Main function
if __name__ == "__main__":
    # Create two instances of the ItemToPurchase class
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Take user input for item1
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # Take user input for item2
    print("\nItem 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    # Print the total cost of the items
    print("TOTAL COST")
    # Call the print_item_cost method on each item
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate and print the total cost of both items
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"\nTotal: ${total_cost}")
