class stock:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        while True:
            print("--------STOCK MENU--------")
            print()
            print("1. Insert Items:   ")
            print("2. Update Items:   ")
            print("3. Display:   ")
            print("4. Delete:   ")
            print("0. EXIT   ")
            print()
            ch = int(input("Your Choice:   "))
            if ch==1:
                self.insert()
            elif ch==2:
                self.update()
            elif ch==3:
                self.display()
            elif ch==4:
                self.delete()
            elif ch==0:
                break
            else:
                print("!!!!!WRONG CHOICE!!!!!")

    def delete(self):
        cursor = self.con.cursor()
        name = input("Enter the Item ID to delete the item")
        cursor.execute("delete from Stock where Iid='%s';" % name)
        print("Last delete: Success")
        self.con.commit()
        cursor.close()

    def insert (self):
        cursor=self.con.cursor()
        while True:
            iid=self.genID()
            iname=input("Enter Item Name")
            Iqnty=input("Enter Quantity of Item")
            icost=input("Eneter Item cost")
            if Iqnty.isdigit() and icost.isdigit():
                st= "insert into Stock (Iid,Iname,Iqnty,Icost) values('{}','{}',{},{})".format(iid,iname,Iqnty,icost)
                cursor.execute(st)
            self.con.commit()
            ch=int(input("Enter 1 to continue adding enter 0 to exit to stock menu"))
            if ch==1:
                continue
            elif ch==0:
                break
        cursor.close()

    def display(self):
        cursor = self.con.cursor()
        cursor.execute("select * from Stock;")
        row = cursor.fetchall()
        a="{:<13} {:<13} {:<17} {:<13}".format("Item ID","Item Name","Item quantity","Item Cost")
        print(a)
        for r in row:
            b="{:<13} {:<13} {:<17} {:<13}".format(r[0],r[1],r[2],r[3])
            print(b)
        self.con.commit()
        cursor.close()


    def update(self):
        uiid=input("enter Item ID to update")
        cursor = self.con.cursor()
        print("--------Update MENU--------")
        print()
        print("1. Change Item Name:   ")
        print("2. Change Item Quantity:   ")
        print("3. Change Item Cost:   ")
        print("4. Change Everything:   ")
        print("0. Back")
        print()
        
        while True:
            ch = int(input("Your Choice:   "))
            if ch==1:
                uiname = input("Enter Item Name")
                cursor.execute("UPDATE Stock SET Iname='{}' where Iid='{}'".format(uiname,uiid))
            elif ch==2:
                uIqnty = input("Enter Quantity of Item")
                cursor.execute("UPDATE Stock SET Iqnty='{}' where Iid='{}'".format(uIqnty,uiid))
            elif ch==3:
                uicost = input("Eneter Item cost")
                cursor.execute("UPDATE Stock SET Icost='{}' where Iid='{}'".format(uicost,uiid))
            elif ch==4:
                uiname = input("Enter Item Name")
                uIqnty = input("Enter Quantity of Item")
                uicost = input("Eneter Item cost")
                cursor.execute("UPDATE Stock SET Iname='{}', Iqnty = {}, Icost = {} where Iid='{}'".format(uiname,uIqnty,uicost,uiid))
            elif ch==0:
                break
            else:
                print("!!!!!WRONG CHOICE!!!!!")
                continue

        self.con.commit()
        cursor.close()


    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select Iid from Stock order by Iid;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            print(row)
            i = int(row[0][1:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'I' + "0" * (4 - len(str(max))) + str(max)
        return s2