accounts = {
    'current': 2000,
    'savings': 10000
}


def add_balance(amount: float, name: str = 'current') -> float:
    """Function to update the balance of an account
    and return the new balance"""
    accounts[name] += amount
    return accounts[name]


# print(accounts['current'])


transactions = [
    (5000, 'current'),
    (-180.67, 'current'),
    (2000, 'savings'),
    (-236.24, 'current'),
    (-151.89, 'current'),
    (1000, 'savings'),
    (-91.62, 'current'),
    (-174.68, 'current'),
    (500, 'savings'),
    (-122.58, 'current'),
]

# * is the unpacking operator which unpacks any iterable into arguments
for t in transactions:
    add_balance(*t)
    print(f'Current: ' + str(round(accounts['current'], 2)) +
          f', Savings: ' + str(round(accounts['savings'], 2)))
