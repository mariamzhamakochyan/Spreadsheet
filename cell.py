from color import Color

class Cell:
    def __init__(self, value, color):
        self.value = value
        self.color = None

    def setValue(self, value):
        self.value = str(value)

    def setColor(self, color):
        self.color = Color(color)
    
    def getValue(self):
        return self.value
    
    def getColor(self):
        return self.color
    
    def toInt(self):
        return int(self.value)

    def toDouble(self):
        return float(self.value)
    
    def toDate(self):
        pass

    def reset(self):
        self.value = 0
        self.color = 'white'
