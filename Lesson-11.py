'''
Task: Create a Python program that simulates a car market where there
 are 10 car brands with prices.
The program should use object-oriented programming and inheritance to implement
a base class CarMarket and a child class MyCar.

 - The CarMarket class should have a dictionary to
store car prices and a method to check
if a given car brand exists in the market.
 - The MyCar class should inherit from CarMarket and include
   a discount attribute and a method
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
        # Initialize car prices dictionary
        self.car_prices = {
            "Toyota": 20000,
            "Honda": 22000,
            "Ford": 25000,
            "BMW": 35000,
            "Audi": 40000,
            "Mercedes": 45000,
            "Lexus": 38000,
            "Chevrolet": 23000,
            "Tesla": 60000,
            "Subaru": 27000
        }

    def check_brand(self, brand):
        # Check if a car brand exists in the market
        return brand in self.car_prices


class MyCar(CarMarket):
    def __init__(self):
        super().__init__()
        self.discount = 0.2  # 20% discount for BMW

    def print_results(self, brand):
        if brand == "BMW":
            if self.check_brand(brand):
                price_with_discount = self.car_prices[brand] * (1 - self.discount)
                print(f"Price of {brand} with 20% discount: ${price_with_discount:.2f}")
            else:
                print(f"{brand} is not available in the market.")  # Anna - you could not write this else, as you have not available message print in line 69
        elif self.check_brand(brand):
            print("Market list:")
            for car, price in self.car_prices.items():
                print(f"{car}: ${price}")
        else:
            print(f"{brand} is not available in the market.")


car_market = MyCar()
car_market.print_results("Honda1")

# Anna - good, in case when car not BMW you should print current car price not all list of cars with prices
# 