# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Fixed bug by clearing the list before it was refilled
# Kevin Wong,11.13.2019,Modified code to complete assignment 6
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "products.txt"    # The name of the data file
lstOfProductObjects = []
strChoice = ""                  # Capture the user option selection

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Kevin Wong,11.26.2019,Modified code to complete assignment 8    
        """

    def __init__(self, product_name, product_price):
        self.name = product_name            
        self.price = product_price
# Data -------------------------------------------------------------------- #



# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Product": data[0].strip(), "Price": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        """
        Desc - Writes data from a list of dictionary rows to a file 

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            objFile = open(strFileName, "w")
            for dicRow in lstOfProductObjects:  # Write each row of data to the file
                objFile.write(f'{dicRow["Product"]},{dicRow["Price"]}\n')
            objFile.close()

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")

    @staticmethod
    def ReloadDataFromFile(file_name, list_of_rows):
        """
        Desc - Reloads data from file to list.

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstOfProductObjects.clear()  
            FileProcessor.ReadFileDataToList(strFileName, lstOfProductObjects)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
            
# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new product
        3) Remove an existing product
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(f'{row["Product"]}, ${row["Price"]}')
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def AddDataToList(list_of_rows):
        """ Ask user input for Product and Price

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        product_name = str(input("What is the product? - ")).strip()  # Get product from user
        product_price = float(input("What is the product's price? - "))  # Get price from user
        print()  # Add an extra line for looks
        dicRow = {"Product": product_name, "Price": product_price}  # Create a new dictionary row
        lstOfProductObjects.append(dicRow)  # Add the new row to the list/table
    
    @staticmethod
    def RemoveDataFromList(list_of_rows):
        """ Ask user input for Product to delete from list. Then update update user Product was deleted or not.

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        strKeyToRemove = input("Which product would you like removed? - ")  # get Product user wants deleted
        blnItemRemoved = False  # Create a boolean Flag for loop

        intRowNumber = 0  # Create a counter to identify the current dictionary row in the loop

        while(intRowNumber < len(lstOfProductObjects)):
            if(strKeyToRemove == str(list(dict(lstOfProductObjects[intRowNumber]).values())[0])):  # Search current row column 0
                del lstOfProductObjects[intRowNumber]  # Delete the row if a match is found
                blnItemRemoved = True  # Set the flag so the loop stops
            intRowNumber += 1  # Increase counter to get next row

        if(blnItemRemoved == True):
            print("The Product was removed.")
        else:
            print("I'm sorry, but I could not find that Product.")
        print()  # Add an extra line for looks

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
def main():
    # Load data from file into a list of product objects when script starts
    FileProcessor.ReadFileDataToList(strFileName, lstOfProductObjects)  # read file data
    
    
    while(True):
        IO.OutputMenuItems()                # Show user a menu of options
        strChoice = IO.InputMenuChoice()    # Get user input for menu option
        
        if (strChoice.strip() == '1'):
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show user current data in the list of product objects
            continue  # to show the menu
    
        # Add a new item to the list/Table
        elif(strChoice.strip() == '2'):
            IO.AddDataToList(lstOfProductObjects)          # Ask user for new Product and Price and add item to the List/Table
            IO.ShowCurrentItemsInList(lstOfProductObjects) # Show current data in the list/table
            continue  # to show the menu
    
        # Remove a new item to the list/Table
        elif(strChoice == '3'):
            IO.RemoveDataFromList(lstOfProductObjects)     # Ask user for item to delete and confirm to delete item from list
            IO.ShowCurrentItemsInList(lstOfProductObjects) # Show current data in the list/table
            continue  # to show the menu
    
        # Save Products to the products.txt file
        elif(strChoice == '4'):
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
            FileProcessor.WriteListDataToFile(strFileName, lstOfProductObjects)   # Ask the user if they want to save that data
            continue
    
        # Reload data from the products.txt file (clears the current data from the list/table)
        elif (strChoice == '5'):
            FileProcessor.ReloadDataFromFile(strFileName, lstOfProductObjects)
            continue  # to show the menu
    
        # Exit the program
        elif (strChoice == '6'):
            break   # and Exit

        else:
            print("Please only select between option 1 to 6.")
            continue
                
# Main Body of Script  ---------------------------------------------------- #
          

    
# Start the Program
main()
