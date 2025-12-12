#define the menu of the hotel
menu = { 
    "Pasta": 30, 
    'pizza' : 150,
    'burger': 100,
    'salad': 50,
    "soda": 20,
    "coffee": 40,
    "tea": 30,
    'dessert': 70,
    'steak': 200,
    'fish': 180,
    'chicken': 120,
    'rice': 60,
    'fries': 80,
    'ice cream': 90,
    'juice': 25,
}

#greet
print("Welcome to the shriji resturant")
print("Pasta: Rs30\npizza : Rs150\nburger: Rs100\nsalad: Rs50\nsoda: Rs20\ncoffee:Rs 40\ntea: Rs30\ndessert: Rs70\nsteak: Rs200\nfish: Rs180\nchicken: Rs120\nrice: Rs60\nfries: Rs80\nice cream: Rs90\njuice: Rs25")

order_total = 0
item_1 = input("Enter the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added to your order")
    
else:
    print(f"ordered Item {item_1}is not available ")
     
Another_order = input("Do you want to another Item? (yes/no) = ") 
if Another_order == "yes":
        item_2 = input("enter the name of second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item{item_2} has been added to your order")
        else:
            print(f"ordered Item {item_2} is not available")


            
          
            
print(f"the total amount of Items to pay is : {order_total}")    
      
             