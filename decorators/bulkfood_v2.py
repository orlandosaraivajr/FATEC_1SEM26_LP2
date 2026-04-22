class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # (1)
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property  # (2)
    def weight(self):  # (3)
        return self.__weight  # (4)

    @weight.setter  # (5)
    def weight(self, value):
        if value > 0:
            self.__weight = value  # (6)
        else:
            raise ValueError('value must be > 0')  # (7)


raisins = LineItem('Golden raisins', 10, 6.95)
print(raisins.subtotal())
raisins.weight = -20
print(raisins.subtotal())
