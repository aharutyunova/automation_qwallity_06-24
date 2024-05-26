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
•	Keep attribute with 20% discount for BMW
•	Provides a method to print results based on the given brand if available


# just a simple function

car_dict_list = [
            {"brand": "BMW", "price": 30000},
            {"brand": "Mercedes", "price": 8000},
            {"brand": "Porsche", "price": 100000},
            {"brand": "Opel", "price": 3000},
            {"brand": "Hyundai", "price": 12000},
            {"brand": "Toyota", "price": 10000},
            {"brand": "Nissan", "price": 6000},
            {"brand": "Reno", "price": 4000},
            {"brand": "Lexus", "price": 15000},
            {"brand": "Tesla", "price": 35000},
        ]


car_name = input("Car: ").lower()
discount = 0.2
car_found = False

for car in car_dict_list:
    if car["brand"].lower() == car_name:
        car_found = True
        if car_name == "bmw":
            discounted_price = car["price"] * (1 - discount)
            print(f'Car: {car["brand"]} - Price after 20% discount: ${discounted_price:.2f}')
        else:
            print(f'Car: {car["brand"]} - Price: ${car["price"]}')
        break

if not car_found:
    print("Car does not exist in the list!!!")

'''


class CarMarket:
    def __init__(self):
        self.car_price_dict = {
            "BMW": 30000,
            "Mercedes": 8000,
            "Porsche": 100000,
            "Opel": 3000,
            "Hyundai": 12000,
            "Toyota": 10000,
            "Nissan": 6000,
            "Reno": 4000,
            "Lexus": 15000,
            "Tesla": 35000,
        }

    def is_brand_exists(self, car):
        return car in self.car_price_dict


class MyCar(CarMarket):
    discount = 0.2

    def __init__(self, car):
        super().__init__()
        self.car = car

    def print_price(self):
        if self.is_brand_exists(self.car):
            if self.car == "BMW":
                discounted_price = self.car_price_dict[self.car] * (1 - self.discount)
                print(f"Price for {self.car}: ${discounted_price}")
            else:
                print("Car market list:", self.car_price_dict)
        else:
            print(f"Car {self.car} does not exist in the market.")


my_car = MyCar("Toyota")
my_car.print_price()

my_car = MyCar("BMW")
my_car.print_price()

my_car = MyCar("Mazda")
my_car.print_price()

# Anna - Very good, only in line 93 you should return not all dictionary, but existing car price
# self.car_price_dict[self.car]
#  And the message could be the same - f"Price for {self.car}: ${self.car_price_dict[self.car]}"