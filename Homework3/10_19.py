
# Name: Vu Tran
# Student ID: 2233511

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0,
                 item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Prints the cost of the item based on its quantity and price
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = "
              f"${int(self.item_price * self.item_quantity)}")

    def print_item_description(self):
        # Prints the description of the item
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item):
        # Adds an item to the cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Removes an item from the cart by name
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                break
        else:
            print(f"Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        # Modifies the quantity of an item in the cart
        for i in self.cart_items:
            if i.item_name == item.item_name:
                print("Enter the new quantity:")
                quantity = int(input())
                item = i
                item.item_quantity = quantity
                return
        print("Enter the new quantity:")
        quantity = input()
        item.item_quantity = quantity
        print(f"Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Returns the total number of items in the cart
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        # Returns the total cost of the items in the cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_quantity * item.item_price)
        return total_cost

    def print_total(self):
        # Prints the total number of items and total cost of the cart
        num_items = self.get_num_items_in_cart()
        total_cost = self.get_cost_of_cart()

        if len(self.cart_items) == 0:
            # If the cart is empty, print a special message
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {num_items}\n")
            print("SHOPPING CART IS EMPTY")
            print()
            print("Total: $0")

        else:
            # Otherwise, print the cart items and total cost
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {num_items}\n")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${int(total_cost)}")

    def print_descriptions(self):
        # Prints the descriptions of all items in the cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()

    def output_cart(self):
        # Print the shopping cart (including all items and the total cost)
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart()}")


def print_menu(cart):
    # Display the menu options for the user and handle their inputs
    choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                   "Choose an option:\n")

    while choice != "q":
        if choice == "a":
            # Add an item to the cart
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))

            choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                           "Choose an option:\n")

        elif choice == "r":
            # Remove an item from the cart
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

            choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                           "Choose an option:\n")

        elif choice == "c":
            # Modify an item in the cart (change the quantity)
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()
            item = ItemToPurchase(item_name)
            cart.modify_item(item)

            choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                           "Choose an option:\n")

        elif choice == "i":
            # Print the descriptions of all items in the cart
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

            choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                           "Choose an option:\n")

        elif choice == "o":
            # Print the shopping cart (including all items and the total cost)
            print("OUTPUT SHOPPING CART")
            cart.print_total()

            choice = input("\nMENU\n\
a - Add item to cart\n\
r - Remove item from cart\n\
c - Change item quantity\n\
i - Output items' descriptions\n\
o - Output shopping cart\n\
q - Quit\n\n"
                           "Choose an option:\n")

        else:
            # Handle invalid inputs
            choice = input("Choose an option:\n")


def main():
    # Get the customer's name and the current date, and display them
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Display the menu and handle the user's inputs
    print_menu(ShoppingCart(customer_name, current_date))


if __name__ == "__main__":
    main()
