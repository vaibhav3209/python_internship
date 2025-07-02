# question1.).........................
import pandas as pd
dates = pd.Series(["2023-01-25", "2024-02-14", "2025-01-21","2025-10-10"])
print(dates)

timeseries = pd.to_datetime(dates)
print(timeseries)              #type == datetime64[ns]



#QUESTION 2.).............................................

df1 = pd.DataFrame({ "id":[1,2,3,4],
    'fruit': ['apple','mango','banana','orange'], 'qty': [10,20,30,35],
                    "available":[True,False,True,True]},index=[1,2,3,4])
df2 = pd.DataFrame({"id":[1,3,5,7],
                      'veg': ['okra','loki','tomato','zomato'], 'qty': [35,30,20,20],
                    "available":[True,True,False,False]},index=[1,2,3,4])

print(df1)
print(df2)
vaib = df1.merge(df2,on= "id")
print("mergerd along id:\n",vaib)

vaib = df1.merge(df2,on= "id",how="left")
print("Left join on id:\n",vaib)

#NaN: not a number is entered for values not available for a particular id

vaib = df1.merge(df2,on= "available",how="right")
print("right join on available:\n",vaib)
#for right join it present all values of available values of DF2 which are equal in DF1

vaib = df1.join(df2,on="id",rsuffix="p",lsuffix="d")
print("\n joining df\n",vaib)


# ........................................
#QUESTION 3.)

# df3 =
concat = pd.concat([df1,df2]
                   # ,keys=["pehla","doosra"]
                   )
print("\nconcaeanted:\n",concat)

df3 = pd.DataFrame({ "id":[1,3,7],
    'name': ['vaib','mohit','shiv'], 'age': [15,20,22] },
index=[1,2,3])
print(df3)

vaib = df3.merge(concat,on="id")
print(vaib)

vaib = concat.join(df3,lsuffix="-p",rsuffix="-d")
print(vaib)


# .................................
