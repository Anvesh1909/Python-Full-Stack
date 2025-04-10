

import mysql.connector


con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anv@14078",
        database='Internship_supermarket'
    )
cursor = con.cursor()

def viewItems():
    print("===============View Items=================")
    
    query = 'SELECT COUNT(*) FROM products;'
    cursor.execute(query)
    count = cursor.fetchone()
    print("The number of items in the inventory are:", count[0])

    query = 'SELECT * FROM products;'
    cursor.execute(query)
    products = cursor.fetchall()  

    print("Here are all the items available in the supermarket:")
    for i in products:
        print(f'ID: {i[0]} \nName: {i[1]} \nQuantity: {i[2]} \nPrice: {i[3]}')

def addItem():
    print("===============Add Items=================")
    try:    
        name = input("Item name : ")
        quantity = int(input("Item quantity : "))
        price = float(input("Price $ : "))
        
        if quantity<0:
            print("quantity must be greater than equal 0")
            return 
        
        s = f'insert into products(name,quantity,price) values(%s,%s,%s)'
        cursor.execute(s,(name,quantity,price))
        con.commit()
        print("Item has been successfully added.")
    except Exception as e:
        print(e)

def purchaseItems():
    print("===============Purchase Items=================")
    query = 'SELECT * FROM products;'
    cursor.execute(query)
    products = cursor.fetchall() 
    print(products)
    product = input("Which item do you want to purchase? Enter name: ")
    quantity = int(input("Enter the no of quantity: "))
    for i in products:
        if i[1]== product:
            if i[2]-quantity<0:
                print("requested quantity is not available")
                return 
            try:
                quary = 'update products set quantity=%s where name=%s'
                cursor.execute(quary,(i[2]-quantity,product))
                con.commit()
                print(f"Pay {i[3]*quantity} at checkout counter")
            except Exception as e:
                print(e)
            
def searchItems():
    print("===============Search Items=================")
    product = input("Enter the item's name to search in inventory : ")
    query = 'SELECT * FROM products where name = %s'
    cursor.execute(query,(product,))
    products = cursor.fetchone() 
    if product:
        print(products)
    else:
        print("no products found")

def editItems():
    print("===============Edit Items=================")
    product = input("Enter the name of the item that you want to edit: ")

    name = input("Item name : ")
    quantity = int(input("Item quantity : "))
    price = float(input("Price $ : "))
    try:
        query = 'update products set name=%s,quantity=%s,price=%s where name=%s'
        cursor.execute(query,(name,quantity,price,product))
        con.commit()
        print("Item has been successfully updated.")
    except Exception as e:
        print(e)



while True:
    s = '''Press enter to continue.
    1. View items
    2. Add items for sale
    3. Purchase items
    4. Search items
    5. Edit items
    6. Exit
    Enter the number of your choice: '''
    choice = int(input(s))

    if choice==1:
        viewItems()
    elif choice==2:
        addItem()
    elif choice==3:
        purchaseItems()
    elif choice==4:
        searchItems()
    elif choice==5:
        editItems()
    elif choice==6:
        print("===============exited=================")
        break
    else:
        print("Enter valid number")
    
