from abc import ABC, abstractmethod
from datetime import date
import Exception_Classes as Ex

class User(ABC):
    def __init__(self):
        while True:
            try:
                self.name = input('Enter name: ')
                self.mail = input('Enter email: ')
                self.password = input('Enter password: ')
                if self.name=='' or self.mail=='' or self.password=='':
                    raise Ex.NoValue
            except Ex.NoValue:
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break

    @abstractmethod
    def SaveToFile(self):
        pass

    def CheckInFile(self, y):
        with open(y, 'r') as k:
            lines = k.readlines()
            for record in lines:
                if self.mail in record and self.password in record:
                    return True
                elif self.mail in record and self.password not in record:
                    return 'invalid'
                else:
                    return False

class Customer(User):
    def __init__(self):
        self.Cart = ShoppingCart()
        while True:
            super().__init__()
            self.truth_value = super().CheckInFile('store.txt')
            if self.truth_value == True:
                print('Your account is already present\n')
                self.Take_Address()
                break
            elif self.truth_value == False:                          #interpreter iskay if elif me ghus hi nahi raha
                self.SaveToFile()
                print('Your account has been created successfully')
                self.Take_Address()
                break
            elif self.truth_value == 'invalid':
                print('Enter correct password')

    def SaveToFile(self):
        with open('store.txt', 'a+') as f:
            f.write(self.name + ',' + self.mail + ',' + self.password + '\n')

    def Take_Address(self):
        while True:
            try:
                self.Address = input('Enter your Address: ')
                if self.Address == '':
                    raise Ex.NoValue
            except Ex.NoValue:
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            else:
                break

    def Show_Choose_And_Print(self):
        self.Cart.Show_Items()
        self.Cart.Choose_Domain()

    def Show_Shopping_Cart(self):
        self.Cart.Show_Cart()

    def Add_To_ShoppingCart(self):
        Additional_Items={}
        Prod_Pr_dic={}
        Chose_Product_Dict={}
        Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
        s_no=1
        for Domain in Products.Domain_Products_Dict:
            print(f'{s_no}. {Domain}')
            s_no+=1
        while True:
            try:
                domain_choice=input('Enter no. of domain you want to add products from: ')
                if domain_choice=='':
                    raise Ex.NoValue
                elif domain_choice.isalpha():
                    raise Ex.AlphabeticError
            except Ex.NoValue:
                print('Empty text is not acceptable\n'
                      'Kindly Enter something')
                continue
            except Ex.AlphabeticError:
                print('Enter a number please')
                continue
            else:
                break
        if domain_choice == '1':
            dom_prods=Products.Domain_Products_Dict['Clothing']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='2':
            dom_prods=Products.Domain_Products_Dict['Electronics']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='3':
            dom_prods=Products.Domain_Products_Dict['Grocery']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        elif domain_choice=='4':
            dom_prods=Products.Domain_Products_Dict['Fruits']
            self.AddCart_Supporter(dom_prods, Prod_Pr_dic, Chose_Product_Dict, Additional_Items)
        else:
            print(f'Enter Valid Choice')

    def AddCart_Supporter(self,dom_prods,Prod_Pr_dic,Chose_Product_Dict,Additional_Items):
        count = 1
        countt = 1
        print('               %-15s%-17s%-13s' % ('S.no.', 'Product', 'Price'))
        for Prod_Price_Lst in dom_prods:
            print('                %-14s%-17s%-15s' % (str(count) + '.', Prod_Price_Lst[0], Prod_Price_Lst[1] + '/-'))
            count += 1
            Prod_Pr_dic[Prod_Price_Lst[0]] = eval(Prod_Price_Lst[1])
        for Product in Prod_Pr_dic:
            Chose_Product_Dict[countt] = Product
            countt += 1
        while True:
            print(f'Enter Product number you want to add in cart: ', end='')
            Pr_Choice = int(input())
            Prod = Chose_Product_Dict[Pr_Choice]
            Quant = int(input(f'Enter Quantity of {Prod} to be added: '))
            Additional_Items[Prod] = Quant
            decide = input('Do you want to continue Shopping(y/n): ')
            if decide == 'y' or decide == 'Y':
                continue
            elif decide == 'N' or decide == 'n':
                self.Cart.Product_Quantity=Order.Give_Cart_Dict()
                self.Cart.Product_Quantity.update(Additional_Items)
                self.Cart.Write_CustomerChosenProduct_Quantity_Dict_InFile()
                break

    def Remove_From_ShoppingCart(self):
            self.Cart.Remove_from_Cart()

    def Final_Formalities(self):
        self.Cart.FinalOrderAndFeedback(self.name, self.mail, self.Address)

    def History_Provider(self):
        with open('Cust_Order_History.txt','r') as f:
            print(f'Mr/Ms {self.name}, Your Order History is shown Below:')
            lines=f.readlines()
            for line in lines:
                line=eval(line)
                if self.mail in line[0]:
                    print(line[0])

