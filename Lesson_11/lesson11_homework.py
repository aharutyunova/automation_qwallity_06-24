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


# parent class
class CarMarket:
    def __init__(self):
        self.car_prices = {
            "Ford": 35000,
            "BMW": 45000,
            "Toyota": 20000,
            "Honda": 25000,
            "Audi": 37000,
            "Lexus": 47000,
            "Chevrolet": 32000,
            "Mercedes": 45000,
            "Niva": 20000,
            "Kia": 25000
        }

    def check_brand(self, brand):
        # check if the brand exists in the market
        return brand in self.car_prices


# child class
class MyCar(CarMarket):
    def __init__(self, discount=0.2):
        super().__init__()
        self.discount = discount

    def print_price(self, brand):
        if self.check_brand(brand):
            if brand == "BMW":
                price = self.car_prices[brand]
                discounted_price = price - (price * self.discount)
                print(f"The price of {brand} with 20% discount is {discounted_price}$")
            else:
                print(f"The price of {brand} is {self.car_prices[brand]}$")  # or print(self.car_prices)
        else:
            print(f"{brand} is not available in the market")


my_car = MyCar()
my_car.print_price("BMW")
my_car.print_price("Tesla")
my_car.print_price("Ford")
