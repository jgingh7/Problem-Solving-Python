# https://www.hackerrank.com/challenges/non-divisible-subset/problem
# Time: O(s)
# Space: O(k)

def nonDivisibleSubset(k, s):
    # Write your code here
    remainderCounter = [0] * k
    
    # if the remainders of 2 numbers add up to k, the 2 numbers' sum is divisible by k
    # so count the remainders of the array, add number with more count to the res.
    # if the number is 0 or exact half of k, add just 1 if there is a count.
    for num in s:
        remainderCounter[num % k] += 1

    res = 0
    for i in range(len(remainderCounter) // 2 + 1):
        if k - i == i or i == 0: # if the number is 0 or exact half of k, add just 1 if there is a count
            if remainderCounter[i] != 0:
                res += 1
        else: # add number with more count to the res
            res += max(remainderCounter[i], remainderCounter[k - i])
        
    return res