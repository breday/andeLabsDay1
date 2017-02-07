#SHOPPING CART OOP
class Item(object): 
    def __init__(self,id, name, price, quantity ):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    #getters
    def get_name(self):
        return self._name
             
    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

        
    
class Cart:
    def __init__(self, list):
        self.list = []

    def newItem(self, item):
        self.list.append(self.list)

    def totalPrice(self):
        total = 0
        for item in self.list:
             price = item[1] 
            total = total + price

    def NumbOfItems(self):
        i = 0
        for x in range(self.list):
            i = self.list + 1
            return i

    def remove(self, item):
        for x in self.quantity:
            if item == x:
                self.quantity.remove(item)
                self._price -= item.get_price()
        return(Cart)

        







