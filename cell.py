import main

class Cell:
    def __init__(self, value = '', color = "white"):
        self.value = str(value)
        self.color = color

    def setValue(self, value):
        self.value = str(value)
    
    def getValue(self):
        return str(self.value)

    def setColor(self, color):
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

    def reset(self, row, col):
        self.value = ''
        self.color = 'white'
        s.setCellAt(row, col)