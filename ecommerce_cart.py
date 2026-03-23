def calculate_total(cart_items):
    """Calculate total price of items with discount if applicable."""
    if not cart_items:
        return "Cart is empty."

    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total *= 0.9  # 10% discount

    return total
if __name__ == "__main__":
    cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
    total_price = calculate_total(cart_items)
    print(f"Total Price: {total_price}")
