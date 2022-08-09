import OOP as f
print('_'*10,'','_'*10)
print('Who are you?\na) Customer\nb) Administrator\nc) Delivery Rider')
Choice=input()
if Choice=='a' or Choice=='A':
    cust=f.Customer()
    print(f'What do you want to do:\n'
          f'a)Shop Some interesting item\n'
          f'b)See History of your Orders')
    in1=input('Enter Choice(a or b): ')
    if in1=='a' or in1=='A':
        cust.Show_Choose_And_Print()
        while True:
            print(f'Do you want to:\n'
                  f'a) See Cart\n'
                  f'b) Add to cart\n'
                  f'c) Remove from Cart\n'
                  f'd) Proceed to Checkout')
            Decision=input('Your Choice(a,b,c): ')
            if Decision=='a' or Decision=='A':
                cust.Show_Shopping_Cart()
                continue
            elif Decision=='b' or Decision=='B':
                cust.Add_To_ShoppingCart()
                continue
            elif Decision=='c' or Decision=='C':
                cust.Remove_From_ShoppingCart()
                continue
            elif Decision=='D' or Decision=='d':
                cust.Final_Formalities()
                break
            else:
                print('Invalid Input')
                continue
    elif in1=='b' or in1=='B':
        cust.History_Provider()
elif Choice=='b'or Choice=='B':
    Admin=f.Administrator()
    if Admin.truth_value==True:
        print('\t\tWelcome Administrator of ')
        while True:
            print(f'Which Operation do you want to execute?\n'
                  f'a) View Notification\n'
                  f'b) View FeedBacks\n'
                  f'c) Manage Stock\n'
                  f'd) Manage Employees')
            choice=input('Enter your Choice(a,b,c,d): ')
            if choice=='a' or choice=='A':
                Admin.notification()
            elif choice == 'b' or choice == 'B':
                Admin.Feedback_Checker()
            elif choice=='c' or choice=='C':
                Admin.Manage_Stock()
            elif choice=='d' or choice=='D':
                Admin.Manage_EmployeesForDelivery()
            admin_ch=input('What do you want to do?\n'
                           'a) Continue in application\n'
                           'b) LogOut\n'
                           'Your Choice(a,b): ')
            if admin_ch=='a' or admin_ch=='A':
                continue
            elif admin_ch=='b' or admin_ch=='B':
                break
    else:
        print('Enter Valid Credentials!')
elif Choice=='c' or Choice=='C':
    Employee=f.Delivery_Employee()
    Employee.Take_Info()
    while True:
        print(f'What do you want to do?\n'
              f'a) Inspect Balance\n'
              f'b) See Orders to be Delivered')
        choice=input('Enter Choice(a,b): ')
        if choice=='a' or choice=='A':
            Employee.Show_Balance()
        elif choice=='b' or choice=='B':
            Employee.Display_order()
        else:
            print('invalid choice')
        ch_1 = input(f'What do you want to do?\n'
                     f'a) Continue in your ID\n'
                     f'b) Log Out'
                     f'Enter choice(a or b):')
        if ch_1 == 'a' or ch_1 == 'A':
            continue
        elif ch_1 == 'b' or ch_1 == 'B':
            break