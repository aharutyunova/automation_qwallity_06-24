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
        self.car_prices = {
            "Toyota": 28000,
            "Honda": 27000,
            "Ford": 30000,
            "Chevrolet": 32000,
            "BMW": 90000,
            "Mercedes": 75000,
            "Audi": 52000,
            "Lexus": 48000,
            "Nissan": 26000,
            "Tesla": 70000
        }
        
    def check_brand(self, brand):
        if brand in self.car_prices:
            return f"The {brand} car is successfully found"
        else:
            return "No found"

class MyCar(CarMarket):
    discount = 0.2

    def print_price(self, brand):
        if brand == "BMW":
            price = self.car_prices.get(brand)
            discounted_price = price * (1 - self.discount)
            print(f"Price of {brand} with 20% discount: ${discounted_price}")
        elif self.check_brand(brand):
            print("Market list:")
            for brand, price in self.car_prices.items():
                print(f"{brand}: ${price}")
        else:
            print("This brand is not available in the market.")





class Penmarket:
    def __init__(self):
        self.pen_prices = {
           "Red": 1000,
           "Yellow": 2000,
           "Green": 500,
           "Black": 100,
           "Grey": 600,
           "Blue": 50,
           "White": 400,
           "Pink": 700,
        }

    def pen_color_check(self, color):
        if color in self.pen_prices:
            return f"The pen with {color} color is available"
        else:
            return "No such pen color found"

class Mypen(Penmarket):
    def __init__(self, price=100):
        super().__init__()
        self.price = price

    def print_price(self, color):
        if color in self.pen_prices:
            print(f"Price of {color} pen is ${self.pen_prices[color]}")
        else:
            print("Pen color not found")
