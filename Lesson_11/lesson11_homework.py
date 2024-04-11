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
    car_dictionary = [
                        {'name': 'Nissan', 
                         'price': 5000},
                        {'name': 'Volkswagen', 
                         'price': 6000},
                        {'name': 'Toyota', 
                         'price': 10000},
                        {'name': 'Ford', 
                         'price': 7000},
                        {'name': 'Kia', 
                         'price': 7000},
                        {'name': 'Mercedes-Benz', 
                         'price': 9000},
                        {'name': 'BMW', 
                         'price': 9000},
                        {'name': 'Audi', 
                         'price': 8000},
                        {'name': 'Hyundai', 
                         'price': 12000},
                        {'name': 'Chevrolet', 
                         'price': 11000}]

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def car_existence(self):
        for car in CarMarket.car_dictionary:
            if self.name == car['name']:
                return 1
        return 0


class MyCar(CarMarket):
    def __init__(self, name, price):
        super().__init__(name,price)
        if self.name == 'BMW':
            self.discount = 20

    def result(self):
        if self.car_existence() == 0:
            return "The brand is not exist in the Market"
        else:
            if self.name == 'BMW':
                self.price *= (1-self.discount/100)
                return f"There is a 20 % discount for BMW, and the price now is {self.price}"
            else: 
                carNames = []
                for car in CarMarket.car_dictionary:
                    carNames.append(car['name'])
                return f"Discount only for BMW, Market list : {carNames}"

           
x = MyCar('Yaguar', 1000)
print(x.result())
x = MyCar('BMW', 1000)
print(x.result())
x = MyCar('Kia', 1000)
print(x.result())


# Anna - from one side logic is covered, but solution a bit dificcult Ray jan
# Look at first you could keep car names and prices as one dictionary 
#  In case you already have stored prices you don't need pass them in line 48 __init__()
# And the second for loop in else line 72 not necessary. 
# You already have the list of availabe cars, why you create empty list and re-create it?

# Please have a look pn my solution, will add it on the main branch
    