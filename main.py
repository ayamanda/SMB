import mysql.connector
from central import main

class agent:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="ayan2005")
        self.cursor = self.con.cursor()

        '''________________DATABASE SETUP_____________________'''

        # Create the ShoppingMallBilling database if it doesn't exist
        self.cursor.execute("Create database if not exists ShoppingMallBilling")
        self.cursor.execute("use ShoppingMallBilling")

        # Create tables for Stock, Agent, and Sale if they don't exist
        self.cursor.execute(
            "Create table if not exists Stock(Iid varchar(20) Primary key,Iname varchar(20),Icategory varchar(20), Iqnty int, Icost int);")
        self.cursor.execute(
            "Create table if not exists Agent(Aid varchar(20) Primary key,Aname varchar(20),Apwd varchar(20), Amob bigint);")
        self.cursor.execute(
            "Create table if not exists Sale(Invc varchar(20) Primary key,Cname varchar(20),Cmob varchar(20), Netpay int, Gst int,Aid varchar(20), foreign key (Aid) references Agent(Aid))")

        '''***************************************************'''

        '''___________LOGIN AND NEW-USER MENU____________'''

        print("1. New User")
        print("2. Login")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            self.new_user()
        elif ch == 2:
            self.login()
        else:
            print("!!!!!WRONG CHOICE!!!!!")

        '''**********************************************'''

    def new_user(self):
        cursor = self.con.cursor()
        aid = self.genID()
        aname = input("Enter Agent Name: ")
        while True:
            amob = input("Enter Agent Mobile no: ")
            if len(amob) < 10:
                print("!!!!!Enter 10 digit mobile no!!!!!")
                continue
            else:
                break
        while True:
            apwd = input("Enter Password: ")
            apwd_check = input("Re-enter password: ")
            if apwd != apwd_check:
                print("!!!!!Re-Password not matched Re-enter password !!!!!")
                continue
            else:
                break
        st = "insert into Agent (Aid,Aname,Amob,Apwd) values('{}','{}','{}','{}');".format(aid, aname, amob, apwd)
        cursor.execute(st)
        print("Successfully registered a new agent")
        print(aid)
        self.con.commit()
        cursor.close()
        self.login()

    def login(self):
        cursor = self.con.cursor()
        while True:
            aid = input("Enter your Id: ")
            cursor.execute("SELECT COUNT(*) FROM Agent WHERE Aid = '{}'".format(aid))
            check = cursor.fetchall()
            if check[0][0] > 0:
                apwd = input("Enter your password: ")
                cursor.execute("select Apwd from Agent where Aid='%s';" % aid)
                r = cursor.fetchall()
                if r[0][0] == apwd:
                    cursor.execute("select Aname from Agent where Aid='%s';" % aid)
                    print("Welcome ", cursor.fetchall()[0][0])
                    main(aid)  # Launch the main menu for the agent
                    break
                else:
                    print("!!!!!Wrong Password!!!!!")
                    continue
            else:
                print("!!!!!Wrong Agent Id!!!!!")
                continue

    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select Aid from Agent order by Aid;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            i = int(row[0][1:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'A' + "0" * (4 - len(str(max))) + str(max)
        return s2

agent()
