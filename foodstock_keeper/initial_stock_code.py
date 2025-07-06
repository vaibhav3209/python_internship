
import sqlite3
import pandas as pd
import numpy as np                                          #to convert np.float64 to float etc etc


                                                    # THIS IS AONE TIMEFUNCTION
def stock_table_initial():
    initial_stock_df = pd.DataFrame({"id": range(1, 8),
                                     'item_name': ['Apple', 'Banana', 'Dairymilk', 'Kitkat', 'Oreo', 'Almond',
                                                   'Cashew'],
                                     'category': ['Fruits', 'Fruits', 'Chocolates', 'Chocolates', 'Grocery', 'Grocery',
                                                  'Grocery'],
                                     'unit_price': [50.00, 40.00, 75.00, 45.00, 30.00, 300.00, 350.00],
                                     'qty_original': [100, 70, 50, 50, 200, 100, 80]})

    # # print(initial_stock_df)


    food_stock = sqlite3.connect("foodstock.db")
    food_stock.executescript('''
     -- DROP TABLE IF EXISTS stock;                -- DROP KIYA TO JOB GAYIIIIIII...........
    CREATE TABLE stock(
    id  INT ,
    item_name TEXT PRIMARY KEY,
    category TEXT,
    unit_price FLOAT,
    qty_original INT,
    qty_final INT DEFAULT "NULL");

    ''')
    # food_stock.close()

                                                            # # #now put it into initial_stock table

    query = "INSERT INTO stock(id,item_name,category,unit_price,qty_original) VALUES (?,?,?,?,?)"
    for i in range(7):
        row = initial_stock_df.loc[i, :]  # row is a series
        row2 = row.tolist()
        row2 = [
            float(x) if isinstance(x, (np.float32, np.float64)) else int(x) if isinstance(x,
                                                                                          (np.int32, np.int64)) else x
            for x in row2]
        row3 = tuple(row2)  # series->list->tuple mein karo
        print(row3, "\n")
        food_stock.execute(query, row3)

    food_stock.commit()
    food_stock.close()


def customers_table_initial():
    make_sales = sqlite3.connect("foodstock.db")
    c= make_sales.cursor()

    c.executescript(''' -- drop table if exists customers;
    CREATE TABLE  customers(
    cid INTEGER PRIMARY KEY AUTOINCREMENT,
    cname TEXT,
    order_date DATE
    
    );
    ''')

    make_sales.close()


def orders_table_initial():
        make_orders = sqlite3.connect("foodstock.db")
        c = make_orders.cursor()

        c.executescript('''
        -- drop table  if exists orders;
        CREATE TABLE orders (
        oid INTEGER ,     
        cid INTEGER ,
        
        item_name TEXT,
        units_ordered INT,
        order_date DATE,
        PRIMARY KEY (oid),
        FOREIGN KEY (cid,order_date) REFERENCES customers(cid,order_date)
                   
        );
        ''')
        make_orders.close()

def main ():

    # stock_table_initial()
    # customers_table_initial()
    # orders_table_initial()##


if __name__ == '__main__':
    main()