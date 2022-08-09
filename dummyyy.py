from abc import ABC, abstractmethod
from datetime import date


class User(ABC):
    def __init__(self):
        self.name = input('Enter name: ')
        self.mail = input('Enter email: ')
        self.password = input('Enter password: ')

    @abstractmethod
    def SaveToFile(self):
        pass

    def CheckInFile(self, y):
        with open(y, 'r') as k:
            lines = k.readlines()
            for record in lines:
                # print(record)
                if self.mail in record and self.password in record:
                    return True
                elif self.mail in record and self.password not in record:
                    return 'invalid'
                # elif self.name=='' and self.mail=='' and self.password=='':
                #     return 'empty'
                else:
                    return False

class Customer(User):
    def SaveToFile(self):
        with open('store.txt', 'a+') as f:
            f.write(self.name + ',' + self.mail + ',' + self.password + '\n')

    def __init__(self):
        self.Cart = ShoppingCart()
        while True:
            super().__init__()
            self.truth_value = super().CheckInFile('store.txt')
            if self.truth_value == True:
                print('Your account is already present\n')
                self.Address = input('Enter your Address: ')
                break
            elif self.truth_value == False:                          #interpreter iskay if elif me ghus hi nahi raha
                self.SaveToFile()
                print('Your account has been created successfully')
                self.Address = input('Enter your Address: ')
                break
            elif self.truth_value == 'invalid':
                print('Enter correct password')



    def Show_Choose_And_Print(self):
        self.Cart.Show_Items()
        self.Cart.Choose_Domain()

    def Show_Shopping_Cart(self):
        self.Cart.Show_Cart()

    def Add_To_ShoppingCart(self):
        # self.Show_Choose_And_Print()
        Additional_Items={}
        Prod_Pr_dic={}
        Chose_Product_Dict={}
        Products.Give_Domain_Products_Dict(Products.Domain_Products_Dict)
        s_no=1
        for Domain in Products.Domain_Products_Dict:
            print(f'{s_no}. {Domain}')
            s_no+=1
        print('Enter no. of domain you want to add products from: ',end='')
        domain_choice=input()
        if domain_choice=='1':
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
            #yahan pr stock me vapis total quantity add krwani hai
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
                str(count) + '.', item, str(Products.All_Product_Prices_Dict[item]) + '/-', str(shopping_dict[item]),str(Products.All_Product_Prices_Dict[item] * shopping_dict[item]) + '\n')
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
        # print(Details)
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
        with open('Cust_Order_History.txt', 'a') as f:
            self.ListOfOrder = []
            self.ListOfOrder.append(self.strg_ord)
            f.write(str(self.ListOfOrder) + '\n')

    def Write_In_File(self):
        with open('order.txt', 'a+') as l:
            l.write(self.strg_ord)

    def Cal_total_payment(self):
        self.summ_list = sum(self.Amount_list)
        string = 'Your Total Payment is :' + str(self.summ_list) + 'Rs\nTHANK YOU FOR SHOPPING!!\n'
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

    def UpdateStock(self, Purpose='Add to Cart',Prod=None,Quantity=None):#All k liye call krwana hai ye method Remove from cart k liye
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





class Shipping_Details:
    def ConfirmationMail(self, email):
        return f'Your Following order is confirmed for email {email}\n'

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