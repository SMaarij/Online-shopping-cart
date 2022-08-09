# # class Customer(User):
# #     def __init__(self):
# #         super().__init__()
# #         truth_value = super().CheckInFile('store.txt')
# #         if truth_value != True:
# #             super().SaveToFile('store.txt')
# #             print('Your account has been created successfully')
# #         else:
# #             print('Your account is already present\n')
# #         self.Address = input('Enter your Address: ')
# #         self.Cart = ShoppingCart()
# #     def Show_Choose_And_Print(self):
# #
# #         self.Cart.Show_Products()
# #         self.Cart.choose_Product()
# #         self.Cart.Show_Order()
# class ShoppingCart:
#     Prod_Price_dict = {}
#     Choose_Dict = {}
#
#     def Show_Products(self):
#         count = 1
#         countt = 1
#         Item_List = ShoppingCart.Give_ItemAndPriceList()
#         # print(Item_List)
#         for Pair_Product in Item_List:
#             # ShoppingCart.Prod_Price_dict[Pair_Product[0]] = Pair_Product[1]
#             print(str(count) + '.' + Pair_Product[0] + '\t' + 'pkr' + Pair_Product[1])
#             count += 1
#             ShoppingCart.Prod_Price_dict[Pair_Product[0]] = Pair_Product[1]
#         for Product in ShoppingCart.Prod_Price_dict:
#             # print(str(countt) + '.' + Product)
#             ShoppingCart.Choose_Dict[countt] = Product
#             countt += 1
#         for Product in ShoppingCart.Prod_Price_dict:
#             ShoppingCart.Choose_Dict[countt] = Product
#             countt+=1
#     @staticmethod
#     def Give_ItemAndPriceList():
#         Item_List = []
#         with open('Products.txt', 'r+') as Products:
#             Product_list = Products.readlines()
#             for Retailer_Products in Product_list:
#                 single_Procuct = Retailer_Products.split(',')
#                 for price_procut in single_Procuct:
#                     ItemAndPrice = price_procut.split(':')
#                     Item_List.append(ItemAndPrice)
#         return Item_List
# Do=ShoppingCart()
# Do.Show_Products()
# p=[1,2,3,4]
# s=sum(p)
# print(s)
# s={'roll':15}
# p={'roll':30}
# l=[]
# for i in s:
#     l.append(s[i]*p[i])
# print(l)
# @staticmethod
def Give_ItemAndPriceList():
    Item_List = []
    with open('Products.txt', 'r+') as Products:
        Product_list = Products.readlines()
        for Domain_Products in Product_list:
            single_Procuct = Domain_Products.split(';')
            for price_produt in single_Procuct:
                ItemAndPrice = price_procut.split(':')
                Item_List.append(ItemAndPrice)
    return Item_List
print(Give_ItemAndPriceList())








