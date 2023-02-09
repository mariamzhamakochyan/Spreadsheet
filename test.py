from cell  import Cell
from spreadsheet import Spreadsheet

def testsetCellAt(row, col, value):
    if s.getCellAt(row, col) == value:
        print("setValue: Passed")
    else:
        print("setValue: Failed")

def testgetCellAt(row, col):
    if s.getCellAt(row, col) == s.cells[row][col]:
        print("getCellAt: Passed")
    else:
        print("getCellAt: Failed")

# def testaddRow(index):
#     if spreadsheet.getrow(index) = 

# def testaddColumn(index)
# def testremoveRow(row)
# def testremoveColumn(col)
# def testswapColumns(col1, col2):

def testswapRows(row1, row2):
    if  s.swapRows(row1, row2)==s.getrow(row1):
        print("passed")
    else:
        print("Failed")


def testsetValue(value):
    if c.getValue() == value:
        print("Passed")
    else:
        print("Failed")

def testsetValue():
    if type(c.getValue()) == str:
        print("setValue: Passed")
    else:
        print("setValue: Failed")

# def testsetColor(color):
#     if c.getColor(c.setColor(color)) == color:
#         print("Passed")
#     else:
#         print("Failed")

# def testgetColor():
#     if type(c.getColor()) == int:
#         print('Passed')
#     else:
#         print("Failed")

def testtoInt():
    res = isinstance(c.getValue(), int)
    if res == c.toInt():
        print("toInt: Passed")
    else:
        print("toInt: Failed") 

def testtoDouble():
    res = isinstance(c.getValue(), float)
    if res == c.toDouble():
        print("toDouble: Passed")
    else:
        print("toDouble: Failed") 

def testisData():
    pass


c = Cell(3,4)
s = Spreadsheet(5,5)
s.setCellAt(3,4,"12")
c.setValue("12")
c.setColor(2)
c.getValue()
c.getColor()
c.toInt()
c.toDouble()
c.reset()
# s.swapRows(1,2)


testsetCellAt(3,4,"12")
testgetCellAt(3, 4)
testsetValue()
testsetValue()
testtoInt()
testtoDouble()
# testswapRows(2, 1)
# testsetColor()