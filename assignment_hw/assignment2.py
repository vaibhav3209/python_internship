#QUESTION 2.............


#
# name=input("enter srtudent name")
# clas=input("enter srtudent class")
# a,b,c,d,e = (input("enter marks of students").split())
# total_marks = int(a)+int(b)+int(c)+int(d)+int(e)
# per= total_marks/5
# print(f"{name} of {clas} got {total_marks}marks and {per:.2F}% ")
#
#
# if per>60:
#     print("grade A")
# elif per>50 :
#     print("grade B")
# elif per > 40 :
#     print("grade C")
# else :
#     print("fail")
#     print("we are sorry")
# print(type(per))


# QUESTION 3..................
# x=int(input("wnter a number"))
# fact=1
# for x in range(1,x+1):
#     fact*=x
# print(fact)
#..................................


# #QUESTION 4 ................
# list=[]                         #ITEMS TO BE ADDED
# sum=0                           #TOTAL TO BE CALCULATED
# while True:
#     print('''
# 1. Create Bill
# 2. Display Item Price and total bill amount
# 3. Display Total
# 4. Exit
# ''')
#     ch= int(input("Enter your choice "))
#     if ch == 1:
#        # pass
#        print("enter number  order items ")               #do by walris operator
#        item=int(input())
#
#        for x in range(item):
#          print(f"enter name of item {x}  and amount of item {x} ")
#          name = input()
#          amount=int(input())
#          list.extend([name,amount])
#
#     elif ch == 2:
#         # pass
#         print(" bill summary:", list)
#     elif ch == 3:
#         # pass
#         item_amt = list[1::2]               #ITEM AMOUNT KI ALAG LIST
#         # print(item_amt)                   THIS TAKES AMOUNT FOR RESPECTIVE ITEMS
#         # print(type(item_amt))
#                                                  #METHOD 2 direct for loop ki range(0,n,2) isse 2 skip karega?????????
#         for x in item_amt:
#             sum+=x
#         print("Total Bill amount is: ",sum)
#
#     elif ch == 4:
#        break
#     else:
#         print("invailde inputia")

#.................................................
#              QUESTION5 LARGEST ,2ND LARGEST ,SECOND SMALLEST IN A LIST

x = (input("enter elemetns sep by spaces:"))
list = x.split()
print("List is: ",list)

#largest
# max = list[0]
# for i in list:
#     if i>max:
#         max=i
#
# print("Maximum elemtn is: ",max)
#
# #second largest
# max2=list[0]
# for i in list:
#     if (i>max2 and i<max):
#         max2=i
# print("second maximum elemetn: ",max2)

#second smallest
mini=list[0]
# mini2=list[0]

for i in list[1:]:
    if i<mini:
        mini2=mini
        mini=i
    elif  i != mini and (i<mini2 or mini2==mini) :
        mini2 = i
print("second smallest is: ",mini2 )
print("smallest is: ",mini )










