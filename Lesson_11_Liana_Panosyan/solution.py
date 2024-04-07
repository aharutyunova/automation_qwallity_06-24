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
        self.dict_car_prices = {
            "Ford": 15000,
            "Nissan": 10000,
            "BMW": 24500,
            "Honda": 14000,
            "Mercedes-Benz": 20000,
            "Volkswagen": 5000,
            "Kia": 16000,
            "Lexus": 45000,
            "Tesla": 30000,
            "Porsche": 45000
              }

    def check_brand(self, brand):
        return brand in self.dict_car_prices


class MyCar(CarMarket):
    def __init__(self):
        super().__init__()
        self.dis = 0.2

    def print_results_based_on_the_brand(self, brand):
        if brand in self.dict_car_prices:
            if brand == "BMW":
                dis_price = self.dict_car_prices[brand] * (1 - self.dis)
                print("The discounted price of the 'BMW' is", int(dis_price))
            else:
                print(f"Price of '{brand}' {self.dict_car_prices[brand]}")
        else:
            print(f"Brand '{brand}' is not in the market.")


car_market = MyCar()
print(car_market.check_brand("Audi"))
print(car_market.check_brand("Lexus"))

car_market.print_results_based_on_the_brand("BMW")
car_market.print_results_based_on_the_brand("Audi")
car_market.print_results_based_on_the_brand("Porsche")
