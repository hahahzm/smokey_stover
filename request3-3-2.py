def printSolution(solution):
    n = len(solution)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, 201):
                if solution[i][j][k]:
                    print k,
            print " | ",
        print

def buildSolution(dimension):
    grid = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            solution = []
            for k in range(0, 201):
                solution.append(False)
            row.append(solution)
        grid.append(row)
    return grid

def setSolution(solution, i, j, food):
    solution[i][j][food] = True

def update(solution, grid):
    n = len(grid)
    for i in range(0, n):
        for j in range(0, n):
            if j > 0:
                for k in range(0, 201):
                    if solution[i][j-1][k]:
                        if k >= grid[i][j]:
                            solution[i][j][k-grid[i][j]] = True
            if i > 0:
                for k in range(0, 201):
                    if solution[i-1][j][k]:
                        if k >= grid[i][j]:
                            solution[i][j][k-grid[i][j]] = True

def extract(solution):
    n = len(solution)
    for k in range(0, 201):
        if solution[n-1][n-1][k]:
            return k
    return -1

def answer(food, grid):
    # your code here
    solution = buildSolution(len(grid))
    setSolution(solution, 0, 0, food)
    update(solution, grid)
    printSolution(solution)
    return extract(solution)


grid = []
grid.append([0,2,5])
grid.append([1,1,3])
grid.append([2,1,1])

print answer(7, grid)