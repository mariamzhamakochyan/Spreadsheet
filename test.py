from cell import Cell
from spreadsheet import Spreadsheet
from color import Color

#setValue function turn any argument into a string
def testsetValue(value):
    if isinstance(c.setValue(value), str):
        print("Test setValue: passed")
    else:
        print("Test setValue: Failed")

def testgetValue():
    if c.getValue() == c.value:
         print("Test getValue: passed")
    else:
        print("Test getValue: Failed")

def testsetColor(color): 
    if color in co.colors:
        print("Test setColor: passed")
    else:
        print("Test setColor: Failed")

def testgetColor():
    if c.getColor() == c.color:
         print("Test getColor: passed")
    else:
        print("Test getColor: Failed")

def testtoInt():
    if isinstance(c.toInt(), int):
        print("Test toInt: passed")
    else:
        print("Test toInt: Failed")

def testtoDouble():
    if isinstance(c.toDouble(), float):
        print("Test toDouble: passed")
    else:
        print("Test toDouble: Failed")

def testreset():
    pass

# def testsetCellAt(row, col):
#     if s.setCellAt(row, col) == s.cl:
#         print("testsetCellAt: Passed")
#     else:
#         print("testsetCellAt: Failed") 
    




s = Spreadsheet(3,4)
co = Color()
c = Cell()

testsetValue("12")
testgetValue()
testsetColor("blue")
# testgetColor()
# testtoInt()
# testtoDouble()
# testsetCellAt(0,0)
s.show()









# def testgetCellAt(row, col):
#     if s.getCellAt(row, col) == s.cells[row][col]:
#         print("getCellAt: Passed")
#     else:
#         print("getCellAt: Failed")

# def testswapRows(row1, row2):
#     if  s.swapRows(row1, row2)==s.getrow(row1):
#         print("passed")
#     else:
#         print("Failed")


# def testsetValue(value):
#     if c.getValue() == value:
#         print("Passed")
#     else:
#         print("Failed")

# def testsetValue():
#     if type(c.getValue()) == str:
#         print("setValue: Passed")
#     else:
#         print("setValue: Failed")


# def testtoInt():
#     res = isinstance(c.getValue(), int)
#     if res == c.toInt():
#         print("toInt: Passed")
#     else:
#         print("toInt: Failed") 

# def testtoDouble():
#     res = isinstance(c.getValue(), float)
#     if res == c.toDouble():
#         print("toDouble: Passed")
#     else:
#         print("toDouble: Failed") 

# def testisData():
#     pass

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
# def testaddRow(index):
#     if spreadsheet.getrow(index) = 

# def testaddColumn(index)
# def testremoveRow(row)
# def testremoveColumn(col)
# def testswapColumns(col1, col2):








# s.setCellAt(3,4,"12")
# c.getValue()
# c.getColor()
# c.toInt()
# c.toDouble()
# c.reset()
# s.swapRows(1,2)


# testsetCellAt(3,4,"12")
# testgetCellAt(3, 4)
# testsetValue()
# testtoInt()
# testtoDouble()
# testswapRows(2, 1)
# testsetColor()
# def testsetCellAt(row, col, value):
#     if s.getCellAt(row, col) == value:
#         print("setValue: Passed")
#     else:
#         print("setValue: Failed")