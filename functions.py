def calculate_discount(price, discount_percent):
    """Calculate the final price after applying the discount."""
    if discount_percent > 20:
        return price * (1-discount_percent/100)
    return price