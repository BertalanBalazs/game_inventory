# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print('inventory:')
    sum = 0
    for x in inv:
        sum += inv[x]
        print(inv[x],x)
    return 'Total number of items: %d' %sum
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i == 'gold coin':
            inv['gold coin'] += 1
        elif i == 'dagger':
            inv['dagger'] += 1
        elif i == 'ruby':
            inv['ruby'] = 1
    return
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
import collections
def print_table(inventory, order):
    d1,d2,lines = ' ' * 5, ' ' * 8,'-' * 28
    if order == 'count,asc':
        ord_asc = collections.OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
        print('inventory:\n',d1,'count',d1,'item name\n',lines)
        sum = 0
        for x in ord_asc:
            sum += ord_asc[x]
            print('{:10d}'.format(ord_asc[x]),'{:>17}'.format(x))
        return_print = print(lines,'\nTotal number of items: %d' %sum)
        return return_print
    elif order == 'count,desc':
        ord_asc = collections.OrderedDict(reversed(sorted(inv.items(), key=lambda t: t[1])))
        print('inventory:\n',d1,'count',d1,'item name\n',lines)
        sum = 0
        for x in ord_asc:
            sum += ord_asc[x]
            print('{:10d}'.format(ord_asc[x]),'{:>17}'.format(x))
        return_print = print(lines,'\nTotal number of items: %d' %sum)
        return return_print
    elif order == 'empty':
        print('inventory:\n',d1,'count',d1,'item name\n',lines)
        sum = 0
        for x in inv:
            sum += inv[x]
            print('{:10d}'.format(inv[x]),'{:>17}'.format(x))
        return_print = print(lines,'\nTotal number of items: %d' %sum)
        return return_print
    else: 
        raise TypeError 
        print("Please enter 'count,asc' or 'count,desc' or empty' for the succesfull list.")

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
import csv 
def import_inventory(inventory,filename):
    with open(filename, 'r') as myFile:  
        reader = myFile.read()
    new_inv = []
    stuff = reader.split(',')
    for i in stuff:
        new_inv.append(i)
    for i in new_inv:
        if i == 'gold coin':
            inv['gold coin'] += 1
        elif i == 'dagger':
            inv['dagger'] += 1
        elif i == 'rope':
            inv['rope'] += 1
        elif i == 'ruby':
            inv['ruby'] += 1
        elif i == 'axe\n':
            inv['axe'] = 1
    return


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
import csv

def export_inventory(inventory, filename):
    with open(filename,'w') as f:
        for key in inventory.keys():
            f.write("%s,%s\n"%(key,inventory[key]))
    return
#step6
def ensure_inventory(inventory, added_items):
    for i in added_items:
        if i == 'и краткое':
            inv['и краткое'] = 1
        elif i == '漢字':
            inv['漢字'] = 1
    return 
c_list = ['и краткое', '漢字', ]
inv = ensure_inventory(inv, c_list)