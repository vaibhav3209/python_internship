#
# QUESTION 1.) Practise Pandas Series
import pandas as pd
                                                #series k index will be keys of dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
print("QUESTION 1.) Practise Pandas Series..............................\n")
x = pd.Series(data)
print(x)
#ACCESS SERIES ITEMS
'''range() ki length automate karni'''
for i in range(3):
    print(f"person: {x["Name"][i]} is of age:{x["Age"][i]} lives in:{x["City"][i]}")

data2 = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 22, 'Chicago']
]
y = pd.Series(data2)
print(y)
#
# #ACCESS ITEMS from SERIES FROM LIST
for i in range(3):
    for u in range(1):
        print(f"person: {y[i][u]} is of age:{y[i][u+1]} lives in:{y[i][u+2]}")
#..............................................................


# QUESTION 2.) DataFrames
'''USING ABOVE DATA2 AS LIST OF LISTS
DATA AS DICTIONARY'''
print("\n\nQUESTION 2.) DataFrames..................................\n")
df1 = pd.DataFrame(data)
print("dictionary se dataframe:\n",df1)

df2 = pd.DataFrame(data2)
print("lsit of lists se dataframe\n",df2)


data3 = [
    ('Alice', 25, 'New York'),
    ('Bob', 30, 'Los Angeles'),
    ('Charlie', 22, 'Chicago')
]
df3 = pd.DataFrame(data3)
print("lsit of tuples se dataframe\n",df3)


data4 = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Chicago'}
]
df4 = pd.DataFrame(data4)
print("lsit of dictionaries se dataframe\n",df4)
# .............................................



# QUESTION 3.)Data iteration
print("\n\nQUESTION 3.)Data iteration................................")
print("all names in data frame are\n",df4.loc[:,"Name"])
print("deatils: ",df4.loc[0:1,:])                          #isme include hota hai
print("deatils by iloc[]\n: ",df4.iloc[0:1,:])          #isme inc. nhi hota

print("2 rows of 3 column:\n",df3.loc[[0,1],:])
print("singular row:\n",df3.iloc[0,:])                      #series ki form mein dega


print("delte first row:\n",df1.drop(0))
                                                                    #isko loop se karna and also check for every
                                                                    #type of dataframe
lst0 = (df4.loc[0,:]).tolist()
lst1 = (df4.loc[1, :]).tolist()
lst2 = (df4.loc[2, :]).tolist()

final = []
final.extend([lst0,lst1,lst2])
print("\n\nlsit of rows is:",final)


# pos = int(input("enter position after which to enter a new row "))
# new_df = df4.iloc[]
#     Insert row at given position in Pandas Dataframe
