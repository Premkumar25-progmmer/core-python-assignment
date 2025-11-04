def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty. Please add some items."
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = total * 0.10
        total -= discount

    return f"Total Price: {int(total)}"
cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500
}
print(calculate_total(cart_items))
