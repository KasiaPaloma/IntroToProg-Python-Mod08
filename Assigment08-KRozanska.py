# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KRozanska,12.13.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strProduct = ""  # Captures the product name from user
strProductPrice = ""  # Captures the product price from user


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        __str__: -> (string with product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KRozanska,12.13.2020,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # 	   -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product name cannot have numbers in it.")

    # product_price
    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Price must be numeric.")

    # -- Methods --
    def __str__(self):
        return self.product_name + ',' + self.product_price


# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list)
        """
        list_of_product_rows = []
        try:
            list_of_product_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            raise e
        return list_of_product_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data to file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you will be writing to file:
        :return: (list) of dictionary rows
        """
        try:
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(row.__str__() + '\n')
            file.close()
            print("Data Saved!")
        except Exception as e:
            raise e
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View Current Data
        2) Add New Product
        3) Save Current Data to File      
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list(list_of_product_rows):
        """ Shows the current Products in list

        :param list_of_product_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The Current List of Products Is: *******")
        for row in list_of_product_rows:
            print('\t\t\t' + row.product_name + " - $" + row.product_price.strip())
        print("************************************************")

    @staticmethod
    def input_new_product_and_price():
        """ Gets the product and price from user

        :return: object
        """
        product = str(input("Which product would you like to add? - ")).strip().title()
        price = float(input("What is the price? - "))
        p = Product(product_name=product, product_price=price)
        return p

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    # Show user a menu of options
    IO.print_menu_Tasks()
    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.print_current_list(lstOfProductObjects)
        continue

    # Let user add data to the list of product objects
    if strChoice.strip() == '2':
        lstOfProductObjects.append(IO.input_new_product_and_price())
        continue
    # let user save current data to file and exit program
    if strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue

    if strChoice.strip() == '4':
        print("Goodbye")
        break

# Main Body of Script  ---------------------------------------------------- #
