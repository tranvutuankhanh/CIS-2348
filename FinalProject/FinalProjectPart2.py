# Name: Vu Tran
# Student ID: 2233511

import csv
from datetime import datetime


# This class is responsible for managing the inventory of electronic items
class ElectronicsInventory:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item data
        self.item_types = set()  # Set to store unique item types

    # Load manufacturer list and store item details in the inventory dictionary
    def load_manufacturer_list(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, manufacturer, item_type, damaged = row[0], row[1].strip(), row[2], row[3] if len(
                    row) == 4 else ''
                self.inventory[item_id] = {'manufacturer': manufacturer, 'item_type': item_type, 'damaged': damaged}
                self.item_types.add(item_type)

    # Load price list and update the inventory dictionary with price information
    def load_price_list(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, price = row[0], float(row[1])
                if item_id in self.inventory:
                    self.inventory[item_id]['price'] = price

    # Load service dates list and update the inventory dictionary with service date information
    def load_service_dates_list(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, service_date = row[0], datetime.strptime(row[1], '%m/%d/%Y')
                if item_id in self.inventory:
                    self.inventory[item_id]['service_date'] = service_date


# This class is responsible for generating various inventory reports by extending the ElectronicsInventory class
class InventoryReports(ElectronicsInventory):
    # Generate a full inventory CSV file sorted by manufacturer and item ID
    def generate_full_inventory_csv(self):
        def sort_key(inventory_item):
            inventory_id, inventory_data = inventory_item
            return inventory_data['manufacturer'], inventory_id

        def format_date_without_leading_zeros(date):
            return f"{date.month}/{date.day}/{date.year}"

        with open('FullInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
            for item_id, item in sorted(self.inventory.items(), key=sort_key):
                service_date = format_date_without_leading_zeros(item['service_date']) if 'service_date' in item else ''
                writer.writerow([item_id, item['manufacturer'], item['item_type'], int(item['price']),
                                 service_date, item['damaged']])

    # Generate a laptop inventory CSV file sorted by item ID
    def generate_laptop_inventory_csv(self):
        def format_date_without_leading_zeros(date):
            return f"{date.month}/{date.day}/{date.year}"

        with open('LaptopInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for item_id, item in sorted(self.inventory.items()):
                if item['item_type'] == 'laptop':
                    damaged = item['damaged'] if item['damaged'] else ''
                    price = int(item['price']) if 'price' in item else ''
                    service_date = format_date_without_leading_zeros(
                        item['service_date']) if 'service_date' in item else ''
                    writer.writerow([item_id, item['manufacturer'], price, service_date, damaged])

    # Generate a CSV file with items that have a service date in the past, sorted by service date
    def generate_past_service_date_inventory_csv(self):
        past_service_items = []

        def format_date_without_leading_zeros(date):
            return f"{date.month}/{date.day}/{date.year}"

        for past_item_id, past_item in self.inventory.items():
            if 'service_date' in past_item and past_item['service_date'] < datetime.now():
                past_service_items.append((past_item_id, past_item))

        # Define the sort key for sorting the past_service_items by service date
        def sort_key(item_tuple):
            item_id, item = item_tuple
            return item['service_date']

        # Sort the past_service_items list using the sort key
        past_service_items.sort(key=sort_key)

        # Write the past_service_items to a CSV file
        with open('PastServiceDateInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for past_item_id, past_item in past_service_items:
                writer.writerow(
                    [past_item_id, past_item['manufacturer'], past_item['item_type'], int(past_item['price']),
                     format_date_without_leading_zeros(past_item['service_date']), past_item['damaged']])

    # Generate a damaged inventory CSV file sorted by descending price
    def generate_damaged_inventory_csv(self):
        def sort_key(inventory_item):
            inventory_id, inventory_data = inventory_item
            return -inventory_data['price']

        def format_date_without_leading_zeros(date):
            return f"{date.month}/{date.day}/{date.year}"

        with open('DamagedInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
            for item_id, item in sorted(self.inventory.items(), key=sort_key):
                if item['damaged']:
                    writer.writerow([item_id, item['manufacturer'], item['item_type'], int(item['price']),
                                     format_date_without_leading_zeros(item['service_date'])])

    # Generate a CSV file for each item type in the inventory
    def generate_item_type_inventory_csv(self):
        def format_date_without_leading_zeros(date):
            return f"{date.month}/{date.day}/{date.year}"

        for item_type in self.item_types:
            with open(f'{item_type.capitalize()}Inventory.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for item_id, item in sorted(self.inventory.items()):
                    if item['item_type'] == item_type:
                        damaged = item.get('damaged', '')
                        price = int(item['price']) if 'price' in item else ''
                        service_date = format_date_without_leading_zeros(
                            item['service_date']) if 'service_date' in item else ''
                        writer.writerow([item_id, item['manufacturer'], price, service_date, damaged])

    # Query the inventory based on the user's input and return the most expensive item and the closest alternative
    def query_inventory(self, query):
        query_words = [word for word in query.strip().lower().split() if word != 'a']

        manufacturers = [word for word in query_words if any(
            word.lower() in inventory_item['manufacturer'].lower() for _, inventory_item in self.inventory.items())]
        item_type = next((word for word in query_words if any(
            word.lower() == inventory_item['item_type'].lower() for _, inventory_item in self.inventory.items())),
                         '')

        if len(manufacturers) > 1:
            manufacturers = list(set(manufacturers))
            if len(manufacturers) > 1:
                return "No such item in inventory"

        manufacturer = manufacturers[0] if manufacturers else ''

        valid_items = []
        for item_id, item in self.inventory.items():
            if item_type.lower() == item['item_type'].lower():
                if item.get('damaged', False):
                    continue
                elif 'service_date' in item and item['service_date'] < datetime.now():
                    continue
                else:
                    valid_items.append((item_id, item))

        if not valid_items:
            return "No such item in inventory"

        # Find the most expensive item from the specified manufacturer
        most_expensive_item = None
        for item in valid_items:
            if manufacturer.lower() in item[1]['manufacturer'].lower():
                if most_expensive_item is None or item[1]['price'] > most_expensive_item[1]['price']:
                    most_expensive_item = item

        if most_expensive_item is None:
            return f"No {manufacturer} {item_type} in inventory"

        # Find the closest priced item from a different manufacturer
        closest_item = None
        min_price_diff = float('inf')
        for item in valid_items:
            if item[1]['manufacturer'].lower() != most_expensive_item[1]['manufacturer'].lower():
                price_diff = abs(item[1]['price'] - most_expensive_item[1]['price'])
                if price_diff < min_price_diff:
                    min_price_diff = price_diff
                    closest_item = item

        result = f"Your item is: {most_expensive_item[0]}, {most_expensive_item[1]['manufacturer']}, " \
                 f"{most_expensive_item[1]['item_type']}, {int(most_expensive_item[1]['price'])}"

        if closest_item:
            result += f"\nYou may, also, consider: {closest_item[0]}, {closest_item[1]['manufacturer']}, " \
                      f"{closest_item[1]['item_type']}, {int(closest_item[1]['price'])} "

        return result


# Main function to run the inventory application
def main():
    inventory = InventoryReports()

    manufacturer_list_file = "ManufacturerList.csv"
    price_list_file = "PriceList.csv"
    service_dates_list_file = "ServiceDatesList.csv"
    inventory.load_manufacturer_list(manufacturer_list_file)
    inventory.load_price_list(price_list_file)
    inventory.load_service_dates_list(service_dates_list_file)

    while True:
        query = input("\nPlease enter the manufacturer and item type (or 'q' to quit): ")
        if query.strip().lower() == 'q':
            break

        print(inventory.query_inventory(query))


if __name__ == "__main__":
    main()
