""""
import os

path = "T1_Test_Cases"
file_names = os.listdir(path)

# Create a list to store the content of each file
file_contents = []

for file_name in file_names:
    file_path = os.path.join(path, file_name) # combining the directory path and current file name
    try:
        # Open and read the text file
        with open(file_path, 'r') as file:
            # Process the content of the file as needed
            content = file.read()
            #Print the file name and content
            print(f"File: {file_name}\nContent:\n{content}\n")
            
            # Append the content to the list
            file_contents.append(content)

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {str(e)}")

#############################################33

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item quantities and prices
        self.sales_records = {}  # Dictionary to track sales records
        self.profit = 0.0

    def process_command(self, command):
        parts = command.split()
        action = parts[0]

        if action == "ADD":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.inventory:
                self.inventory[item_name][0] += quantity
            else:
                self.inventory[item_name] = [quantity, price]

        elif action == "SELL":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
                self.profit += quantity * (price - self.inventory[item_name][1])
                if item_name not in self.sales_records:
                    self.sales_records[item_name] = []
                self.sales_records[item_name].append((quantity, price))
            else:
                return "Profit/Loss: NA"

        elif action == "RETURN":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.sales_records and self.sales_records[item_name]:
                for i in range(len(self.sales_records[item_name]) - 1, -1, -1):
                    sold_quantity, sold_price = self.sales_records[item_name][i]
                    if sold_quantity >= quantity and sold_price == price:
                        self.sales_records[item_name][i] = (sold_quantity - quantity, sold_price)
                        self.profit -= quantity * (price - self.inventory[item_name][1])
                        break
                else:
                    return "Profit/Loss: NA"
            else:
                return "Profit/Loss: NA"

        elif action == "WRITEOFF":
            item_name, quantity = parts[1].lower(), int(parts[2])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
                self.profit -= quantity * self.inventory[item_name][1]
            else:
                return "Profit/Loss: NA"

        elif action == "DONATE":
            item_name, quantity = parts[1].lower(), int(parts[2])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
            else:
                return "Profit/Loss: NA"

        elif action == "CHECK":
            result = []
            for item_name, (quantity, _) in self.inventory.items():
                result.append(f"{item_name.capitalize()}: {quantity}")
            return "\n".join(result)

        elif action == "PROFIT":
            return f"Profit/Loss: ${self.profit:.2f}"

        return None

if __name__ == "__main__":
    input_files = ["input_01.txt", "input_02.txt", "input_03.txt", "input_04.txt", "input_05.txt", "input_06.txt"]

    for file_name in input_files:
        ims = InventoryManagementSystem()
        with open(os.path.join(path, file_name), "r") as file: 
            commands = file.readlines()
            for command in commands:
                result = ims.process_command(command.strip())
                if result is not None:
                    print(result)
        print("\n")  # Add a newline between outputs of different files
"""
import os

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item quantities and prices
        self.sales_records = {}  # Dictionary to track sales records
        self.profit = 0.0

    def process_command(self, command):
        parts = command.split()
        action = parts[0]

        if action == "ADD":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.inventory:
                self.inventory[item_name][0] += quantity
            else:
                self.inventory[item_name] = [quantity, price]

        elif action == "SELL":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
                self.profit += quantity * (price - self.inventory[item_name][1])
                if item_name not in self.sales_records:
                    self.sales_records[item_name] = []
                self.sales_records[item_name].append((quantity, price))
            else:
                return "Profit/Loss: NA"

        elif action == "RETURN":
            item_name, quantity, price = parts[1].lower(), int(parts[2]), float(parts[3])
            if item_name in self.sales_records and self.sales_records[item_name]:
                for i in range(len(self.sales_records[item_name]) - 1, -1, -1):
                    sold_quantity, sold_price = self.sales_records[item_name][i]
                    if sold_quantity >= quantity and sold_price == price:
                        self.sales_records[item_name][i] = (sold_quantity - quantity, sold_price)
                        self.profit -= quantity * (price - self.inventory[item_name][1])
                        break
                else:
                    return "Profit/Loss: NA"
            else:
                return "Profit/Loss: NA"

        elif action == "WRITEOFF":
            item_name, quantity = parts[1].lower(), int(parts[2])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
                self.profit -= quantity * self.inventory[item_name][1]
            else:
                return "Profit/Loss: NA"

        elif action == "DONATE":
            item_name, quantity = parts[1].lower(), int(parts[2])
            if item_name in self.inventory and self.inventory[item_name][0] >= quantity:
                self.inventory[item_name][0] -= quantity
            else:
                return "Profit/Loss: NA"

        elif action == "CHECK":
            result = []
            for item_name, (quantity, _) in self.inventory.items():
                result.append(f"{item_name.capitalize()}: {quantity}")
            return "\n".join(result)

        elif action == "PROFIT":
            return f"Profit/Loss: ${self.profit:.2f}"

        return None

def process_input_file(file_path):
    ims = InventoryManagementSystem()
    try:
        with open(file_path, "r") as file:
            commands = file.readlines()
            for command in commands:
                result = ims.process_command(command.strip())
                if result is not None:
                    print(result)
        print("\n")  # Add a newline between outputs of different files
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {str(e)}")

if __name__ == "__main__":
    path = "T1_Test_Cases"
    input_files = ["input_01.txt", "input_02.txt", "input_03.txt", "input_04.txt", "input_05.txt", "input_06.txt"]

    for file_name in input_files:
        file_path = os.path.join(path, file_name)
        print(f"Processing file: {file_name}")
        process_input_file(file_path)

