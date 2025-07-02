import sqlite3
import pandas as pd
import tabulate as tb
import datetime



def manager_update(item,order_qty):
    update_stock = sqlite3.connect("foodstock.db")
    c = update_stock.cursor()
    c.execute(f'''
    UPDATE stock SET qty_final =
    (CASE 
    WHEN qty_final = "NULL" THEN  qty_original - {order_qty}                   -- ****IMP****  YHA PE PEHLE IS NULL diya tha but not work
                                                                               -- as ye NULL = string hai not a NULL value 
    WHEN qty_final != "NULL" THEN  qty_final - {order_qty}
    ELSE  qty_final
    END),
    sold_units = sold_units+{order_qty}
    where item_name = "{item}"
    ''')
    update_stock.commit()
    update_stock.close()
        #ya phir dbase se table lao




def make_bill(cid,name_of_customer,lst,size,bill_amt=0) :


    billing = sqlite3.connect("foodstock.db")
    c=billing.cursor()
    for i in range(0,(size-1),2):                                  # yha 3 ki lagah length/2 +1 ayega
        price = c.execute(f"SELECT item_name,unit_price FROM stock where item_name = \"{lst[i]}\"")
        i+=1
        qty2 = float(lst[i])
        # print(price,qty2)                         #price is the cusror object dega

        output = c.fetchall()                        #ye deta list of tuples  [(,),(,)]
        # print(output)
        tup = output[0]                              #humne li ek value of tuple  (,)
        # for x in tup:                            #PEHLE EK BAAR CHAL RHA THA AB DO BAAR CHALRHA HAI ISSE
                                                    #KYUKI PEHLE X == UNIT PRICE HI THA AB ITEM_NAME K LIYE
                                                    #BHI EK BAAR CHALA
        # print(f"item_name:{tup[0]} unit price: {tup[1]} units_ordered: {qty2}")                                #fir us tuple se unit price leli


        bill_amt += (tup[1]*qty2)                                            #YHA PAR UNIT PRICE OF SPECIFIC PRODUCT KA NAAM LAO
        bill_items.append([tup[0], tup[1], qty2,(tup[1]*qty2) ])

        manager_update(tup[0],qty2)

              #send poori lsit ek satth

#orders table mein bhi daala


        c.execute(f'''INSERT INTO orders(cid,cname,oid,item_name, units_ordered)
        VALUES (?,?,?,?,?)''',(cid,name_of_customer,None,tup[0],qty2))                                              #agli baar values put karne mein ? hi dena string ki dikkat aati
        billing.commit()


    # print("total bill",bill_amt)
    c.close()
    return  bill_amt,bill_items
    # bill_amt = price * qty2


def shopping_menu(cid,name_of_cust,bill_amt):
    print("available categories:")
    shopping = sqlite3.connect("foodstock.db")
    meta = shopping.execute('''SELECT id,item_name,category,unit_price,
    (CASE 
    WHEN qty_final = "NULL" then qty_original
    ELSE qty_final
    END) 
    FROM stock''')

                                                                #tabulate se direct print ho jayega varna har row alag se print karani padegi
    print(tb.tabulate(meta,headers=['id', 'item_name', 'category', 'unit_price',"stock_available"],tablefmt='grid'))

# {
    # print("(id, 'item_name', 'category', 'unit_price')")
    # print(type(meta))
                                                          # ye tuple ki form mein ayega so print first element of tuple
    # for row in meta:                                      # see (if later) by print(row)
    #     # print(row)                                       # ye AVIALABLE CATEGORIES PRINT

# }

    shopping.close()

                                                                # ab order select from same category twixe or mainmenu pe waapas jaana
    shop = input("what name and HOW MUCH in spaces??")
    str = shop.split(" ")
    # print(len(str))                                               YE PASS IN BELOW FUNCTION FOR ITERATION LIMIT PROBLEM IN MAKE_BILL

    z ,new_items= make_bill(cid,name_of_cust,str, len(str), bill_amt)
    return  z,new_items

    # qty2 = float(qty)
    # print(str,type(str))



#cid ,oid= 1  ,1          #globally first customer
bill_items =[]
def main():

    print('''********WELCOME to PYTHON ENTERPRISES*******''')
    cid = None
    z=None
    count = 0
    bill_amt = 0
                            #customer id for sales tabel
    cname = ""
    while True:
        choice_user = int(input('''
        1. START SHOPPING: 
        2. Exit
        3. Show total
         '''))
        match choice_user:
            case 1:

                if count==0:
                    print("inital bill: ",bill_amt)
                    cname = input("enter name to be in your bill:")                #pehli baar ayega tabhi  name lenge

#inseert name into sales table with xero bill

                    early_sale = sqlite3.connect("foodstock.db")
                    c = early_sale.cursor()
                    c.execute('''
                            INSERT INTO sales (cname, order_value, order_date)
                            VALUES (?, ?, ?)
                        ''', (cname, 0.0, datetime.date.today()))
                    early_sale.commit()

                    c.execute('SELECT cid FROM sales WHERE cname = ? ORDER BY cid DESC LIMIT 1', (cname,))
                    row = c.fetchone()
                    cid = row[0]
                    early_sale.close()


                if count>=1:                                            #if customer enters menu more than one
                    # new_bill = make_bill()                             #ye nhi kar sakte as baaki arg nhi hai
                    print("Updated bill:",z)
                    bill_amt =z                                              #ab ye pass hoga in makebill()
                                                                             #pehle nhi honrha tha
                count += 1

                z,new_items=shopping_menu(cid,cname,bill_amt)
                bill_amt=z
                # bill_items.extend(new_items)
            case 2:
                # global cid
                # global oid


                enter_sales_info = sqlite3.connect("foodstock.db")
                c = enter_sales_info.cursor()
#ye double values dera iski jagah update karo
                # c.execute(f'''
                # INSERT INTO sales(cname,order_value,order_date) VALUES
                # ('{cname}',{z},'{datetime.date.today()}');
                # ''')

                c.execute('''
                       UPDATE sales
                       SET order_value = ?
                       WHERE cid = ?
                   ''', (bill_amt, cid))
                enter_sales_info.commit()
                c.close()


                # cid+= 1  # jab break press kiya tab naya customer manna
                # oid += 1
                break


            case 3 :
                print(tb.tabulate(bill_items, headers=['item_name', 'unit price', 'units_ordered', 'subtotal'],
                                  tablefmt="pretty"))
                print(tb.tabulate([[" ", " ", "TOTAL:", bill_amt]], tablefmt="pretty"))

    print("THANKYOU for shopping!!!!")


if __name__ == '__main__':
    main()