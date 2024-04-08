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
    def __init__(self):
        self._protected_car_prices = {
            "opel": 20000,
            "bwd": 25000,
            "ford": 22000,
            "lotus": 23000,
            "ladaniva": 18000,
            "bmw": 40000,
            "mercedes": 45000,
            "yeraz": 1000,
            "moskvich": 60000,
            "zil": 210000
        }
    def checker(self,brand):
        return brand in self._protected_car_prices


class Mycar(CarMarket):
    def get_car(self, brand):
        brand = brand.lower()
        if self.checker(brand):
            if brand == "bmw":
                discount_price = self._protected_car_prices[brand] - (self._protected_car_prices[brand]*0.2)
                print("Price with 20% discount = ", discount_price)
            else:
                print(self._protected_car_prices[brand])
        else:
            print("The brand doesn't exist")


obj = Mycar()     
obj.get_car("BMW")

# Anna - The logic is correct, only you convert brand to lower case and then compare with "BMW" :)
# So you never will get discounted result.
#Juli-Done
#  And also will be better to convert to float (line 49) in case exact price was matter
#Juli-Done
# Other implementaions is good