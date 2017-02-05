

stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragon_loot = {
    'gold coin': 4,
    'dagger': 1,
    'ruby': 1,
    'rope': 1
}

def display_inventory(inventory):
    print('Inventory: ' + str(stuff))
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + 1
    print('Total number of unique items: ' + str(item_total))

def add_to_inventory(stuff, added_items):
    for item in dragon_loot:
        if item not in stuff.keys():
            stuff[item] = dragon_loot[item]
        else:
            stuff[item] += dragon_loot[item]
    return stuff




add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)

