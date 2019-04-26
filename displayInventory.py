stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displaeyInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' ' + str(v))
        item_total += v
    print('Total number of items : ' + str(item_total))

#displaeyInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin':42, 'rope':1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displaeyInventory(inv)

'''
for v in dragonLoot:
    if v in inv:
        inv[v] = inv[v] + 1
    else:
        inv[v] = 1
print(inv)
'''

