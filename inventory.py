"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""


def add_item_to_inventory(character, item):
    character["inventory"].append(item)
    print(f"{item} added to inventory!")


def remove_item_from_inventory(character, item):
    character["inventory"].remove(item)
    print(f"{item} was removed from inventory!")
