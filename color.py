class Color:
    def __init__(self, color = "white"):
        self.color = color
        self.colors = {'red':0, 'green':1, 'blue':2, 'black':3}
    
    def getColor(self):
        return self.colors[self.color]
    
    def setColor(self, color = "white"):
        if color in self.colors:
            self.color == color
        else:
            print("We dont have that color yet")

co = Color()
