from datetime import date


class sale:
    def __init__(self, con, aid):
        self.con = con  # Initialize the database connection
        self.cursor = self.con.cursor()
        self.aid = aid  # Store the agent ID
        self.cname = ''  # Initialize customer name
        self.cmob = 0  # Initialize customer mobile
        self.da = date.today()  # Get the current date
        while True:
            try:
                print("--------SALE MENU--------")
                print()
                print("1. New Sale:   ")
                print("0. Back:   ")
                print()
                ch = int(input("Your Choice:   "))
                if ch == 1:
                    self.insert()
                elif ch == 0:
                    break
                else:
                    print("!!!!!WRONG CHOICE!!!!!")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

    def insert(self):
        cursor = self.con.cursor()
        self.cname = input("Enter Customer Name: ")
        self.cmob = input("Enter Customer Mobile Number: ")
        d = {}
        while True:
            try:
                if len(d) == 0:
                    item = input("Enter Item ID: ")
                    cursor.execute("SELECT COUNT(*) FROM Stock WHERE Iid = '{}'".format(item))
                    check = cursor.fetchall()
                    if check[0][0] > 0:
                        cursor.execute("select Iname,Icategory from Stock where Iid='{}'".format(item))
                        l = cursor.fetchall()
                        iname = l[0][0]
                        print()
                        print("Product Name: ", iname)
                        icat = l[0][1]
                        print("Product Category: ", icat)
                        print()
                        cursor.execute("select Icost from Stock where Iid='{}'".format(item))
                        iqty = int(input("Enter the item Quantity"))
                        icost = ((cursor.fetchall())[0][0]) * iqty
                        d[item] = [iname, icat, icost, iqty]
                        cursor.execute("UPDATE Stock SET Iqnty=Iqnty-'{}' where Iid='{}'".format(iqty, item))
                        item = ""
                    else:
                        print("!!!!!Wrong Item Id Entered!!!!!")
                        continue
                else:
                    item = input("Enter Item ID or Press 0 to !!!EXIT!!! : ")
                    if item == '0':
                        print("**********PRODUCTS ADDED SUCESSFULLY**********")
                        print()
                        self.invoice(d)
                        break
                    cursor.execute("SELECT COUNT(*) FROM Stock WHERE Iid = '{}'".format(item))
                    check = cursor.fetchall()
                    if check[0][0] > 0:
                        cursor.execute("select Iname,Icategory from Stock where Iid='{}'".format(item))
                        l = cursor.fetchall()
                        iname = l[0][0]
                        print()
                        print("Product Name: ", iname)
                        icat = l[0][1]
                        print("Product Category: ", icat)
                        print()
                        cursor.execute("select Icost from Stock where Iid='{}'".format(item))
                        iqty = int(input("Enter the item Quantity"))
                        icost = ((cursor.fetchall())[0][0]) * iqty
                        d[item] = [iname, icat, icost, iqty]
                        cursor.execute("UPDATE Stock SET Iqnty=Iqnty-'{}' where Iid='{}'".format(iqty, item))
                        item = ""
                    else:
                        print("!!!!!Wrong Item Id Entered!!!!!")
                        continue
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

    def invoice(self, d):
        cursor = self.con.cursor()
        invc = self.genID()
        l_k = list(d.keys())
        l_v = list(d.values())
        tcost = 0
        for i in l_v:
            tcost = tcost + i[2]  # myltiplying the cost of each item with the quantity
        gst = 18 / 100 * tcost
        tcost = tcost + gst

        print("********** SASTA SHOPPING MALL **********")
        print("---------- BILL ----------")
        print()
        print("Invoice No:  ", invc)
        print()
        print("Agent ID: ", self.aid)
        print("Customer Name: ", self.cname)
        print("Customer Mobile No: ", self.cmob)
        print("Date: ", self.da)

        cursor.execute(
            "insert into Sale (Invc,Cname,Cmob,Netpay,Gst,Aid) values('{}','{}',{},{},{},'{}')".format(invc, self.cname,
                                                                                                       self.cmob, tcost,
                                                                                                       gst, self.aid))

        print()
        print('+', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('+')
        a = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format("| Item ID", "| Item Name", "| Item Category",
                                                             "| Item quantity", "| Item Cost", "|")
        print(a)
        print('+', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('+')
        for a, b in zip(l_k, l_v):
            b = "{:<13} {:<20} {:<17} {:<17} {:17} {:<2}".format('|   ' + a, '|   ' + b[0], '|   ' + str(b[1]),
                                                                 '|   ' + str(b[2]), '|   ' + str(b[3]), '|')
            print(b)
        print('+', end='')
        for i in range(0, 13 + 20 + 17 + 17 + 21):
            print('-', end='')
        print('+')

        print()
        print("GST: ₹", gst)
        print("Net Payable Amount:  ₹", tcost)

        self.con.commit()

    def genID(self):
        cursor = self.con.cursor()
        cursor.execute("select Invc from Sale order by Invc;")
        r = cursor.fetchall()
        max = 0
        for row in r:
            i = int(row[0][3:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'Inv' + "0" * (4 - len(str(max))) + str(max)
        return s2
