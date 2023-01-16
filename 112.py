#Multilevel Inheritence

class Company:
    def __init__(self):
        cmp=''

    def getCompany(self):
        self.cmp=input('Enter Company')
    
class Product(Company):
    def __init__(self):
        prd=''
    def getProduct(self):
        self.prd=input('Enter Product : ')

class Purchase(Product):
    def __init__(self):
        price=0.0
        qty=0
    def productPurchase(self):
        self.price=float(input('Enter Price : '))
        self.qty=int(input('Enter Qty : '))
    def printBill(self):
        print('Purcahse Product')
        print('Company : ',self.cmp)
        print('Product : ',self.prd)
        print('Qty : ',self.qty)
        print('Price : ',self.price)
        print('Amount : ',self.qty*self.price)