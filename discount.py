"""
Discount Calc
Returns a calculated discount
"""

def calc_discount(price: float, discount: float) -> float:
    """returns the discounted price
    ex.: a price of $100.00 with a discount of 20% returns $80.00"""
    return round(price - price * (discount / 100), 2)
