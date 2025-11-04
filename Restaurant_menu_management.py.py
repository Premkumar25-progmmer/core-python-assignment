def add_item(menu, item):
    menu.append(item)
    return menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(item, "not found in the menu")
    return menu
def check_item(menu, item):
    if item in menu:
        return item + " is available"
    else:
        return item + " is not available"
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item_name = "Tacos"
remove_item_name = "Salad"
check_item_name = "Pizza"
menu = add_item(menu, add_item_name)
menu = remove_item(menu, remove_item_name)
availability = check_item(menu, check_item_name)
print("Updated menu:", menu)
print("Availability:", availability)
