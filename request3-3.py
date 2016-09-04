def printGrid(grid):
    for row in grid:
        print row

def buildGrid(dimension):
    grid = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(0)
        grid.append(row)
    return grid

def update(minimum, grid, a, b, flag):
    n = len(grid)
    for i in range(a, n):
        for j in range(b, n):
            if (i == 0) and (j == 0):
                continue
            elif i == 0:
                p = minimum[i][j - 1]
            elif j == 0:
                p = minimum[i - 1][j]
            else:
                if flag == "min":
                    p = min(minimum[i - 1][j], minimum[i][j - 1])
                else:
                    p = max(minimum[i - 1][j], minimum[i][j - 1])
            minimum[i][j] = p + grid[i][j]


def answer(food, grid):
    # your code here
    n = len(grid)

    minimum = buildGrid(n)
    maximum = buildGrid(n)

    minimum[0][0] = 0
    update(minimum, grid, 0, 0, "min")
    maximum[0][0] = 0
    update(maximum, grid, 0, 0, "max")

    printGrid(grid)
    print
    printGrid(minimum)
    print
    printGrid(maximum)
    print
    print
    print

    if minimum[n - 1][n - 1] > food:
        return -1

    bestfit = 0
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            minimum[i][j] = maximum[i][j]
            update(minimum, grid, i, j, "max")
            newmin = minimum[n - 1][n - 1]
            print newmin
            if newmin > food:
                continue
            elif newmin < food:
                if newmin > bestfit:
                    bestfit = newmin
            else:
                return 0



    return food - bestfit

grid = []
grid.append([0,2,5])
grid.append([1,1,3])
grid.append([2,1,1])

print answer(7, grid)