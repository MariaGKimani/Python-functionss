class  Fruit:
    is_ripe = True
    def __init__(self,type,size,flavor):
        self.type =type
        self.size = size
        self.flavor = flavor
    def colors (self,color):
        self.color = color
        return f"the fruits are{self.color}"
    def name(self,names):
        self.names = names
        return f"she brought {self.names}"
    def price(self,price):
        self.price
        return f"hello your total is {self.price}"
