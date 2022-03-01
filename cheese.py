from pizzafood import Pizza

class Cheese(Pizza):
    def __init__(self, size, tprice):
        Pizza.__init__(self, size)
        self.tprice = tprice

    def get_tprice(self):
        return self.base_price + self.tprice
    

    



