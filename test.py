from cell  import Cell
from spreadsheet import Spreadsheet


def testsetCellAt(row, col, value):
    if spreadsheet.getCellAt(row, col) == value:
        print("Passed")
    else:
        print("Failed")

def testgetCellAt(row, col):
    if spreadsheet.getCellAt(row, col) == spreadsheet.cells[row][col]:
        print("Passed")
    else:
        print("Failed")

def testaddRow(index):
    
def testaddColumn(index)
def testremoveRow(row)
def testremoveColumn(col)
def testswapColumns(col1, col2)
def testswapRows(row1, row2)


def testsetValue(value):
    if cell.getValue(cell.setValue(value)) == value:
        print("Passed")
    else:
        print("Failed")

def testsetValue():
    if type(cell.getValue()) == str:
        print("Passed")
    else:
        print("Failed")

def testsetColor(color):
    if cell.getColor(cell.setColor(color)) == color:
        print("Passed")
    else:
        print("Failed")

def testgetColor():
    if type(cell.getColor()) == int:
        print('Passed')
    else:
        print("Failed")

def testtoInt():
    assert cell.setValue(1) == True
    assert cell.setValue(1.2) == False
    assert cell.setValue("1") == False

def testtoDouble():
    assert cell.setValue(1) == False
    assert cell.setValue(1.2) == True
    assert cell.setValue("1") == False

def testisData():
    assert cell.setValue(1) == False
    assert cell.setValue("1") == False
    assert cell.setValue(1.2) == False
    assert cell.setValue("data") == True


































# from cell import Cell
# from color import Color
# from main import SpreadSheet

# def testsetValue(23):
#     res = isinstance(23, str)
#     if res == 23:
#         print("Pass")

# def testsetColor(Red):
#     if  Red == Color.Red:
#         print("pass")

# def testgetValue(2,3, "Hello"):
#     if type(SpreadSheet.Cells[2][3]) == str:
#         if Spreadsheet.Cells[2][3] == "Hello":
#             print('pass')    
#     else:
#         print("Faild")
    
# def setCellAt(3, 4):
#     if len(Spreadsheet.Cells) == 3 and len(SpreadSheet.Cells[0]) == 4:
#         print("pass")
# def testget
        
# def testgetColor(2,3,1):
#     if Spreadsheet.Cells[2][3] == "Red":
#         print("pass")

# def testtoInt(12, res):
#     res = isinstance(12, int)
#     if 12 == res:
#         print("pass")
#     else:
#         print("Faild: can not be an integer")

# # def getCellAt():
# #     if 


# def testreset(2,3):
#     if SpreadSheet.Cells[2][3] = '':
#         print("pass"):
#     else:
#         print("faild")

# def testwapColumns(2,3):
#     s = SpreadSheet.Cell
#     if SpreadSheet.Cell[2] == 

# def testremoveRow(3):
#     if SpreadSheet.row == len(SpreadSheet.Cell):
#         print("Faild")
#     else:
#         print("Pass")

# def testremoveColumn(3):
#     if SpreadSheet.colum == len(SpreadSheet.Cell[0]):
#         print("Faild")
#     else:
#         print("Pass")

# def testswapRows(2, 3):
#     if SpreadSheet.Cell[2][4] == "Hello":
#         print("Pass")

# def testwapColumns(2, 3):
#     if SpreadSheet.Cell[1][2] == "cell12":
#         print('pass')
    

# def testaddColumn(3):
#     if SpreadSheet.row + 1 == len(SpreadSheet.Cell):
#         print("pass")


