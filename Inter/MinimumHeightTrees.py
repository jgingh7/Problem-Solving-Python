# https://leetcode.com/problems/minimum-height-trees/
# Time: O(V)
# Space: O(V) - edges + leaves

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]
        
        # make adjacency list of tree edges
        tree = defaultdict(set)
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
        
        # check for leaves
        leaves = []
        for key in tree:
            if len(tree[key]) == 1:
                leaves.append(key)
                
        while True:            
            newLeaves = []
            for leaf in leaves:
                fixNeededNode = tree[leaf].pop()
                tree[fixNeededNode].remove(leaf) # remove leaf from the nodes that connect the leaf
                if len(tree[fixNeededNode]) == 1: # if the connecting node becomes a leaf, set it as newLeaf
                    newLeaves.append(fixNeededNode)
                
                tree.pop(leaf) # remove leaf from the tree
                

            if len(tree) <= 2: # there are at most 2 roots possible for a MHT
                return tree.keys()
            
            leaves = newLeaves #set next leaves as newLeaves
