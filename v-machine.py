import beef 
import cheese 
import pepperoni 
import pizzafood
import snacks 
import vegan 

class v_machine:
    def __init__(self, iprice, item_name, quantity):
        self.iprice = iprice
        self.item_name = item_name
        self.quantity = quantity

    def description(self):
        return "Price: {}, Item name: {}, Quantity: {}".format(self.iprice, self.item_name, self.quantity)