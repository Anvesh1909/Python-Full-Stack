import pandas as pd 

print("===Sub modules===")
print(dir(pd))
print("=================")



import pandas as pd

df = pd.DataFrame()
print(df)
print("Type",type(df))
print("Dimentions",df.ndim)





import pandas as pd

df = pd.DataFrame([1,2,3,4,5,6,7,8,9])
print(df)






import pandas as pd

L = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(L)
print(df)






import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]

df = pd.DataFrame(dataSet)
print(df)





import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
df = pd.DataFrame(dataSet,columns=col)
print(df)





import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1001","1222","1221","13343"]

df = pd.DataFrame(dataSet,columns=col,index=i)
print(df)






import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1001","1222","1221","13343"]

df = pd.DataFrame(dataSet,columns=col,index=i)

print("First 5")
print(df.head())

print()
print("First 2")
print(df.head(2))

print()
print("First 1")
print(df.head(1))



import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1001","1222","1221","13343"]

df = pd.DataFrame(dataSet,columns=col,index=i)


print()
print("Last 5")
print(df.tail())

print()
print("Last 2")
print(df.tail(2))





import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1001","1222","1221","13343"]

df = pd.DataFrame(dataSet,columns=col,index=i)


print()
print(df.sum())


print()
print(df.sum(1))



import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1","2","3","4"]

df = pd.DataFrame(dataSet,columns=col,index=i)
print(df)

# print("using sum(1)")
# print(df.sum(1))

print("Max()")
print(df.max())

print("Min()")
print(df.min())

print("Count()")
print(df.count())



import pandas as pd

dataSet = [[1,"Anvesh",22],[2,"surya",23],[3,"Nikhil",25],[4,"Bunny",22]]
col = ["rollno","name","age"]
i = ["1","2","3","4"]

df = pd.DataFrame(dataSet,columns=col,index=i)
print(df)

print("coloums")
for i in df.iterrows():
    print(i)

print("Rows")
for i in df.itertuples():
    print(i)