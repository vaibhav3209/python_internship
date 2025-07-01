import sqlite3
import pandas as pd

def check_stock_func():
    final_stock = c.execute('''SELECT *,
           CASE 
           WHEN qty_final BETWEEN 0 AND 15 THEN "low stock"
           WHEN qty_final ==0 THEN " stock finished "
           ELSE "adequate stock"
           END AS "stock info"
           FROM stock''')
    data = pd.DataFrame(final_stock,
                        columns=['id', 'item_name', 'category', 'unit_price', 'qty_original', 'qty_final', "units_sold",
                                 "stock_info"])
    print(data)


password = input("WELCOME SAA...enter your password: ")
if password == 'iloveindia':
    stock_check = sqlite3.connect("foodstock.db")
    c = stock_check.cursor()
    check_stock_func()                                                      #called above
    c.close()
else :
    input("wrong password,,BETTER LUCK NEXT TIME! ")