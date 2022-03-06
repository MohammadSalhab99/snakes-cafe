def menu():
    
   print( """
    **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
    
    
    """)
   listofmenu={"Wings","Cookies" ,"Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie" , "Coffee", "Tea","Unicorn Tears"}
   order =""
   list = []
   while order !="quit":
        order=input(">")
        if order=="quit":
            break
        if order not in listofmenu:
            print("Please select form the menu")
            continue
        list.append(order)
        
        print(f'** {list.count(order)} order of {order} have been added to your meal **')
   

menu()