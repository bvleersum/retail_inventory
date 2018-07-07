class RetailItem:


    def __init__(self, description, units, price):

        self.__description = description
        self.__units = units
        self.__price = price

    def get_description(self):
        return self.__description

    def set_decription(self, description):
        self.__description = description

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return "Description: \t " + self.get_description() + "\nUnits: \t\t\t " + str(self.get_units()) + "\nPrice: \t\t\t $" + str(format(float(self.get_price()),".2f"))