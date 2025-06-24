#QUESTION 1 CSV ADDRESS BOOK
import csv
# add_book = [
#     ["name","address","mobile","email"],
#     ["vaibhav","kota",1222,"e@gm"],
#     ["malav","delhi",5554,"g@gm"],
#     ["feb","up",4445,"f@gs"],
#     ["dec","mp",4785,"gg@gm"]
# ]
#
# with open("address.csv","w",newline="") as file:                    #jab with open() karte to close() karne ki no need
#                                                                     #baaki mein karna padega
#     var = csv.writer(file)
#     for x in add_book:
#         var.writerow(x)

# with open("address.csv","r",newline="") as file2:
#     var2=csv.reader(file2)
#     for x in var2:
#         print(x)

#....................................................

# QUESTION 2 ...............................

# import requests
# def weather(city,api_key):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     var = requests.get(url)
#     var.raise_for_status()
#     weather_data = var.json()
#
#     print(f"cooordinates for {city} are:\n{weather_data['coord']['lon']} longitude and {weather_data['coord']['lat']}")
#     print(f"temperature is {weather_data['main']['temp']}°F")
#     print(f"humidity {weather_data['main']['humidity']}%")
#     print(f"wind speeds {weather_data['wind']['speed']}units")
#
#
# city = input("enter city for weather data: ")
# my_api="903664686bab1d5ff4898b2233ae72a3"
# weather(city,my_api)

#..................................................................
#QUESTION 3:
import sqlite3
conn = sqlite3.connect("asssignment4.db")              #database

# def create_table(name):
# conn.execute('''                          -- ek table to create hoti but not 3 simultaneously
# CREATE TABLE students(
# rollno INTEGER PRIMARY KEY,
# sname VARCHAR(30),
# age INTEGER
# )
# ''')
#
# conn.executescript('''                    -- execute karo multiple sql satetements separated by ;
# CREATE TABLE teachers(
# id INTEGER PRIMARY KEY,
# tname VARCHAR(30),
# age INTEGER,
# sub VARCHAR(30)
# );
# CREATE TABLE DEPARTMENT(
# sub VARCHAR(30) PRIMARY KEY,
# dept VARCHAR(30)
# )''')
#...................................................



#insert data
# conn.executescript('''
# INSERT INTO students
#  values
# (101,"vaib",20),
# (102,"bl",21),
# (103,"chal",22);
#
# INSERT INTO teachers
#  values
# (1,"bhanu",20,"hindi"),
# (2,"gupta",21,"eng"),
# (3,"sharma",22,"maths");
#
# INSERT INTO DEPARTMENT
#  values
# ("eng","cs"),
# ("hindi","it"),
# ("maths","meta");
# ''')
# conn.commit()

#..........................................
#printing and updating
table1 = conn.execute('''SELECT * FROM students''')               #can we print three tables simultsneously do by hit and trial
table2 = conn.execute('''SELECT * FROM teachers''')
table3 = conn.execute('''SELECT * FROM DEPARTMENT''')
                                                                        #iska koi combine sattement hai kya
                                                                        #iske uptput mein column names nhi aate kya
for x in table1:
    print(x)
for x in table2:
    print(x)
for x in table3:
    print(x)

#updateing values
conn.execute("UPDATE students SET sname = \"mehul\" WHERE rollno = 102 ")
table1 = conn.execute('''SELECT * FROM students''')
for x in table1:
    print(x)

#delteting
conn.close()


# while True:
#     x = int(input("enter your choice: "))
#     if x == 1:
#         name = input("enter name for table: ")
#         create_table(name)
#     if x == 2:
#         break