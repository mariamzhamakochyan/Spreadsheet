from color import Color

class Cell:
    def __init__(self, value = '', color = "white"):
        self.value = ''
        self.color = "white"
        self.cl = {self.value:self.color}
    
    def setValue(self, value):
        self.value = str(value)
        return self.value
    
    def getValue(self):
        return str(self.value)
        
    def n(self,val,col):
        val = getValue()
        col = getColor()
        self.cl = {val:col}

    def setColor(self, color):
        if co.sColor(color):
            self.color = color
            return self.color
   
    def getColor(self):
        return self.color
    
    def toInt(self):
        res = True
        try:
           int(self.value)
        except ValueError:
            res = False
        if res:
            return int(self.value)
        else:  
            print( "Value can not be an integer")
    

    def toDouble(self):
        res = True
        try:
           float(self.value)
        except ValueError:
            res = False
        if res:
            return float(self.value)
        else:  
            print( "Value can not be a float")
    
    def toDate(self):
        pass

    def reset(self, row, col):
        self.value = ''
        self.color = 'white'
        s.setCellAt(row, col)

co = Color()