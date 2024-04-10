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


class Car_Market:
    def __init__(self, car):
        self.car = car.upper()
        self.car_in_market = {
            "BMW": 30000,
            "Mercedes": 8000,
            "Porsche": 100000,
            "Opel": 3000,
            "Hyundai": 12000,
            "Toyota": 10000,
            "Nissan": 6000,
            "RENO": 4000,
            "Lexus": 15000,
            "TEsla": 35000
        }
        # Convert dictionary keys to upper
        self.car_in_market = {
            key.upper(): value for key, value in self.car_in_market.items()}

    def check_car_exists(self):
        if self.car in self.car_in_market.keys():
            return True
        else:
            return False


class MyCar(Car_Market):
    def __init__(self, car, discount=0.2):
        super().__init__(car)
        self.discount = discount

    def print_price(self):
        if self.check_car_exists():
            if self.car == 'BMW':
                price = self.car_in_market[self.car] * (1-self.discount)
                print(f"{self.car} price is {price}")
            else:
                price = self.car_in_market[self.car]
                print(f"{self.car} price is {price}")
        else:
            print(f"{self.car} doesn't exist in the market")


car_brand = 'Nissan'
check_car = MyCar(car_brand)
check_car.print_price()
