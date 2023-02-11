
from cell import Cell
from spreadsheet import Spreadsheet
from color import Color

s = Spreadsheet(3,4)
co = Color()
c = Cell()

c.setValue(12)
# print(c.getValue())

c.setColor("blue")
# print(c.getColor())

s.setCellAt(0,0)
c.setValue(12)
# print(c.getValue())

c.setColor("blue")

s.show()
# print(type(c.toInt()))
# print(type(c.toDouble()))

print("\n")
# c.reset(0,0)
s.show()
print("\n")

c.setValue(12)
c.setColor("blue")
s.setCellAt(0,0)

print(s.getCellAt(0,0))
print("\n")

s.addRow(0)
s.show()
print("\n")

s.removeRow(0)
s.show()
print("\n")

s.addColumn(0)
s.show()
print("\n")

s.removeColumn(0)
s.show()
print("\n")

s.swapColumns(0,2)
s.show()
print("\n")

s.swapRows(0,2)
s.show()
print("\n")
