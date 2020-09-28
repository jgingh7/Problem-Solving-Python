#https://www.lintcode.com/problem/find-the-celebrity/description
#Time: O(n)
#Space: O(1)

def findcelebrity(self, n):
    cand = 0 
    for i in range(n):
        if knows(cand, i):
            cand = i # the candidate is automatically updated to i because if a candiate knows someone, he/she is no longer a candiate for celebrity
                     # because everyone knows the celebrity, this can rule out people that are not known to somebody, and people that knows somebody,
                     # leaving just 1 candidate left

    for i in range(n):
        if i == cand:
            continue
        else:
            if not knows(i, cand) or know(cand, i): #if somebody does not know candidate or the candidate knows somebody, than there is no celebrity
                return -1
    return cand
