import sqlite3
import pandas as pd
import tabulate as tb


#COLOR CODES
#  {                          but this need to fetch every row to more complex hoga
# \033[91m {}\033[00m  red code 91
# \033[92m {}\033[00m   green code 92
# \033[93m {}\033[00m   yellow code 93
#  }

def restock_table():
    restock = sqlite3.connect("foodstock.db")
    c = restock.cursor()
    c.execute('''
                        UPDATE stock SET
                         qty_final = "NULL" ,
                         sold_units = "NULL"
                        ''')
    restock.commit()
    restock.close()


def check_stock_func():
    stock_check = sqlite3.connect("foodstock.db")
    c = stock_check.cursor()

    final_stock = c.execute('''SELECT *,
           CASE 
           WHEN qty_final BETWEEN 0 AND 15 THEN "low stock"
           WHEN qty_final ==0 THEN " stock finished "
           WHEN qty_final == "NULL" THEN  "not ordered yet"
           ELSE "adequate stock"
           END AS "stock info"
           FROM stock''')

    print(tb.tabulate(final_stock,headers=['id', 'item_name', 'category', 'unit_price', 'qty_original', 'qty_final', "units_sold",
                                "stock_info"],tablefmt="grid"))

    c.close()
                                        # IF TABULATE NA LAGARE TO YE CODE LIKHNA
    #  {
        # data = pd.DataFrame(final_stock,
        #                     columns=['id', 'item_name', 'category', 'unit_price', 'qty_original', 'qty_final', "units_sold",
        #                              "stock_info"])
        # print(data)
    #  }



def main():##

    password = input("WELCOME SAA...enter your password: ")
    if password == 'iloveindia':
        while True:
            ch3 = int(input('''whaddooo wanna do::
                              1-->>restock table to original(at start of month)
                              2-->>see available stock
                              3-->>see sales data
                              4-->> exit as manager\n'''))

            match ch3:
                case 1:
                    ...
                    restock_table()

                case 2:
                    ...
                    check_stock_func()  # called above

                case 3:
                    ...
                    #isko graph mein banana  x,y,points leke straight line hai ya nhi matlab sales drop hori
                    #isi se total sales ,,,total sales by category ,,,most sold products
                    #MATPLOTLIB SE SALES GRAPH  bhi bna sakte

                    # print("total sales by each category per day:")
                    # data = sqlite3.connect("foodstock.db")
                    # c = data.cursor()
                    # c.execute('''SELECT order_date,category,sum(units_ordered * unit_price) as sales,
                    #             count(item_name) as units_sold
                    #                                   FROM orders o
                    #                                   JOIN stock s USING (item_name)
                    #                                   WHERE order_date IS NOT NULL
                    #                                   GROUP BY order_date,category''')
                    # c.close()

                case 4:
                    break

    else :
        input("wrong password,,BETTER LUCK NEXT TIME! ")




if __name__ == '__main__':
    main()