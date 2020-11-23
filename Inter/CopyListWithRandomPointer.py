# https://leetcode.com/problems/copy-list-with-random-pointer/
# Time: O(n)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        
        def deepCopy(node: 'Node') -> 'Node':
            if not node:
                return None

            #if node does not exist in map,
            #  a) node may be the first node,
            #  b) or a node of future called by random
            if node not in d:
                #place copy of that node without setting the next and random values
                d[node] = Node(node.val, None, None)

                #set the next and random value
                d[node].next = deepCopy(node.next)
                d[node].random = deepCopy(node.random)
                
            #this eventually populates the map with all nodes

            return d[node] #if node is in map, return that node
        
        return deepCopy(head)