class ShoppingCart:
    def __init__(self):
        self.Product_Quantity = {}
        self.Order = Order()

    def choose_Product(self):
        while True:
            try:
                ask_user = int(input('Enter which product number do you want to choose: '))
                if ask_user in Products.Choose_Prod_Dict:
                    final_product = Products.Choose_Prod_Dict[ask_user]
                    print('Enter the quantity of ', final_product, ':', end='')
                    choosee = int(input())
                    self.Product_Quantity[final_product] = choosee
                    print('Do you want to continue shopping?(y/n) ', end='')
                    choice = input()
                    if choice == 'y' or choice == 'Y':
                        continue
                    elif choice == 'n' or choice == 'N':
                        self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
                        break
                else:
                    print('Please enter valid choice')
            except:
                print(f'Please enter integer')

    def Show_Cart(self):
        count = 1
        print('Item(s) Included in your cart are: ')
        with open ('CustomerChosenProduct_Quantity_Dict.txt','r') as f:
            items_in_cart=eval(f.read())
            for items in items_in_cart.items():
                print(f'{count}. {items[1]} {str(items[0])}(s)')
                count+=1

    def Remove_from_Cart(self):
        self.Show_Cart()
        ProdName = input('Enter name of product to be removed: ')
        QuantityToBeRemoved = input(f'Enter Quantity of {ProdName} to be removed,\n'
                                    f'Type All to completely remove {ProdName}: ')
        if QuantityToBeRemoved == 'All' or QuantityToBeRemoved == 'all' or QuantityToBeRemoved == 'ALL' or QuantityToBeRemoved == 'all':
            self.Product_Quantity=Order.Give_Cart_Dict()
            QuantityOfRemovedItems=self.Product_Quantity[ProdName]
            Removeditems = self.Product_Quantity.pop(ProdName)
            print(f'{Removeditems} {ProdName} is/are removed from your cart')
            self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
            self.Order.UpdateStock('Remove from Cart',ProdName,QuantityOfRemovedItems)
        elif QuantityToBeRemoved.isdigit():
            OriginalChosenQuantity=self.Product_Quantity[ProdName]
            self.Product_Quantity[ProdName]=OriginalChosenQuantity-int(QuantityToBeRemoved)
            self.Write_CustomerChosenProduct_Quantity_Dict_InFile()
            self.Order.UpdateStock('Remove from Cart',ProdName,int(QuantityToBeRemoved))

    def Choose_Domain(self):
        count = 1
        countt = 1
        choice = int(input('Enter the number of domain you want to choose products from :'))
        if choice in Products.Choose_Domain_Dict:
            final = Products.Choose_Domain_Dict[choice]
            display_prod = Products.Domain_Products_Dict[final]
            print('               %-15s%-17s%-13s' % ('S.no.', 'Product', 'Price'))
            for Pair_Product in display_prod:
                print('                %-14s%-17s%-15s' % (str(count) + '.', Pair_Product[0], Pair_Product[1] + '/-'))
                count += 1
                Products.Prod_Price_dict[Pair_Product[0]] = eval(Pair_Product[1])
            for Product in Products.Prod_Price_dict:
                Products.Choose_Prod_Dict[countt] = Product
                countt += 1
            ShoppingCart.choose_Product(self)
        else:
            print('Invalid input')

    def Show_Items(self):
        self.Order.From_Product()

    def FinalOrderAndFeedback(self, name, email, Address):
        self.Order.Checkout_Slip(name, email, Address)
        self.Order.takefeedback()

    def Write_CustomerChosenProduct_Quantity_Dict_InFile(self):
        with open('CustomerChosenProduct_Quantity_Dict.txt', 'w') as f:
            f.write(str(self.Product_Quantity))

