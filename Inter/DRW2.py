# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    # write your code in Python 3.6
    idxDict = defaultdict(list)
    for i in range(len(A)):
        idxDict[A[i]].append(i) #keys are the values, values are indices

    ans = -1
    A.sort()
    if len(A) <= 1:
        return ans

    hasAdj = 0
    for i in range(len(A) - 1):
        if A[i] != A[i + 1]:
            hasAdj += 1
            if hasAdj == 1:
                ans = makeShortest(idxDict[A[i]], idxDict[A[i + 1]])
            else:
                ans = min(ans, makeShortest(idxDict[A[i]], idxDict[A[i + 1]]))
    
    return ans

def makeShortest (list1, list2):
    ans = abs(list1[0] - list2[0])
    for k in range(len(list1)):
        for l in range(len(list2)):
            ans = min(ans, abs(list1[k] - list2[l]))
    return ans