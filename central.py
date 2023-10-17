import mysql.connector
from stock import stock
from sale import sale
from SaleStat import SaleStat

class main:
    def __init__(self, aid):
        # Establish a connection to the MySQL database
        self.con = mysql.connector.connect(host="localhost", user="root", password="ayan2005")
        self.cursor = self.con.cursor()
        # Select the database to work with
        self.cursor.execute("USE ShoppingMallBilling")

        while True:
            try:
                print("--------MAIN MENU--------")
                print()
                print("1. Stocks")
                print("2. Sale")
                print("3. SaleStat")
                print("0. Exit")
                print()
                ch = int(input("Your Choice: "))

                if ch == 1:
                    # Option 1: Manage Stocks
                    stock(self.con)
                elif ch == 2:
                    # Option 2: Perform Sales
                    sale(self.con, aid)
                elif ch == 3:
                    # Option 3: View Sale Statistics
                    SaleStat(self.con)
                elif ch == 10:
                    # Hidden feature to drop the database (use with caution)
                    i = input("You discovered a Hidden feature to drop the database, press 'y' to continue or 'n' to dismiss: ")
                    if i == 'y':
                        # Drop the database if confirmed
                        self.cursor.execute("DROP DATABASE IF EXISTS ShoppingMallBilling;")
                        print("*****DATABASE DELETED*****")
                        break
                    else:
                        print("Congrats, you avoided a big mistake.")
                elif ch == 0:
                    # Exit the program
                    break
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
