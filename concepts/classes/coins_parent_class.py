import random as r
from symbol import arith_expr

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        
        '''The below code will work for any dictionary that is passed in
            In this example, this means the states of any new type of coin
                that is initialised through the Coin class'''
        for key, value in kwargs.items():
            setattr(self, key,value)
        
        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

        def rust(self):
            self.colour = self.rusty_colour

        def clean(self):
            self.colour = self.clean_colour

        def __del__(self):
            print("Coin Spent!")

        def flip(self):
            coin_toss_options = [True, False]
            choice = r.choice(coin_toss_options)
            self.heads = choice

        def __str__(self):
            if self.original_value >= 1.00:
                return "£{} coin".format(int(self.original_value))
            else:
                return "{}p Coin".format(int(self.original_value * 100))

class One_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 12,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }

        super().__init__(**data) 

class One_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }

        super().__init__(**data) 

class Two_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }

        super().__init__(**data) 

class Five_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": "None",
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": "None",
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.5
        }

        super().__init__(**data) 

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Twenty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": "None",
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5
        }

        super().__init__(**data) 

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Fifty_Pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": "None",
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8
        }

        super().__init__(**data) 

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Two_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 11,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
        }

        super().__init__(**data)

coins = [One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),
         Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    coin_details = f"""
    Coin: {coin}\n
    Colour: {coin.colour},\
    Value: {coin.value},\
    diameter(mm): {coin.diameter},\
    thickness(mm): {coin.thickness},\
    number of edges: {coin.num_edges},\
    mass(g): {coin.mass}
    """
    print(coin_details)