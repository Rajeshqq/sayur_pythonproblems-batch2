#Lets create a python application for managing a restaurant billing system
#Features
#Add new items to menu with price (owner - idly : 10rs)
#Calculate bill for each customer based on their order
#Bill should include tax, tip 
#Ability to run promotion and give discount
#nteractive with user - get inputs, print results`
foodItemsCost = {'idly':5,'dosa':10,'poori':20,'chapathi':30}
userno=0
orderedfood=[]
orderedquantity=[]
promocode="SAYUR100"
discount=10
def addNewItems():
    itemsCount=int(input("enter the items you going to enter:"))

    for i in range(itemsCount):
        name = input("Enter food name: ")
        cost = input("Enter food cost: ")

        foodItemsCost[name] = cost
def foodMenu():
    print(foodItemsCost)
def orderFood():
    while(1):
        option=input("you want to order food(y/n):")
        if(option=="y"):
            food=input("enter the food you want to eat : ")
            quantity=int(input("enter the quantity yo want : "))
            if food in foodItemsCost:
                orderedfood.append(food)
                orderedquantity.append(quantity)
            else:
                print("we dont have that food")
        else:
            break
        
def bill():
    subtotal=0
    discount_amount=0
    for i in range(len(orderedfood)):
        food=orderedfood[i]
        quantity=orderedquantity[i]
        if food in foodItemsCost:
            subtotal+=foodItemsCost[food]*quantity
    yorn=input("do you have a promo code (y/n) : ")
    if yorn=="y":
        getthepromo=input("enter the promocode : ")
        if getthepromo==promocode:
            discount_amount=subtotal*(discount/100)
            total=subtotal-discount_amount
        else:
            print("invalid promocode")
            total=subtotal
    else:
        total=subtotal
    print("-------------bill-------------")
    for i in range(len(orderedfood)):
        print(f"{orderedfood[i]} : {orderedquantity[i]} x {foodItemsCost[orderedfood[i]]} = {foodItemsCost[orderedfood[i]] * orderedquantity[i]}")
        print(f"Subtotal: {subtotal}")
        if discount_amount>0:
            print(f"Discount (-{discount}%): {discount_amount}")
        print(f"Total: {total}")
    print("-------------------------------")
           
def main():
    while True:
        print("\n--- Restaurant Billing System ---")
        print("1. Add New Items to Menu")
        print("2. View Menu")
        print("3. Order Food")
        print("4. Generate Bill")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addNewItems()
        elif choice == "2":
            foodMenu()
        elif choice == "3":
            orderFood()
        elif choice == "4":
            bill()
        elif choice == "5":
            print("Thank you Have a great day!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


    
    
