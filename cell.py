from color import Color
from datetime import datetime

class Cell:
    def __init__(self, value = '', color = "white"):
        self.value = ''
        self.color = "white"
    
    def setValue(self, value):
        self.value = str(value)
        return self.value
    
    def getValue(self):
        return str(self.value)

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
        res = True
        date_string = self.value
        try:
            todate = datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError:
            res = False
        if res:
            return todate
        else:
            print("Value can not have the format YYYY/MM/DD")

    def reset(self):
        self.value = ''
        self.color = 'white'

co = Color()
