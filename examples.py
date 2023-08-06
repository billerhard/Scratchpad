"""
Examples"""
#pylint: disable=unused-import
from discount import calc_discount

def main():
    """Examples of modules in the scratchpad."""

    print("print(f\"${calc_discount(100, 20):0.2f}\")")
    print(f"${calc_discount(100, 20):0.2f}")
    print("print(f\"${calc_discount(135.99, 17):0.2f}\")")
    print(f"${calc_discount(135.99, 17):0.2f}")

if __name__ == "__main__":
    main()
