def addToInventory(inventory,addedItems):
    for subject in addedItems:
        if subject in inventory.keys():
            inventory[subject]=int(inventory[subject]+1)
        else:
            inventory[subject]=1
    return inventory

def displayInventory(inventory):
    counter=0
    print('Inventory:')
    for k,v in inventory.items():
        print(str(v)+' '+k)
        counter=counter+v

inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
