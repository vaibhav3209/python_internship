#question 1...................................................
# import re
# name = input("Type name!!!!!!!!!!\n")
#
# if re.findall(r"^v|^V",name):
#     print(f"safe!! {name} is a very nice name")
# else : print("get a better name next time")
#
#
# email = input("type email.......\n")
#
# if  re.findall(r"@gmail.com$",email) :
#     print(f"safe!! {email} is a valid email")
#
# else : print("get a better email next time")
#
#
# mobile = input("type it 5digit number")
#
# if re.findall(r"[1-5][0-5][0-5][0-5][0-5]",mobile):
#     print(f"safe!! {mobile} got u")
# else: print("RUN")
#
#

#.................................................
#question 2.)
import pandas as pd
# import datetime
fixed = "2038-01-19 03:14:07"
# year  = fixed.dt.year
time = pd.to_datetime(fixed)
print(time)

print("\nyeaar:",time.year)
print("month :",time.month,"\tmonth name:",time.month_name())
print("date:",time.day,"\tday:",time.day_name())
print("hour:",time.hour)
print(time.isocalendar())

# ........................................................................
#QUESTION3
# pd.options.display.max_rows =100
file = pd.read_csv("products-100.csv")
data = pd.DataFrame(file,columns=["Index","Name","Category","Price","Stock","Availability"])
print("\nfinal table for analysis\n",data.to_string())

print("\nBASIC DETAILS:\n")
print(data.info(),data.describe(),data.shape,sep="\n")

print("\n1.)Products by popularity:(pre-order<-out of stock<-limited stock<-in stock) \n")
print(data.sort_values(by="Availability").to_string())





# high_p =(data["Availability"]=="pre_order")
# print((data[data["Name"]]==high_p).head())
# print("\n2)Least popular products(backorder<-discontinued)\n")