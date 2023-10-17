class stock:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        while True:
            try:
                print("--------STOCK MENU--------")
                print()
                print("1. Insert Items:   ")
                print("2. Update Items:   ")
                print("3. Display:   ")
                print("4. Delete:   ")
                print("5. Low Stock:   ")
                print("0. Back   ")
                print()
                ch = int(input("Your Choice:   "))
                if ch == 1:
                    self.insert()
                elif ch == 2:
                    self.update()
                elif ch == 3:
                    self.display()
                elif ch == 4:
                    self.delete()
                elif ch == 5:
                    self.low_stock()
                elif ch == 0:
                    break
                else:
                    print("!!!!!WRONG CHOICE!!!!!")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

    def delete(self):
        cursor = self.con.cursor()
        name = input("Enter the Item ID to delete the item: ")
        cursor.execute("delete from Stock where Iid='%s';" % name)
        print("Last delete: Success")
        self.con.commit()
        cursor.close()

    def insert(self):
        cursor = self.con.cursor()
        while True:
            try:
                iid = self.genID()
                iname = input("Enter Item Name:    ")
                Iqnty = input("Enter Quantity of Item:     ")
                icat = input("Enter Item category:     ")
                icost = input("Enter Item cost:    ")

                if Iqnty.isdigit() and icost.isdigit():
                    st = "insert into Stock (Iid, Iname, Icategory, Iqnty, Icost) values('{}','{}','{}',{},{})".format(
                        iid, iname, icat, Iqnty, icost)
                    cursor.execute(st)
                    self.con.commit()
                else:
                    print("Wrong input. Quantity and cost should be numeric.")
                    continue

                ch = int(input("Enter 1 to continue adding or 0 to exit to the stock menu:     "))
                if ch == 1:
                    continue
                elif ch == 0:
                    break
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

        cursor.close()

    def display(self):
        cursor = self.con.cursor()
        cursor.execute("select * from Stock;")
        row = cursor.fetchall()
        print()
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        a = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format("| Item ID", "| Item Name", "| Item Category",
                                                             "| Item quantity", "| Item Cost", "|")
        print(a)
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        for r in row:
            b = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format('|   ' + r[0], '|   ' + r[1], '|   ' + r[2],
                                                                 '|   ' + str(r[3]), '|  ' + str(r[4]), '|')
            print(b)
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        self.con.commit()
        cursor.close()

    def update(self):
        uiid = input("enter Item ID to update")
        cursor = self.con.cursor()
        print("--------Update MENU--------")
        print()
        print("1. Change Item Name:   ")
        print("2. Change Item Quantity:   ")
        print("3. Change Item Cost:   ")
        print("4. Change Item Category:   ")
        print("5. Change Everything:   ")
        print("0. Back")
        print()

        while True:
            try:
                ch = int(input("Your Choice:   "))
                if ch == 1:
                    uiname = input("Enter Item Name:    ")
                    cursor.execute("UPDATE Stock SET Iname='{}' where Iid='{}'".format(uiname, uiid))
                elif ch == 2:
                    uIqnty = input("Enter Quantity of Item:    ")
                    cursor.execute("UPDATE Stock SET Iqnty='{}' where Iid='{}'".format(uIqnty, uiid))
                elif ch == 3:
                    uicost = input("Eneter Item cost:   ")
                    cursor.execute("UPDATE Stock SET Icost='{}' where Iid='{}'".format(uicost, uiid))
                elif ch == 4:
                    uicat = input("Eneter Item category:    ")
                    cursor.execute("UPDATE Stock SET Icategory='{}' where Iid='{}'".format(uicat, uiid))
                elif ch == 5:
                    uiname = input("Enter Item Name:    ")
                    uIqnty = input("Enter Quantity of Item:    ")
                    uicost = input("Eneter Item cost:   ")
                    uicat = input("Eneter Item category:    ")
                    cursor.execute(
                        "UPDATE Stock SET Iname='{}', Iqnty = {}, Icost = {}, Icategory = {}, where Iid='{}'".format(uiname,
                                                                                                                     uIqnty,
                                                                                                                     uicost,
                                                                                                                     uicat,
                                                                                                                     uiid))
                elif ch == 0:
                    break
                else:
                    print("!!!!!WRONG CHOICE!!!!!")
                    continue
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

        self.con.commit()
        cursor.close()

    def low_stock(self):
        print("!!!!!!!!!!LOW STOCK ITEMS!!!!!!!!!!")
        cursor = self.con.cursor()
        cursor.execute("select * from Stock where Iqnty<=5;")
        row = cursor.fetchall()
        print()
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        a = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format("| Item ID", "| Item Name", "| Item Category",
                                                             "| Item quantity", "| Item Cost", "|")
        print(a)
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        for r in row:
            b = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format('|   ' + r[0], '|   ' + r[1], '|   ' + r[2],
                                                                 '|   ' + str(r[3]), '|  ' + str(r[4]), '|')
            print(b)
        print('|', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('|')
        self.con.commit()
        cursor.close()

    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select Iid from Stock order by Iid;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            i = int(row[0][1:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'I' + "0" * (4 - len(str(max))) + str(max)
        return s2
