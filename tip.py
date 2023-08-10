"""
Tip Calc
Returns a calculated tip
"""

def calc_tip(price: float, tip: float) -> float:
    """returns the discounted price
    ex.: a price of $100.00 with a discount of 20% returns $80.00"""
    return round(price + tip * (price / 100), 2)

if __name__ == "__main__":
    import sys
    calc_tip(float(sys.argv[1]), float(sys.argv[2]))
