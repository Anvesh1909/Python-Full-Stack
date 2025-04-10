import mysql.connector

con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anv@14078",
        database='Internship_supermarket'
    )

cursor = con.cursor()


def viewItems():
    print("---------------view items--------------------")
    query = 'SELECT COUNT(*) FROM products;'
    cursor.execute(query)
    count = cursor.fetchone()
    print("The number of items in the inventory are:", count[0])

    query = 'SELECT * FROM products;'
    cursor.execute(query)
    products = cursor.fetchall()  

    if products:
        print("Here are all the items available in the supermarket:")
        for i in products:
            print(f'Name: {i[1]} \nQuantity: {i[2]} \nPrice: {i[3]}\n')

def addItem():
    print("---------------Add items--------------------")
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
        print("Item already exists")

def purchaseItem():
    print("---------------Purchase items--------------------")

def searchItem():
    print("---------------Search item--------------------")

def editItem():
    print("---------------Edit item--------------------")

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
        purchaseItem()
    elif choice==4:
        searchItem()
    elif choice==5:
        editItem()
    elif choice==6:
        print("---------------exited--------------------")
        break
    else:
        print("Enter valid choice")






