# Use the ‘Automobile_data.csv’ and answer following questions by using Pandas library:
import pandas as pd
df = pd.read_csv("Automobile_data.csv")

# From given data set, print first and last five rows.
print(df.head(5))
print(df.tail(5))

# Replace all column values which contain ‘?’ and ‘n.a.’ with NaN. Update the CSV file.
df = pd.read_csv("Automobile_data.csv", na_values={
    'price':["?","n.a"],
    'stroke':["?","n.a"],
    'horsepower':["?","n.a"],
    'peak-rpm':["?","n.a"],
    'average-mileage':["?","n.a"]
    })
print (df)
df.to_csv("Automobile_data.csv")

# Print All volvo Cars details.
car_Manufacturers = df.groupby('company')
volvoDf = car_Manufacturers.get_group('volvo')
print(volvoDf)

# Count total cars per company.
print(df['company'].value_counts())

# Find each company’s Highest price car.
priceDf = car_Manufacturers['company','price'].max()
print(priceDf)

# Find the average mileage of each car making company.
mileageDf = car_Manufacturers['company','average-mileage'].mean()
print(mileageDf)

# Merge two data frames using the following condition: Create two data frames using the
# following two Dicts, Merge two data frames, and append second data frame as a new
# column to the first data frame.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
# Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)