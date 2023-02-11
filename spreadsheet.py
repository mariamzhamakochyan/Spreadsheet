from cell import Cell
from color import Color

class Spreadsheet:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cells = [[{c.value:c.color} for i in range(col)] for j in range(row)]

    def setCellAt(self, row, col, ):
        self.cells[row][col] = {c.getValue() : c.getColor()}
        return self.cells[row][col]
        
    def show(self):
        for i in self.cells:
            print('\t'.join(map(str, i)))

    def getCellAt(self, row, col):
        return self.cells[row][col]

    def addRow(self, index):
        self.cells.insert(index, [{'':"white"} for i in range(self.col)])

    def addColumn(self, index):
        for row in self.cells:
            row.insert(index, {'':"white"})
        self.col += 1

    def removeRow(self, row):
        del self.cells[row]
    
    def removeColumn(self, col):
        for row in self.cells:
            del row[col]
    
    def swapColumns(self, col1, col2):
        for row in self.cells:
            row[col1], row[col2] = row[col2], row[col1]
    
    def swapRows(self, row1, row2):
        self.cells[row1], self.cells[row2] = self.cells[row2], self.cells[row1]
        return self.cells[row1]

# s = Spreadsheet(3,4)
c = Cell(12, "blue")

# c.setValue(12)
# # print(c.getValue())

# c.setColor("blue")
# co = Color()