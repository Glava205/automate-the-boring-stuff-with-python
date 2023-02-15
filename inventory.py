inventory={}
while True:
    print('Введите название предмета который присутствует в инвентаре,для выхода ничего не вводите.')
    subject=input()
    print('Введите количество этого предмета в вашем инвенторе, для выхода нечего не вводите.')
    num=input()
    if subject=='' or num=='':
        break
    else:
        inventory[subject]=int(num)
def displayInventory(inventory):
    counter=0
    print('Inventory:')
    for k,v in inventory.items():
        print(str(v)+' '+k)
        counter=counter+v

    print('Total number of items: '+str(counter))

displayInventory(inventory)
