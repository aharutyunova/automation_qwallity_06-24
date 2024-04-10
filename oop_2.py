'''
Task: Create a Python program that simulates a car market where there are 10 car brands with prices. 
The program should use object-oriented programming and inheritance to implement 
a base class CarMarket and a child class MyCar. 

 - The CarMarket class should have a dictionary to store car prices and a method to check 
if a given car brand exists in the market. 
 - The MyCar class should inherit from CarMarket and include a discount attribute and a method 
to print the results based on the brand:
1. If the brand is BMW, system prints price with 20 % discount
2. If the brand is not exist in list, develop message
3. If the brand exist in list, but not a BMW, just print Market list.

Technical Solution:
Base class CarMarket:
•	Initializes the car prices dictionary.
•	Provides a method to check if a car brand exists in the market.

Child class MyCar:
•	Inherits from CarMarket
•	Keep atribute with 20% discount for BMW
•	Provides a method to print results based on the given brand if available
'''




class CarMarket:
    def __init__(self, car_price): #TODO #Anna - you don't need car_price as class parameter
        self.car_price = {
            'BMW': 50000,
            'Toyota': 30000,
            'Ford': 40000,
            'Honda': 35000,
            'Tesla': 60000,
            'Audi': 45000,
            'Mercedes': 55000,
            'Lexus': 48000,
            'Chevrolet': 32000,
            'Hyundai': 28000
        }
        
    def check_available(self, brand , price):
        return brand , price in self.car_price  


class Param: #TODO  # Anna - why you need Param class? it was not required and don't need for your solution
    def __init__(self , currency, production):
        self.currency = currency
        self.production = production
 

class MyCar(CarMarket, Param):
    def __init__(self, currency, production, discount=20):
        CarMarket().__init__(self)
        Param().__init__(currency, production)
        self.discount = discount

    def print_price(self, brand):
        if brand == 'BMW':
            price = self.car_prices.get(brand)
            discounted_price = price - (price * self.discount / 100)
            print(f"You have 20% discount")
        elif self.check_brand(brand):
            print(f"The car is available")
        else:
            print(f"Upps, The car is not available")

my_car = MyCar()
my_car.print_price('BMW') 
my_car.print_price('Toyota') 
my_car.print_price('Tesla') 
my_car.print_price('Test')

# In case you inhertir MyCar from CarMarket and Param classes you shoud in object pass all parameters of init methods of all this classes
#  In your example you should pass  currency and production my_car = MyCar("carrency_value", "production_value")
#  Your print_price method just print messages not calculate and print price for each model

# Please pay attention on my solution, I will coomit it on main branch a bit later

# class CarMarket:
#     def __init__(self,brand, price, currency, production, procent=20):
#         self.brand = input()
#         self.price = price
#         self.currency = currency
#         self.production = production
#         self.percent = procent


# def procent(self):
#     if self.procent = self.brand("BMW")
#       return self.price%20
#     print(self.price)
        
# class MyCar(CarMarket):
#     CarMarket.__init__(self,brand, price, currency, production):
    


# Car_BMW = (MyCar):
# MyCar.
