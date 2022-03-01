from unicodedata import name
from pizzafood import Pizza

class Pepperoni(Pizza):
    def __init__(self, size, tprice):
        Pizza.__init__(self, size)
        self.tprice = self.base_price + tprice

    def get_tprice(self):
        return self.tprice
    


m = Pepperoni("Large", 88)

print(m.get_tprice())
