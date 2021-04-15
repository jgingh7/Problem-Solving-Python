# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Time: O(number of nodes)
# Space: O(height of tree)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0 # need to declare this instance variable
                     # so that all recusions can access this variable

        def dfs(node): # dfs returns the excess amount of coin, which is the same as how many coin shifts will happen
                       # excess can be -1 in the sense that the node is 0 and have -1 access amount
            if not node:
                return 0

            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R) #abs because it is to and from node's children
            return node.val + L + R - 1

        dfs(root)
        return self.ans