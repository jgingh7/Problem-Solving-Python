from collections import Counter

def solution(S):
    # write your code in Python 3.6
    strs = []
    for i in range(len(S)):
        for j in range(len(S)):
            added = S[i:j+1]
            if len(added) != 0:
                strs.append(added)
    # print(strs)

    ans = 0
    for element in strs:
        count = Counter(element)
        for i in count.values():
            if i == 1:
                ans += 1
    
    return ans