class Order:
    def __init__(self):
        self.prod = Products()
        self.prod.Give_Prod_Quantity_Dict()
        self.shipping = Shipping_Details()
        self.prod.Final_ProductPriceDict_maker()

    def __str__(self):
        count = 1
        self.strg_ord += ' '*15+'%-9s%-15s%-13s%-16s%s' % ('Sno.', 'Product', 'Price', 'Quantity', 'Amount\n')
        self.Amount_list = []
        shopping_dict=Order.Give_Cart_Dict()
        for item in shopping_dict:
            self.strg_ord += ' '*16+'%-8s%-15s%-16s%-13s%s' % (
                str(count) + '.', item, str(Products.All_Product_Prices_Dict[item]) + '/-', str(shopping_dict[item]),
                str(Products.All_Product_Prices_Dict[item] * shopping_dict[item]) + '\n')
            self.Amount_list.append(shopping_dict[item] * Products.All_Product_Prices_Dict[item])
            count += 1
        self.strg_ord += self.Cal_total_payment()
        return self.strg_ord

    def Customer_Details_Stringer(self, name, email, Address):
        self.today = date.today()
        self.Date = self.today.strftime("%B %d, %Y")
        Details = ''
        Details += f'Date: {str(self.Date)}\n'
        Details += f'Name: {name}\nEmail: {email}\nAddress: {Address}\n'
        return Details

    def Checkout_Slip(self, name, email, Address):
        user_Details = self.Customer_Details_Stringer(name, email, Address) + self.shipping.ConfirmationMail(email)
        self.strg_ord = ''
        self.strg_ord += user_Details
        print(self)
        self.Payment = Payment()
        if self.Payment.Pay == 'a' or self.Payment.Pay == 'A':
            self.Payment.Cash_On_Delivery(Address)
        else:
            self.Payment.Online_Payment()
        self.SlipInFile()
        self.UpdateStock('Add to Cart')

    def SlipInFile(self):
        self.Write_In_File('Cust_Order_History.txt')
        self.Write_In_File('Orders.txt')

    def Write_In_File(self,filename):
        with open(filename, 'a') as f:
            self.ListOfOrder = []
            self.ListOfOrder.append(self.strg_ord)
            f.write(str(self.ListOfOrder) + '\n')

    def Cal_total_payment(self):
        self.summ_list = sum(self.Amount_list)
        string = 'Total Payment is :' + str(self.summ_list) + 'Rs\nTHANK YOU FOR SHOPPING!!\n'
        return string

    def takefeedback(self):
        print(f'Do you want to give any feedback ?')
        about_feedback = input(f'Your choice (Y) or (N):')
        if about_feedback == 'y' or about_feedback == 'Y':
            feedbackchoice = input(f'a)Did you have a good experience?(a)\n'
                                   f'b)Did you have a bad experience?(b)\n'
                                   f'Your choice: ')
            if feedbackchoice == 'a' or feedbackchoice=='A':
                Order.Write_Feedback('Goodfeedbacks.txt')
            elif feedbackchoice == 'b' or feedbackchoice=='B':
                Order.Write_Feedback('Badfeedbacks.txt')
        elif about_feedback == 'N' or about_feedback == 'n':
            return
        else:
            print('Invalid Input')
            return

    @staticmethod
    def Write_Feedback(filename):
        feedback = input('Your feedback: ')
        with open(filename, 'a+') as f:
            f.write(feedback + '\n')
        print('Thank you for your feedback')

    def UpdateStock(self, Purpose='Add to Cart',Prod=None,Quantity=None):
        if Purpose=='Add to Cart' and Prod==None and Quantity==None:
            Cust_Dict = Order.Give_Cart_Dict()
            for Prod_s in Cust_Dict:
                Sold_Quantity = Cust_Dict[Prod_s]
                Stock_Quantity = Products.Stock_Prod_Quantity_dict[Prod_s]
                Products.Stock_Prod_Quantity_dict[Prod_s] = Stock_Quantity - Sold_Quantity
        else:
            Stock_Quantity=Products.Stock_Prod_Quantity_dict[Prod]
            Products.Stock_Prod_Quantity_dict[Prod] = Stock_Quantity + int(Quantity)
        self.prod.reset_Quantity()

    @classmethod
    def Give_Cart_Dict(cls):
        with open('CustomerChosenProduct_Quantity_Dict.txt', 'r') as f:
            Cust_Dict = eval(f.read())
            return Cust_Dict

    def From_Product(self):
        self.prod.Show_Domain()

