# Expense Tracker Project

expenseslist=[] #list of expenses in form of dictionary
print("Welcome to Expense Tracker : Khrcha Kam Karo ")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice= int(input("Please Enter The Choice"))

#ADD Expense
    if(choice==1):
       date= input("Enter The Date?:")
       category= input("Enter The Category? (Food, Bill, Shopping, Transport, Books, Other):")
       description= input("Give Detail:")
       amount= float(input("Enter The Amount:"))

       expense= {
           "date": date,
           "category": category,
           "description": description,
           "amount": amount
       }

       expenseslist.append(expense)
       print("\n DONE. Expense is added succesfully")

#2. VIEW ALL EXPENSES
    elif(choice == 2):
        if( len(expenseslist)==0):
            print("No Expenses Added")
        else:
            print("====Your All Expense====")
            count= 1
            for eachspendings in expenseslist:
                print(f"Spending Number {count} ->{eachspendings["date"]}, {eachspendings["category"]}, {eachspendings["description"]}, {eachspendings["amount"]}")
                count= count+1

#3. VIEW TOATL SPENDING
    elif(choice ==3):
        total= 0
        for eachspendings in expenseslist:
            total= total + eachspendings["amount"]

            print("\n TOTAL SPENDINGS=", total)

#4. EXIT
    elif(choice == 4):
        print("THANK YOU FOR USING OUR SYSTEM HAVE NICE DAY ")
        
        break

    else:
        print("INVALID CHOICE")

                    
            

