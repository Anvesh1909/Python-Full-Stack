# marks = eval(input("enter 6 numbers in list: "))
# marks = list(map(int,input("Enter marks sepby ,: ").split(",")))

marks = []

for i in range(0,6):
    print(i,"subject marks",end=" :")
    marks.append(int(input()))

avg = sum(marks)/len(marks)

if avg <= 10 and avg>9:
    print("A grade")
elif avg <= 9 and avg>8:
    print("B grade")
elif avg <= 8 and avg>7:
    print("c grade")
elif avg <= 7 and avg>6:
    print("d grade")
else:
    print("Fail")


price = int(input("enter price: "))

if price > 25000:
    price = price*(118/100)
    print(price,"18% gst")
elif price < 15000 and price >= 5000:
    price = price*(110/100)
    print(price,"10% gst")
elif price < 5000 and price>0:
    price = price*(105/100)
    print(price,"5% gst")


a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
    print(a,"is greatest")
elif b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")




# num = int(input())

# if num ==1:
#     print(num,"chicken biryani")
# elif num == 2:
#     print(num,"fish biryani")
# elif num == 3:
#     print(num,"mutton biryani")
# elif num == 4:
#     print(num,"veg biryani")
# else:
#     print("enter proper number")


dish_id = 1,2,3,4,5
dish = 'fish biryani','veg biryani','chicken biryani', 'mutton biryani','punner biryani'
price = 270,200,250,300,270

for i in dish_id:
    print(i,dish[i-1])

num = int(input("Enter a dish number: "))


if num ==1:
    print(num,dish[num-1],price[num-1])
elif num == 2:
    print(num,dish[num-1],price[num-1])
elif num == 3:
    print(num,dish[num-1],price[num-1])
elif num == 4:
    print(num,dish[num-1],price[num-1])
elif num == 5:
    print(num,dish[num-1],price[num-1])
else:
    print("enter proper number")
