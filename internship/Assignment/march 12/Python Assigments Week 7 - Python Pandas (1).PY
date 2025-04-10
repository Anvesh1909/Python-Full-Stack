# 1
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
print(df.head())
print(df.tail())


# 2
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
df.replace(["?", "n.a", "NaN"], pd.NA, inplace=True)
df.to_csv('updated_dataset.csv', index=False)



# 3
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
mCar = df.loc[df['price'].idxmax()]
print(mCar)

# 4
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
tCars = df[df['company']=='toyota']
print(tCars)


# 5
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
cCount = df['company'].value_counts()
print(cCount)


# 6
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
sCars = df.sort_values(by='price',ascending=False)
print(sCars)


# 7
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
highestPrice = df.loc[df.groupby('company')['price'].idxmax()]
print(highestPrice)


# 8
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
avg_milage = df.groupby('company')['average-mileage'].mean()
print(avg_milage)


# 9
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')
germanCars = pd.DataFrame({'company': ['ford', 'mercedes', 'BMV', 'audi'], 'price': [23845, 171995, 135925, 71400]})
japaneseCars = pd.DataFrame({'company': ['toyota', 'honda', 'nissan', 'mitsubishi'], 'price': [29995, 23600, 61500, 58900]})
concat_df = pd.concat([germanCars, japaneseCars], ignore_index=True)
print(concat_df)





# 10
import pandas as pd

df = pd.read_csv('Assignment\march 12\Automobile_data.csv')

Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]})
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]})
res_def = pd.merge(Car_Price, car_Horsepower, on='Company')
print(res_def)
