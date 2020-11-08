# https://www.hackerrank.com/challenges/magic-square-forming/problem
# Time: O(1)
# Space: O(1)

pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    totals = []
    for p in pre:                      # for each possible magic matrix,
        total = 0
        for p_row, s_row in zip(p, s): # compare each element on each position,
            for i, j in zip(p_row, s_row):
                if not i == j:         # and if not equal, add the difference to the total (this total is for each p)
                    total += abs(i - j)
        totals.append(total)
    return min(totals)                 # get the minimum of those totals
