# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Time: O(len(player) * log(len(ranked)))
# Space: O(len(ranked))

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank = 1
    d = {}
    
    # O(len(ranked))
    for i, baseScore in enumerate(ranked): #make a hashmap of scores and their rank
        if i == 0:
            d[baseScore] = rank
        else:
            if ranked[i - 1] == baseScore:
                d[baseScore] = rank
            else:
                rank += 1
                d[baseScore] = rank

    ans = []

    #O(len(player) * log(len(ranked)))
    for score in player:
        if score in d: #if the score is in hashmap, just append the rank
            ans.append(d[score])
            continue
        else:
            l = 0
            r = len(ranked) - 1
            while l <= r: #need to check the last number (l==r number) too
                mid = l + ((r - l) // 2)
                if ranked[mid] > score:
                    l = mid + 1
                elif ranked[mid] < score:
                    r = mid - 1
                # elif ranked[mid] == score: #this does not happen, because "if score in d" has already taken this into account

            if l == 0: #if l comes down to 0, it is rank 1
                ans.append(1)
            else: #get the rank on the left and add 1
                ans.append(d[ranked[l - 1]] + 1)
    
    return ans