class Products:
    Domain_Products_Dict = {}
    Prod_Price_dict = {}
    Choose_Prod_Dict = {}
    Choose_Domain_Dict = {}
    Stock_Prod_Quantity_dict = {}
    All_Product_Prices_Dict={}

    def Show_Domain(self):
        S_no = 1
        Dict = Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
        for Domains in Dict:
            print(str(S_no) + ') ' + Domains)
            Products.Choose_Domain_Dict[S_no] = Domains
            S_no += 1

    @staticmethod
    def Give_Domain_Products_Dict(dic):
        Item_List = []
        with open('Products.txt', 'r+') as P:
            lines = P.readlines()
            for line in lines:
                line = line.strip('\n')
                Domain_Product_List = line.split(';')
                dic[Domain_Product_List[0]] = Domain_Product_List[1]
            for Item in dic.items():
                Product_Price = Item[1].split(',')
                for Procut_Price_string in Product_Price:
                    ItemAndPrice = Procut_Price_string.split(':')
                    Item_List.append(ItemAndPrice)
                    dic[Item[0]] = Item_List
                Item_List = []
        return dic

    @classmethod
    def Give_Prod_Quantity_Dict(cls):
        with open('Quantity.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                linep = line.strip()
                lineps = linep.split(':')
                Products.Stock_Prod_Quantity_dict[lineps[0]] = eval(lineps[1])
            return Products.Stock_Prod_Quantity_dict

    @classmethod
    def reset_Quantity(cls):
        with open('Quantity.txt', 'w') as f:
            for item in Products.Stock_Prod_Quantity_dict.items():
                strg = str(item[0]) + ':' + str(item[1]) + '\n'
                f.write(strg)

    @classmethod
    def Final_ProductPriceDict_maker(cls):
        with open('Products.txt','r') as f:
            Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
            for Domains  in Products.Domain_Products_Dict:
                Prod_TwoDimensionLst=Products.Domain_Products_Dict[Domains]
                for Pro_Price in Prod_TwoDimensionLst:
                    Products.All_Product_Prices_Dict[Pro_Price[0]]=eval(Pro_Price[1])

class Administrator(User):
    def __init__(self):
        super().__init__()
        self.Prod = Products()
        self.truth_value = self.CheckInFile()
        Products.Give_Prod_Quantity_Dict()
        self.Employee=Delivery_Employee()

    def CheckInFile(self, y='Admin Credentials.txt'):
        with open(y, 'r') as f:
            File_Strg = f.read()
            if self.name in File_Strg and self.mail in File_Strg and self.password in File_Strg:
                return True
            return False

    def SaveToFile(self):
        pass

    def View_Stock(self):
        for items in Products.Stock_Prod_Quantity_dict.items():
            print(f'{items[1]} {items[0]} are remaining.')

    @classmethod
    def notification(cls):
        print('NOTIFICATIONS')
        maximum = []
        for value in Products.Stock_Prod_Quantity_dict.values():
            maximum.append(value)
        if min(maximum) > 10:
            print('All items are well Stocked.')
        else:
            for item in Products.Stock_Prod_Quantity_dict.items():
                if item[1] <= 10:
                    print(f'Only {item[1]} {item[0]} are left ')

    def Remove_Stock(self):
        self.View_Stock()
        print('Which Product do you want to remove?\n')
        Prod_name = input()
        QuantityToBeRemoved = int(input(f'Enter number of {Prod_name} to be removed: '))
        f = Products.Stock_Prod_Quantity_dict[Prod_name]
        Products.Stock_Prod_Quantity_dict[Prod_name] = f - QuantityToBeRemoved
        print(f'{QuantityToBeRemoved} {Prod_name} is/are removed from stock')
        Products.reset_Quantity()

    def Feedback_Checker(self):
        print('Which Feedback do you want to examine?\na)Good\nb)Bad\nYour Choice(a or b):',end='')
        choice = input()
        if choice == 'a' or choice == 'A':
            with open('Goodfeedbacks.txt', 'r') as f:
                print('Good Feedbacks:\n' + '*' * 15)
                print(f.read())
        elif choice == 'b' or choice == 'B':
            with open('Badfeedbacks.txt', 'r') as f:
                print('Bad Feedbacks:\n' + '*' * 14)
                print(f.read())
        else:
            print('Invalid Choice')
            return

    def Add_Stock(self):
        self.View_Stock()
        print('Which Product do you want to add?\n')
        Prod_name = input()
        QuantityToBeAdded = int(input(f'Enter number of {Prod_name} to be added: '))
        f = Products.Stock_Prod_Quantity_dict[Prod_name]
        Products.Stock_Prod_Quantity_dict[Prod_name] = f + QuantityToBeAdded
        print(f'{QuantityToBeAdded} {Prod_name} is/are added to stock')
        Products.reset_Quantity()

    def Manage_EmployeesForDelivery(self):
        while True:
            print(f'Select an operation:\n'
                  f'a) Show Employees\n'
                  f'b) Send Bonus\n'
                  f'c) Send Salary')
            Admin_Choice=input('Enter Your choice(a,b,c): ')
            if Admin_Choice=='a' or Admin_Choice=='A':
                self.Employee.ShowEmployees()
            elif Admin_Choice=='b' or Admin_Choice=='B':
                Up_Info=self.BonusOrSalaryToEmployees('Bonus')
                self.Employee.Write_UpdatedRecord(Up_Info,'Employee_details.txt')
            elif Admin_Choice=='c' or Admin_Choice=='C':
                Up_Info=self.BonusOrSalaryToEmployees('Salary')
                self.Employee.Write_UpdatedRecord(Up_Info, 'Employee_details.txt')
            else:
                print('Invalid Choice')
            ch_1 = input('Do you want to continue managing Employees?\n'
                         'Enter choice(Yes or No):')
            if ch_1 == 'Yes' or ch_1 == 'yes':
                continue
            elif ch_1 == 'No' or ch_1 == 'no':
                break

    def BonusOrSalaryToEmployees(self,TypeOfAmount):
        Count_EmpOrd_Dict = self.Employee.ShowEmployees('SEND AMOUNT')
        choice = int(input(f'Enter an employee number to send {TypeOfAmount}: '))
        EmpOrd_Lst = Count_EmpOrd_Dict[choice]
        UPDATED_LST=[]
        with open('Employee_details.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if EmpOrd_Lst[1] in line:
                    line=line.strip()
                    self.Emp_detail_List=line.split(',')
                    if TypeOfAmount=='Salary':
                        self.Emp_detail_List[5]=str(eval(self.Emp_detail_List[5])+Delivery_Employee.salary)+'\n'
                        print(f'Monthly salary of PKR{Delivery_Employee.salary} is sent to Mr.{self.Emp_detail_List[0]}')
                    elif TypeOfAmount=='Bonus':
                        Bonus=int(input('Enter Amount of Bonus: '))
                        self.Emp_detail_List[5]=str(eval(self.Emp_detail_List[5])+Bonus)
                        print(f'A Bonus of PKR{Bonus} is sent to Mr.{self.Emp_detail_List[0]}')
                    UPDATED_LST.append(self.Emp_detail_List[0]+','+self.Emp_detail_List[1]+','
                                       +self.Emp_detail_List[2]+','+self.Emp_detail_List[3]
                                       +','+self.Emp_detail_List[4]+','+self.Emp_detail_List[5]+'\n')
                else:
                    UPDATED_LST.append(line)
            return UPDATED_LST

    def Manage_Stock(self):
        while True:
            print(f'What do you want to do?\n'
                  f'a)View Stock\n'
                  f'b)Add Stock\n'
                  f'c)Remove Stock')
            choice_2 = input('Enter Your Choice(a,b,c): ')
            if choice_2 == 'a' or choice_2 == 'A':
                self.View_Stock()
            elif choice_2 == 'b' or choice_2 == 'B':
                self.Add_Stock()
            elif choice_2 == 'c' or choice_2 == 'C':
                self.Remove_Stock()
            else:
                print('Enter Valid choice')
            ch_1=input('Do you want to continue managing stock?\n'
                       'Enter choice(Yes or No):')
            if ch_1=='Yes' or ch_1=='yes':
                continue
            elif ch_1=='No' or ch_1=='no':
                break

class Delivery_Employee(User):
    salary = 25000
    comission_per_ord=150

    def __init__(self):
        pass

    def Take_Info(self):
        while True:
            super().__init__()
            self.truth_value = self.CheckInFile('Employee_details.txt')
            if self.truth_value == True:
                with open('Employee_details.txt','r') as f:
                    lines=f.readlines()
                    for line in lines:
                        if self.name in line and self.mail in line and self.password in line:
                            line=line.strip()
                            line_lst=line.split(',')
                            self.Phone_number =line_lst[3]
                            self.Acc_number=line_lst[4]
                            self.BankBal=line_lst[5]
                print('Your account is already present\n')
                return
            elif self.truth_value == False:
                self.Phone_number = input('Enter phone number please :(+92) ')
                self.Acc_number = input('Enter your account number please :')
                self.BankBal=input('Enter your bank Balance: ')
                self.SaveToFile()
                print('Your account has been created successfully')
                return
            elif self.truth_value == 'invalid':
                print('Enter correct password')

    def SaveToFile(self):
        with open('Employee_details.txt', 'a+') as f:
            f.write(self.name+','+self.mail+','+self.password+','+self.Phone_number+','+self.Acc_number+','+self.BankBal+'\n')
        with open('Orders_Delivered.txt','a+') as f:
            f.write(self.name+':'+self.mail+':'+'0'+'\n')

    def Display_order(self):
        with open('Orders.txt', 'r+') as f:
            Null_Checker = f.read()
            if Null_Checker == '':
                print(f'No Orders to show, yet :(')
            else:
                with open('Orders.txt','r') as l:
                    Ord_count=1
                    line_Lst=l.readlines()
                    print(f'{len(line_Lst)} Order(s) have been placed by our respected customers: ')
                    for line in line_Lst:
                        line=eval(line)
                        print(f'{Ord_count}.\n{line[0]}')
                        Ord_count+=1
                    self.orders_delievered = len(line_Lst)
                    OrdersDelivered = input('Type "DONE" after Delivering All orders: ')
                    if OrdersDelivered == "DONE" or OrdersDelivered == "Done" or OrdersDelivered == "done":
                        with open('Orders.txt','w') as k:           #file clear kr rhaa hai
                            print(f'{self.orders_delievered} orders delivered successfully ')
                        with open('Orders_Delivered.txt', 'r') as m:
                            lines=m.readlines()
                            update_lst=[]
                            for line in lines:
                                if self.name in line and self.mail in line:
                                    line=line.strip()
                                    line_lst=line.split(':')
                                    line_lst[2]=str(eval(line_lst[2])+self.orders_delievered)+'\n'
                                    update_lst.append(line_lst[0]+':'+line_lst[1]+':'+line_lst[2]+'\n')
                                else:
                                    update_lst.append(line)
                            self.Write_UpdatedRecord(update_lst,'Orders_Delivered.txt')
                        Comission=self.Comission_Setter()
                        Update_Lst=self.ComissionBalance_Adder(Comission)
                        self.Write_UpdatedRecord(Update_Lst,'Employee_details.txt')

    def Comission_Setter(self):
        self.comission = self.orders_delievered * Delivery_Employee.comission_per_ord
        print(f'Comission of Mr.{self.name} is {self.comission},\n'
              f'Pkr{self.comission} is sent to your Account number {self.Acc_number}')
        return self.comission

    def ComissionBalance_Adder(self,Comission):
        with open('Employee_details.txt','r+') as f:
            lines=f.readlines()
            Updated_RecordLst=[]
            strg=''
            for SingleEmployee in lines:
                if self.mail and self.Phone_number and self.Acc_number in SingleEmployee:
                    SingleEmployee=SingleEmployee.strip()
                    Emp_details=SingleEmployee.split(',')
                    Emp_details[5] = str(eval(Emp_details[5]) + Comission) + '\n'
                    for items in Emp_details:
                        if items!=Emp_details[5]:
                            strg+=items+','
                        else:
                            strg+=items
                    Updated_RecordLst.append(strg)
                else:
                    Updated_RecordLst.append(SingleEmployee)
            return Updated_RecordLst

    def Write_UpdatedRecord(self,UpdatedRecord,filename):
        with open(filename,'w') as f:
            for Record in UpdatedRecord:
                f.write(Record)

    def ShowEmployees(self,OrdersDelivered=None):
            count = 1
            Dict = {}
            if OrdersDelivered != None:
                with open('Orders_Delivered.txt') as f:
                    Emps = f.readlines()
                    print(' ' * 10 + '%-9s%-14s%-s' % ('S.no', 'Name', 'Orders Delivered'))
                    for Single_Emp in Emps:
                        Single_Emp = Single_Emp.strip()
                        Emp_lst = Single_Emp.split(':')
                        print(' ' * 11 + '%-8i%-19s%s' % (count, Emp_lst[0], Emp_lst[2]))
                        Dict[count] = [Emp_lst[0],Emp_lst[1],Emp_lst[2]]               #    { 1 : , [name,email,ord_delivered] }
                        count += 1
            elif OrdersDelivered == None:
                with open('Employee_details.txt','r') as f:
                    All_Emps=f.readlines()
                    for line in All_Emps:
                        line=line.strip()
                        line_lst=line.split(',')
                        print(f'{count}. Mr.{line_lst[0]}')
                        Dict[count] = line_lst[0]
                        count+=1
            return Dict

    def Show_Balance(self):
        with open('Employee_details.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if self.mail and self.Phone_number and self.Acc_number in line:
                    line=line.strip()
                    Detail_lst=line.split(',')
                    print(f'Mr.{self.name}, your Bank balance is {Detail_lst[5]}')

class Shipping_Details:
    def ConfirmationMail(self, email):
        return f'Following order is confirmed for email {email}\n'

    @staticmethod
    def Date_Lister(Date):
        date = Date.split()
        DATE = []
        for item in date:
            item = item.strip(',')
            DATE.append(item)
        return DATE

    def Update_ShippingDetails(self,DateOfOrder):
        today = date.today()
        Date = today.strftime("%B %d, %Y")
        Date_List=Shipping_Details.Date_Lister(Date)
        OrderDateList=Shipping_Details.Date_Lister(DateOfOrder)
        Months={'January':1,
                'February':2,
                'March':3,
                'April':4,
                'May':5,
                'June':6,
                'July':7,
                'August':8,
                'September':9,
                'October':10,
                'November':11,
                'December':12}
        Month_Number_Now=Months[Date_List[0]]
        Order_Month_Number=Months[OrderDateList[0]]
        if  Date_List[1]-OrderDateList[1]==0 and Month_Number_Now==Order_Month_Number:
            return f''
        elif Date_List[1]-OrderDateList[1]>=2 and Month_Number_Now==Order_Month_Number:
            return f''
        elif  Date_List[1]-OrderDateList[1]>=10 and Month_Number_Now==Order_Month_Number:
            pass
        else:
            pass

class Payment:
    def __init__(self):
        print(f'Enter mode of Payment:\na)Cash on Deivery\nb)Online Payment\nEnter Choice(a or b): ', end='')
        self.Pay = input()

    def Cash_On_Delivery(self, address):
        print(f'Cash on delivery is selected,\nAbove order will be delivered at {address}')

    def Online_Payment(self):
        print('How would you like to pay?\na) On Credict Card\nb) Through EasyPaisa')
        credit_choice = input()
        if credit_choice == 'a' or credit_choice == 'A':
            print('Please enter your account number')
            self.accnt = input()
            print('Payment has been done successfully!!')
        elif credit_choice == 'b' or credit_choice == 'B':
            print('Enter your EasyPaisa account number')
            e_accnt = input()
            print(f'Payment has been done successfully by account number {e_accnt}')