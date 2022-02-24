class Chart1:
    def __init__(self,ID='', Product='', Price=''):
        self.ID = ID,
        self.Product = Product,
        self.Price = Price,

    def serialize(self):
        return {
            'ID':self.ID,
            'Product':self.Product,
            'Price':self.Price,
        }