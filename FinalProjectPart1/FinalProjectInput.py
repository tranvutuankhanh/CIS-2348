# Name: Vu Tran
# Student ID: 2233511

import csv
from datetime import datetime


# Define the ElectronicsInventory class to manage the inventory of electronic items
class ElectronicsInventory:
    # Initialize the inventory dictionary and item_types set
    def __init__(self):
        self.inventory = {}
        self.item_types = set()

    # Load the manufacturer list from a CSV file and update the inventory dictionary and item_types set
    def load_manufacturer_list(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, manufacturer, item_type, damaged = row[0], row[1].strip(), row[2], row[3] if len(
                    row) == 4 else ''
                self.inventory[item_id] = {'manufacturer': manufacturer, 'item_type': item_type, 'damaged': damaged}
                self.item_types.add(item_type)

    # Load the price list from a CSV file and update the inventory dictionary with the price information
    def load_price_list(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, price = row[0], float(row[1])
                if item_id in self.inventory:
                    self.inventory[item_id]['price'] = price

    # Load the service dates list from a CSV file and update the inventory dictionary with the service date information
    def load_service_dates_list(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id, service_date = row[0], datetime.strptime(row[1], '%m/%d/%Y')
                if item_id in self.inventory:
                    self.inventory[item_id]['service_date'] = service_date

    # Generate a full inventory CSV file sorted by manufacturer and item ID
    def generate_full_inventory_csv(self):
        def sort_key(inventory_item):
            inventory_id, inventory_data = inventory_item
            return inventory_data['manufacturer'], inventory_id

        with open('FullInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
            for item_id, item in sorted(self.inventory.items(), key=sort_key):
                service_date = item['service_date'].strftime('%-m/%-d/%Y') if 'service_date' in item else ''
                writer.writerow([item_id, item['manufacturer'], item['item_type'], int(item['price']),
                                 service_date, item['damaged']])

    # Generate a laptop inventory CSV file sorted by item ID
    def generate_laptop_inventory_csv(self):
        with open('LaptopInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for item_id, item in sorted(self.inventory.items()):
                if item['item_type'] == 'laptop':
                    damaged = item['damaged'] if item['damaged'] else ''
                    price = int(item['price']) if 'price' in item else ''
                    service_date = item['service_date'].strftime('%-m/%-d/%Y') if 'service_date' in item else ''
                    writer.writerow([item_id, item['manufacturer'], price, service_date, damaged])

    # Generate a CSV file with items that have a service date in the past, sorted by service date
    def generate_past_service_date_inventory_csv(self):
        past_service_items = []

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
                     past_item['service_date'].strftime('%-m/%-d/%Y')])

    # Generate a damaged inventory CSV file sorted by descending price
    def generate_damaged_inventory_csv(self):
        def sort_key(inventory_item):
            inventory_id, inventory_data = inventory_item
            return -inventory_data['price']

        with open('DamagedInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
            for item_id, item in sorted(self.inventory.items(), key=sort_key):
                if item['damaged']:
                    writer.writerow([item_id, item['manufacturer'], item['item_type'], int(item['price']),
                                     item['service_date'].strftime('%-m/%-d/%Y')])


# The main function to run the script
def main():
    inventory = ElectronicsInventory()

    manufacturer_list_file = "ManufacturerList.csv"
    price_list_file = "PriceList.csv"
    service_dates_list_file = "ServiceDatesList.csv"

    # Load the manufacturer, price, and service dates lists
    inventory.load_manufacturer_list(manufacturer_list_file)
    inventory.load_price_list(price_list_file)
    inventory.load_service_dates_list(service_dates_list_file)

    # Generate the full inventory, laptop inventory, past service date inventory, and damaged inventory CSV files
    inventory.generate_full_inventory_csv()
    inventory.generate_laptop_inventory_csv()
    inventory.generate_past_service_date_inventory_csv()
    inventory.generate_damaged_inventory_csv()


# Run the main function if the script is run as the main module
if __name__ == "__main__":
    main()
