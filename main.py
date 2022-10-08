grid = [[2,1,1],[1,1,0],[0,1,1]]

def updateGrid(grid):
    for nRow in range(len(grid)):
        for nCol in range(len(grid[nRow])):
            if (grid[nRow][nCol] == 1):
                # first row
                if (nRow == 0 and nCol == 0):
                    if (grid[nRow][nCol + 1] == 2 or grid[nRow + 1][nCol] == 2):
                        grid[nRow][nCol] == 2
                elif (nRow == 0 and nCol == len(grid[nRow]) - 1):
                    if (grid[nRow][nCol - 1] == 2 or grid[nRow + 1][nCol] == 2):
                        grid[nRow][nCol] == 2
                elif (nRow == 0):
                    if (grid[nRow][nCol - 1] == 2 or grid[nRow][nCol + 1] == 2):
                        grid[nRow][nCol] == 2

                # last row
                elif (nRow == len(grid) - 1 and nCol == 0):
                    if (grid[nRow][nCol + 1] == 2 or grid[nRow - 1][nCol] == 2):
                        grid[nRow][nCol] == 2
                elif (nRow == len(grid) - 1 and nCol == len(grid[nRow]) - 1):
                    if (grid[nRow][nCol - 1] == 2 or grid[nRow - 1][nCol] == 2):
                        grid[nRow][nCol] == 2
                elif (nRow == len(grid) - 1):
                    if (grid[nRow][nCol - 1] == 2 or grid[nRow][nCol + 1] == 2):
                        grid[nRow][nCol] == 2

                # first col
                elif (nCol == 0):
                    if (grid[nRow][nCol + 1] == 2 or grid[nRow + 1][nCol] == 2 or grid[nRow - 1][nCol] == 2):
                        grid[nRow][nCol] == 2

                # last col
                elif (nCol == len(grid[nRow]) - 1):
                    if (grid[nRow][nCol - 1] == 2 or grid[nRow + 1][nCol] == 2 or grid[nRow - 1][nCol] == 2):
                        grid[nRow][nCol] == 2

                else:
                    if (grid[nRow - 1][nCol] == 2 or grid[nRow + 1][nCol] == 2 or grid[nRow][nCol - 1] == 2 or
                            grid[nRow][nCol + 1] == 2):
                        grid[nRow][nCol] == 2
    return grid

def complete(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                return False
    return True

def getMinimum(grid):
    retVal = 0
    while True:
        grid = updateGrid(grid)
        retVal+=1
        if complete(grid):
            return retVal

getMinimum(grid)