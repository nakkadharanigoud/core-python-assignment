
def add_item(menu, item):
    """Add a new item to the menu."""
    if item not in menu:
        menu.append(item)
    return menu

def remove_item(menu, item):
    """Remove an item if it exists."""
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu.")
    return menu

def check_item(menu, item):
    """Check if an item is available."""
    return f"{item} is available" if item in menu else f"{item} is not available"


if __name__ == "__main__":
    menu = ["Pizza", "Burger", "Pasta", "Salad"]
    add_item_name = "Tacos"
    remove_item_name = "Salad"
    check_item_name = "Pizza"

    menu = add_item(menu, add_item_name)
    menu = remove_item(menu, remove_item_name)
    print("Updated menu:", menu)
    print("Availability:", check_item(menu, check_item_name))
