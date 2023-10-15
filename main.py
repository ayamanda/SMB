import mysql.connector
from stock import stock
from sale import sale

class main:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",password="ayan2005")
        self.cursor = self.con.cursor()
        self.cursor.execute("use ShoppingMallBilling")
        print("--------MAIN MENU--------")
        print()
        print("1. Stocks   ")
        print("2. Sale   ")
        print()
        ch = int(input("Your Choice:   "))
        if ch==1:
            stock(self.con)
        elif ch==2:
            sale(self.con)