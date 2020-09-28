#https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/
#Time: O(n) where n is the number of tasks
#Space: O(1) - will not be more than O(26)

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = list(Counter(tasks).values()) # if ["A","A","A","B","B","B","C"], taskCounts = list(dict_values([3, 3, 1]))
                                                   # needs to do list(), because dict_values dont have .count()      O(n)

        maxCount = max(taskCounts) # greedy approach: keep track of the most frequent occuring tasks, since all other tasks can be inserted within that task     O(n)
        maxCountTasks = taskCounts.count(maxCount) #.count() gives how many times the given object occurs in the list     O(n)
                                                   #maximum for this is 26

        return max(len(tasks), (maxCount - 1) * (n + 1) + maxCountTasks) #O(1)
        #getting the maximum of this, is getting minimum length, since it inserts all REPEATING tasks (and non-repeating after) within the slots:
        #
        #A: (maxCount - 1) * (n + 1) + maxCountTasks):
        # 1. maxCount - 1, "maxCountingTaks + idle + other" task slots
        #    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
        #    -----------    -----------    -----------    -----------------    ----------------- (5 slots)
        #
        # 2. n + 1, since at max there are n "idle + other" + the maxcounting task
        #    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
        #    1-|----n---    1-|----n---    1-|----n---    1-|-------n------    1-|-------n------
        #
        # 3. + maxCountTask, since if idle spots are not filled, there will be exactly maxCountTask more tasks done after the slots
        #    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
        #                                                                                          (maxCountTasks)
        #
        #B: len(tasks):
        # 1. when n = 0, len(tasks) become larger
        # 2. when idle slots are all filled up

