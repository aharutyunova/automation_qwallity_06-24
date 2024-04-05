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
            "Mazda": 20000,
            "Mercedes": 25000,
            "BMW": 32000,
            "Audi": 25000,
            "Nissan": 20000,
            "Lexus": 15000,
            "Toyota": 10000,
            "Infiniti": 25000,
            "Porsche": 30000,
            "Acura": 10000
        }

    def is_mark_exists(self, car):
        '''Method to check if given car brand exists in the market'''
        return car in self.car_prices


class MyCar(CarMarket):
    discount = 0.2  # 20% discount for BMW

    def __init__(self, car):
        super().__init__()
        self.car = car

    def print_price(self):
        '''Method to print the price of a car brand with discount if applicable'''
        if self.is_mark_exists(self.car):
            if self.car == "BMW":
                discounted_price = self.car_prices[self.car] * (1 - self.discount)
                print(f"Price for {self.car}: ${discounted_price}")
            else:
                print("Market list:", self.car_prices)
        else:
            print(f"Car {self.car} does not exist in the market.")


my_car_1 = MyCar("BMW")
my_car_1.print_price()

my_car_2 = MyCar("Toyota")
my_car_2.print_price()

my_car_3 = MyCar("Tesla")
my_car_3.print_price()
