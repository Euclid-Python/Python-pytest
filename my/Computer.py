class Computer:

    def __init__(self):
        self.total = 0

    def add(self,a):
        self.total = self.total + a
        return self.total

    def substract(self,a):
        self.total = self.total - a
        return self.total

    def reset(self):
        self.total = 0