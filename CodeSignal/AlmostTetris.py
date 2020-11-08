# https://leetcode.com/discuss/interview-question/842141/databricks-oa
n = 4
m = 7
figures = [4,2,1,3,5,2,5]

def almostTetris(n, m, figures):
    grid = [[0] * m for _ in range(n)]

    def shape1(count):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    grid[i][j] = count
                    return

    def shape2(count):
        for i in range(n):
            for j in range(m - 2):
                if grid[i][j] == 0 and grid[i][j + 1] == 0 and grid[i][j + 2] == 0:
                    grid[i][j] = grid[i][j + 1] = grid[i][j + 2] = count
                    return
    
    def shape3(count):
        for i in range(n - 1):
            for j in range(m - 1):
                if grid[i][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                    grid[i][j] = grid[i][j + 1] = grid[i + 1][j] = grid[i + 1][j + 1] = count
                    return

    def shape4(count):
        for i in range(n - 2):
            for j in range(m - 1):
                if grid[i][j] == 0 and grid[i + 1][j] == 0 and grid[i + 2][j] == 0 and grid[i + 1][j + 1] == 0:
                    grid[i][j] = grid[i + 1][j] = grid[i + 2][j] = grid[i + 1][j + 1] = count
                    return
    
    def shape5(count):
        for i in range(n - 1):
            for j in range(m - 2):
                if grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0 and grid[i + 1][j + 2] == 0 and grid[i][j + 1] == 0:
                    grid[i + 1][j] = grid[i + 1][j + 1] = grid[i + 1][j + 2] = grid[i][j + 1] = count
                    return
    
    for i in range(len(figures)):
        if figures[i] == 1:
            shape1(i + 1)
        elif figures[i] == 2:
            shape2(i + 1)
        elif figures[i] == 3:
            shape3(i + 1)
        elif figures[i] == 4:
            shape4(i + 1)
        elif figures[i] == 5:
            shape5(i + 1)                        
    
    return grid


print(almostTetris(n, m, figures))