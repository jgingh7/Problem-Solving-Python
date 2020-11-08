# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
groupAdict = defaultdict(list)
groupB=[]

n, m = map(int, input().split()) #raw_input() gives first line of input
                                    #n, m takes each element and put them into value

for i in range(0,n):
    groupAdict[input()].append(i+1)

for i in range(0,m):
    groupB += [input()]  

for num in groupB: 
    if num in groupAdict:
        print(" ".join( map(str,groupAdict[num]) ))
    else:
        print(-1)