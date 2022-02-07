global N
N = 9


def Grid_Print(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()



def isSafe(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False


    for x in range(9):
        if grid[x][col] == number:
            return False


    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == number:
                return False
    return True


def solveSuduko(grid, row, col):

    if (row == N - 1 and col == N):
        return True


    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSuduko(grid, row, col + 1)
    for number in range(1, N + 1, 1):

        if isSafe(grid, row, col, number):
            grid[row][col] = number

            if solveSuduko(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False


grid = [[2, 1, 0, 0, 0, 0, 5, 0, 0],
        [7, 0, 3, 0, 0, 8, 6, 9, 0],
        [0, 0, 6, 1, 7, 0, 0, 0, 8],
        [0, 6, 0, 4, 0, 0, 0, 7, 3],
        [0, 8, 5, 7, 3, 6, 9, 0, 0],
        [3, 0, 0, 9, 8, 2, 0, 0, 0],
        [0, 0, 9, 8, 0, 3, 7, 5, 0],
        [5, 3, 1, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 5, 0, 0, 3, 0, 6]]

if (solveSuduko(grid, 0, 0)):
    Grid_Print(grid)
else:
    print("no solution  exists ")