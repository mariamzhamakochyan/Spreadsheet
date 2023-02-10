from cell  import Cell

class Spreadsheet:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cells = [[0 for i in range(col)] for j in range(row)]

    def setCellAt(self, row, col):
        self.cells[row][col] = {c.value : co.color}
        
    def show(self):
        return self.cells

    def getCellAt(self, row, col):
        return self.cells[row][col]

    def addRow(self, index):
        self.cells.insert(index, [0 for i in range(self.col)])

    def addColumn(self, index):
        for row in self.cells:
            row.insert(index, 0)
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
s = Spreadsheet(3,4)
