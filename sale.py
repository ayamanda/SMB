from datetime import date


class sale:
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.aid = ''
        self.cname = ''
        self.cmob = 0
        self.da = date.today()
        self.insert()

    def insert(self):
        cursor = self.con.cursor()
        self.aid = input("Enter Your Agent ID: ")
        self.cname = input("Enter Customer Name: ")
        self.cmob = input("Enter Customer Mobile Number: ")
        d = {}
        while True:

            if len(d) == 0:
                item = input("Enter Item ID: ")
                cursor.execute("select Iname from Stock where Iid='{}'".format(item))
                iname = (cursor.fetchall())[0][0]
                print(iname)
                cursor.execute("select Icost from Stock where Iid='{}'".format(item))
                iqty = int(input("Enter the item Quantity"))
                icost = ((cursor.fetchall())[0][0]) * iqty
                d[item] = [icost, iqty, iname]
                item = ""
            else:
                item = input("Enter Item ID or Press 0 to !!!EXIT!!! : ")
                if item == '0':
                    print("**********PRODUCTS ADDED SUCESSFULLY**********")
                    print()
                    self.invoice(d)
                    break
                cursor.execute("select Iname from Stock where Iid='{}'".format(item))
                iname = (cursor.fetchall())[0][0]
                print(iname)
                cursor.execute("select Icost from Stock where Iid='{}'".format(item))
                iqty = int(input("Enter the item Quantity"))
                icost = ((cursor.fetchall())[0][0]) * iqty
                d[item] = [icost, iqty, iname]
                item = ""

    def invoice(self, d):
        cursor = self.con.cursor()
        invc = self.genID()
        l_k = list(d.keys())
        l_v = list(d.values())
        tcost = 0
        for i in l_v:
            tcost = tcost + i[0]  # myltiplying the cost of each item with the quantity
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

        a = "{:<13} {:<13} {:<17} {:<13}".format("Item ID", "Item Name", "Item quantity", "Item Cost")
        print(a)
        for a, b in zip(l_k, l_v):
            b = "{:<13} {:<13} {:<17} {:<13}".format(a, b[2], b[1], b[0])
            print(b)
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
            print(row)
            i = int(row[0][3:])
            if i > max:
                max = i
        max = max + 1
        s2 = 'Inv' + "0" * (4 - len(str(max))) + str(max)
        return s2
