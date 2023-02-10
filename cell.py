from color import Color

class Cell:
    def __init__(self, value = 0, color = "white"):
        self.value = str(value)
        self.color = Color(color)

    def setValue(self, value):
        self.value = str(value)
    
    def getValue(self):
        return str(self.value)

    def setColor(self, color = "white"):
        if co.sColor(color):
            self.color = color
   
    def getColor(self):
        return self.color
    
    def toInt(self):
        return int(c.value)

    def toDouble(self):
        return float(c.value)
    
    def toDate(self):
        pass

    def reset(self):
        c.value = 0
        c.color = 'white'

c = Cell(32)

