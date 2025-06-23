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