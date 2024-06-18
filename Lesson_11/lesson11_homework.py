'''
Task: Create a Python program that simulates a car market where there are
10 car brands with prices.
The program should use object-oriented programming and inheritance to implement
a base class CarMarket and a child class MyCar.

 - The CarMarket class should have a dictionary to store car prices
 and a method to check if a given car brand exists in the market.
 - The MyCar class should inherit from CarMarket and include a
 discount attribute and a method to print the results based on the brand:
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
        self.car_brand = input("Enter a car brand: ")
        self.car_prices = {
            'BMW': 15000,
            'Opel': 5000,
            'Nissan': 8000,
            'Hundai': 7000,
            'Mercedess': 16000,
            'Lexus': 17000,
            'Reno': 12000,
            'Pegue': 9000,
            'Mustang': 30000,
            'Ford': 10000
        }
        self.isCarBrand()

    def isCarBrand(self):
        if self.car_brand in self.car_prices:
            print(f"Requested car price: {self.car_prices[self.car_brand]}")
            # print(f"{self.car_prices}")
        else:
            print("Car brand not found in the market")


class MyCar(CarMarket):

    def discount(self, discount):
        if self.car_brand == "BMW":
            price_for_BMW = self.car_prices["BMW"]
            discounted_price = price_for_BMW - price_for_BMW * \
                (discount / 100)
            return (f"Discounted Price: {discounted_price}")
        else:
            return ("No discaount for this brand.")


my_car = MyCar()
print(my_car.discount(30))

# Anna - generally everything is correct.
# But will be more correct if your isCarBrand method return true if car exists and false if not exists
# After it you will call this methot in MyCar class-discount
#  method which will return final price or message that car doesn't exist
