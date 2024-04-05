class CarMarket:
    def __init__(self):
        self.car_cost = {
            "BMW": 15000,
            "Toyota": 23000,
            "Crysler": 12500,
            "Audi": 13000,
            "Lexux": 17800,
            "Honda": 10000
              }
    
    def check_br(self, brand):
        return brand in self.car_cost


class MyCar(CarMarket):
    def __init__(self):
        super().__init__()
        self.discount = 0.2

    def new_res(self, brand):
        if brand == "BMW":
            print(f"The price of {brand} with discount 20%")
        elif self.check_br(brand):
            print("This is market list")
        else:        
            print(f"{brand} is nor available in the market")


market = MyCar()

market.new_res("BMW")
market.new_res("Honda")
market.new_res("Test")