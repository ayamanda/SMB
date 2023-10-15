d={}
while(True):
    print("--------MAIN MENU--------")
    print()
    print("1. Enter Hotel Details:   ")
    print("2. Search a Hotel:   ")
    print("3. Remove a Hotel:   ")
    print("4. Print Hotel Details in Tabular format:   ")
    print()
    ch=int(input("Your Choice:   "))
    if(ch==1):
        for i in range(10):
            hotelid=int(input(":   "))
            hname=input("Enter Hotel Name:   ")
            hcat=input("Enter Hotel Category:    ")
            L=[hname,hcat]
            d[hotelid]=L
        print()
        print(d)
        print()
    elif(ch==2):
        s=int(input("Enter Hotel ID to search:   "))
        print()
        if s in d.keys():
            print(d[s])
            print()
        else:
            print("Not Found")
            print()
    elif(ch==3):
        id1=int(input("Enter Hotel ID to remove its details:   "))
        id2=int(input("Enter another Hotel ID to remove its details:   "))
        if id1 in d.keys():
            del d[id1]
        if id2 in d.keys():
            del d[id2]
        print(d)
        print()
    elif(ch==4):
        print()
        ax="{:<11} {:<28} {:<13}".format("Hotel ID", "Hotel Name","Category")
        print(ax)
        print()
        for i in d.keys():
            text="{:<11} {:<28} {:<13}".format(i,d[i][0],d[i][1])
            print(text)
        print()
    else:
        print("Wrong Choice!")
        break











    
