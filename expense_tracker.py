expense_field_value = {}
income_field_value = {}


while True:
     print ("Welcome to Expense Tracker\n1)Expenses   2)Income\n3)Report     4)Exit")
     choice =int(input("Enter your choice: "))

     if choice == 1:
        while True:
          ex_choice =  int (input(("1) Add expense field     2) Add expense amount  3)Back\nEnter your choice: ")))

          if ex_choice == 1:
             field_name = input("Enter expense field name: ").lower()
             expense_field_value[field_name] = 0
             print(f"Expense field '{field_name}' added.")

          elif ex_choice == 2:
              print(f"Existing expense fields:{expense_field_value.keys()}")
              field_name = input("Enter expense field name: ").lower()
              if field_name in expense_field_value:
                amount = float(input("Enter expense amount: "))
                expense_field_value[field_name] += amount
                print(f"Added {amount} to '{field_name}'. Total is now {expense_field_value[field_name]}.")
              else:
                print(f"Expense field '{field_name}' does not exist.")
          elif ex_choice == 3:
            break        

     elif choice == 2:
        while True:
          in_choice =  int (input(("1) Add income field     2) Add income amount   3)Back\nEnter your choice: ")))
          if in_choice == 1:
             field_name = input("Enter income field name: ").lower()
             income_field_value[field_name] = 0
             print(f"Income field '{field_name}' added.")  

          elif in_choice == 2:
            print(f"Existing income fields:{income_field_value.keys()}")
            field_name = input("Enter income field name: ").lower()
            if field_name in income_field_value:
                amount = float(input("Enter income amount: "))
                income_field_value[field_name] += amount
                print(f"Added {amount} to '{field_name}'. Total is now {income_field_value[field_name]}.")
            else:
                print(f"Income field '{field_name}' does not exist.")
          elif in_choice == 3:
            break

     elif choice == 3:
        while True:
          re_choice = int(input("1) Expense Report    2) Income Report  3)Combined Comaprison Report  4)Back\nEnter your choice: "))

          if re_choice == 1:
           print("Expense Report:")
           for field, amount in expense_field_value.items():
             print(f"{field}: {amount}")
             
           total_expense = sum(expense_field_value.values())
           print(f"Total Expense: {total_expense}")  

          elif re_choice == 2:
           print("Income Report:")
           for field, amount in income_field_value.items():
             print(f"{field}: {amount}")
             
           total_income = sum(income_field_value.values())
           print(f"Total Income: {total_income}")
           
          elif re_choice == 3:    
            print("Combined Report:")
            print("Expenses:")
            for field, amount in expense_field_value.items():
               print(f"{field}: {amount}")
               print("Income:")
            for field, amount in income_field_value.items():
               print(f"{field}: {amount}")
        
            total_expense = sum(expense_field_value.values())
            total_income = sum(income_field_value.values())
            difference = total_income - total_expense
            if difference > 0:
                print(f"You have saved {difference} BDT till now.")
            else:
                print(f"You are trailing with {difference} BDT till now.")
          elif re_choice == 4:
            break

     elif choice == 4:
        print("Exiting Expense Tracker. Allah Hafez!")
        exit()
     else:
        print("Invalid choice. Please try again.")    