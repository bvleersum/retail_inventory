#name: Bas van Leersum
#date: 4/11/2016


from RetailItem import *

def main():

    #creating empty lists
    description_list =[]
    units_list = []
    price_list = []

    #opening the documents with all the inventory information in it
    des = open("description.txt", "r")
    un = open("units.txt", "r")
    pr = open("price.txt", "r")

    #putting all the previous data in the lists
    for line in des:
        data = line.rstrip("\n")
        description_list.append(data)
    des.close()

    for line in un:
        data = line.rstrip("\n")
        units_list.append(data)
    un.close()

    for line in pr:
        data = line.rstrip("\n")
        price_list.append(data)
    pr.close()

    #adding new data to the lists if need
    another_item = True
    while another_item == True:

        add = input("Do you want to add another item to the inventory? 'yes' or 'no'")
        if add.lower() == "yes":
            description = input("What is the item's description?")
            units = str(int(input("How many units are there of this item?")))
            price = str(format(float(input("What is the price per unit?")),".2f"))
            print("Is the following correct?")
            print("description:", description)
            print("units", units)
            print("price", price)
            correct = input("'yes' or 'no'")

            if correct.lower() == "yes":
                description_list.append(description)
                units_list.append(units)
                price_list.append(price)

        else:
            another_item = False

    #print inventory for all the items in the lists
    for i in range (len(description_list)):
        item = RetailItem(description_list[i], units_list[i], price_list[i])

        print()
        print("Item #" + str(1+i))
        print(item)

    #add all the new data to the .txt documents so it can be used next time
    des = open("description.txt", "w")
    un = open("units.txt", "w")
    pr = open("price.txt", "w")

    for i in range(len(description_list)):
        des.write(description_list[i] + '\n')
    des.close()
    for i in range(len(description_list)):
        un.write(units_list[i] + '\n')
    un.close()
    for i in range(len(description_list)):
        pr.write(price_list[i] + '\n')
    pr.close()

main()