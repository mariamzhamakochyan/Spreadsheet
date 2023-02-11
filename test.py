from cell import Cell
from spreadsheet import Spreadsheet
from color import Color

#setValue function turn any argument into a string
def testsetValue(value):
    if isinstance(c.setValue(value), str):
        print("Test setValue ... passed")
    else:
        print("Test setValue ... Failed")

def testgetValue():
    if c.getValue() == c.value:
         print("Test getValue ... passed")
    else:
        print("Test getValue ... Failed")

def testsetColor(color): 
    if color in co.colors:
        print("Test setColor ... passed")
    else:
        print("Test setColor ... Failed")

def testgetColor():
    if c.getColor() == c.color:
         print("Test getColor ... passed")
    else:
        print("Test getColor ... Failed")

def testtoInt():
    if isinstance(c.toInt(), int):
        print("Test toInt ... passed")
    else:
        print("Test toInt ... Failed")

def testtoDouble():
    if isinstance(c.toDouble(), float):
        print("Test toDouble ... passed")
    else:
        print("Test toDouble ... Failed")

def testsetCellAt(row, col):
    s.setCellAt(row, col)
    if s.setCellAt(row, col) == s.getCellAt(row, col):
        print("Test setCellAt ... Passed")
    else:
        print("Test setCellAt ... Failed") 

def testgetCellAt(row, col):
    s.setCellAt(row,col)
    if s.getCellAt(row, col) == s.cells[row][col]:
        print("Test getCellAt ... Passed")
    else:
        print("Test getCellAt ... Failed") 

def testaddRow(index):
    row = len(s.cells)
    s.addRow(index)
    if len(s.cells) == row + 1:
        print("Test addRow ... passed")
    else:
        print("Test addRow ... failed")

def testaddColumn(index):
    col = len(s.cells[0])
    s.addColumn(index)
    if len(s.cells[0]) == col + 1:
        print("Test addColumn ... passed")
    else:
        print("Test addColumn ... failed")

def testremoveRow(index):
    row = len(s.cells)
    s.removeRow(index)
    if len(s.cells) == row - 1:
        print("Test removeRow ... passed")
    else:
        print("Test removeRow ... failed")

def testremoveColumn(index):
    row = len(s.cells[0])
    s.removeColumn(index)
    if len(s.cells[0]) == row - 1:
        print("Test removeColumn ... passed")
    else:
        print("Test removeColumn ... failed")

def testswapRows(row1, row2):
    s.setCellAt(0,0)
    c1 = s.cells[row1]
    c2 = s.cells[row2]
    s.swapRows(row1,row2)
    if c2 == s.cells[row1] and c1 == s.cells[row2]:
        print("Test swapRows ... passed")
    else:
        print("Test swapRows ... failed")

def testswapColumns(col1, col2):
    s.setCellAt(0,0)
    c1 = s.cells[col1][0]
    c2 = s.cells[col2][col2]
    s.swapColumns(col1,col2)
    if c2 == s.cells[col1][0] and c1 == s.cells[col2][col2]:
        print("Test swapColumns ... passed")
    else:
        print("Test swapColumns ... failed")


# s = Spreadsheet(3,4)
# co = Color()
# c = Cell()

# testsetValue("12")
# testgetValue()
# testsetColor("blue")
# testgetColor()
# testtoInt()
# testtoDouble()

# testsetCellAt(0,0)
# testgetCellAt(0,0)
# testaddRow(2)
# testaddColumn(1)
# testremoveRow(2)
# testremoveColumn(1)
# testswapRows(0,1)
# testswapColumns(0,1)