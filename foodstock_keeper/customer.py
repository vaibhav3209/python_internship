# # import manager
# import sqlite3
# from foodstock_keeper.manager import initial_stock_df
#
# choice_user1 = int(input())
# if choice_user1 == 1:
#     ...#customer ka code
#     while True:
#         print('''
#     1. SELECT CATEGORY of products:
#     2. Display Total
#     3. Exit
#     ''')
#         bill = 0
#         ch = int(input())
#         if ch == 1:
#             print("""whaddoo u wanna buy::
#             a. GROCERY
#             b. CHOCOLATES
#             c. FRUITS""")
#             category = input()
#             if category == 'a':
#                 ...#uska dataframe aa jaye
#                 result = (initial_stock_df[initial_stock_df["category"] == "Grocery"]).iloc[:, 1:5:2]
#                 print("available groceries:\n",result)
#                 shop = input("what and HOW MUCH in spaces??")
#                 prod_name , qty = shop.split(" ")
#                 qty2 = float(qty)
#
#
#                 bill = (qty2)*(result[result["item_name"]==f"{prod_name}"]).loc[:,"unit_price"]
#                 print("total amount:",bill)
#
#                 update_stock = sqlite3.connect("foodstock.db")
#                 update_stock.execute(f'''
#                 UPDATE stock SET
#                 qty_final = qty_original - {qty2},
#                 sold_units = {qty2}
#                 where item_name = "{prod_name}"
#                 ''')
#                 update_stock.commit()
#                 update_stock.close()
#                     #ya phir dbase se table lao
#
#             if category == 'b':
#                 ...#uska dataframe aa jaye
#                 print("available chocolates:\n",
#                       (initial_stock_df[initial_stock_df["category"] == "Chocolates"]).iloc[:, 1:5:2])
#             if category == 'c':
#                 ...#uska dataframe aa jaye
#                 print("available fruits:\n",
#                       (initial_stock_df[initial_stock_df["category"] == "Fruits"]).iloc[:, 1:5:2])
#
#
#
#
# else :
#     ...#manager ka code  neeche wale ko bhi isi mein dalo
#     password = input("WELCOME SAA...enter your password: ")
#     if password == 'iloveindia':
#         ...#import manager file
#     else :
#         input("wrong password,,BETTER LUCK NEXT TIME! ")
#
#
#
