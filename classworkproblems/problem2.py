from datetime import date, datetime

def calculate_Ticket_based_onage(birthdate):
    currentdate = date.today()
    age = currentdate.year - birthdate.year

    if age >= 16 and age <=60:
        amount = 75
    elif age<=15 or age >= 60:  
        amount = 50
    return amount  

def inputoftheuser():
    name=input("Enter your Name : ")
    birthdate_str = input("Please enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")  
    ticket_amount = calculate_Ticket_based_onage(birthdate)  
    print("Your ticket amount is:", ticket_amount)

inputoftheuser()  
