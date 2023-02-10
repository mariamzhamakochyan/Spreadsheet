from cell import Cell
from spreadsheet import Spreadsheet
from color import Color
import test


co = Color()
c = Cell()
s = Spreadsheet(3,4)

c.setValue(12)
print(c.getValue())

c.setColor("blue")
print(c.getColor())

s.setCellAt(0,0)
s.show()
print("\n")
c.reset(0,0)
s.show()
