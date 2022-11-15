itemname=input("Enter the item name : ")
itemquantity=int(input("Enter the item Quantity : "))
itemprice=int(input("Enter the item price : "))

print(f'''
    ##################### Bill ###################
    item Name\t\titem Quantity\t\titem Price
    {itemname}\t\t\t{itemquantity}\t\t\t{itemprice}

    **********************************************
    Total Amount to be paid :{itemquantity*itemprice} 
''')
