from cell import Cell
from color import Color

class Spreadsheet:
    def __init__(self, row, col):
        if row >= 0 and col >=0:
            self.row = row
            self.col = col
            self.cells = [[c for _ in range(col)] for _ in range(row)]
        else:
            return "row, and col must be a positive numbers"

    def setCellAt(self, row, col):
        self.cells[row][col] = (c.setValue(c.value), c.setColor(c.color))
        return self.cells[row][col]
        
    def show(self):
        for i in self.cells:
            print('\t'.join(map(str, i)))

    def getCellAt(self, row, col):
        if len(self.cells) > row >= 0 and len(self.cells[0]) > col >= 0:
            return self.cells[row][col]
        else:
            print("Can not be found")

    def addRow(self, index):
        if 0 <= index <= len(self.cells):
            self.cells.insert(index, [{'':"white"} for i in range(self.col)])
        else:
            print("Index is out of range, try another one")

    def addColumn(self, index):
        if 0 <= index <= len(self.cells[0]):
            for row in self.cells:
                row.insert(index, {'':"white"})
            self.col += 1
        else:
            print("Index is out of range, try another one")          

    def removeRow(self, row):
        if len(self.cells) > row >= 0:
            del self.cells[row]
        else:
            print("Row can not be found to delete")
    
    def removeColumn(self, col):
        if len(self.cells[0]) > col >= 0:
            for row in self.cells:
                del row[col]
        else:
            print("Column can not be found to delete")

    def swapColumns(self, col1, col2):
        if len(self.cells[0]) > col1 >= 0 and len(self.cells[0]) > col2 >= 0:
            for row in self.cells:
                row[col1], row[col2] = row[col2], row[col1]
        else:
            print("Columns can not be swapped")
    
    def swapRows(self, row1, row2):
        if len(self.cells) > row1 >= 0 and len(self.cells) > row2 >= 0:
            self.cells[row1], self.cells[row2] = self.cells[row2], self.cells[row1]
            return self.cells[row1]
        else:
            print("Rows can not be swapped")

c = Cell()
c.setValue("12")
c.setColor("blue")
