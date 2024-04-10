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


class Carmarket:
    def __init__(self, car):
        self.car = car 
        self.car_market_names = {
            "Mazda": 25000,
            "Toyota": 15000,
            "Mercedes": 30000,
            "Kia": 18000,
            "Ford": 5000,
            "BMW": 40000,
            "Opel": 2000,
            "Jeep": 12000,
            "Chevrolet": 8500,
            "Nissan": 3600
        }
    
    def Car_existance(self):
        if self.car in self.car_market_names.keys():
            return True
        else:
            return False

class Mycar(Carmarket):
    def __init__(self, car, discount=20):
        super().__init__(car)
        self.discount = discount
    
    def price(self):
        if self.Car_existance():
            if self.car == "BMW":
                price_1 = self.car_market_names[self.car] * self.discount / 100
                price_2 = self.car_market_names[self.car] - price_1
                print(price_2)
            else:
                print(self.car_market_names)
        else:
            print("There is no such a brand in our list")

car_1 = "Kia"
Existance = Mycar(car_1)   
print(Existance.price())

# Anna - Also good implemented,
#  only pay attention on object names (Existence) it is better to start with lowercase
# Also in case when brand is not BMW you should print price of certen brand, not the whole list of brands and prices

#  Also for the future in such cases compare names or other string to lower or upper case
# Because in case now I input KIA, I will get message - "There is no such a brand in our list"

        