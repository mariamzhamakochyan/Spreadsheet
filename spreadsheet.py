from cell  import Cell

class Spreadsheet:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cells = [[0 for i in range(col)] for j in range(row)]

    def setCellAt(self, row, col, value):
        self.cells[row][col] = value
    
    def getCellAt(self, row, col):
        return self.cells[row][col]
    
    def addRow(self, index):
        self.cells.insert(index, [0 for i in range(self.cols)])
        for i in range(index + 1, self.rows):
            self.cells[i] = self.matrix[i - 1]

    def addColumn(self, index):
        for row in self.cells:
            row.insert(index, 0)
        self.cols += 1

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
