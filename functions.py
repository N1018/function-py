def calculate_discount(price, discount_percent):
    """Calculate the final price after applying the discount."""
    if discount_percent > 20:
        return price * (1-discount_percent/100)
    return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percentage)

    
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")