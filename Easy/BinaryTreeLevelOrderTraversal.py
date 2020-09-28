# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Time: O(number of nodes)
# Space: O(number of nodes)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, level = [], [root]
        while level: #if current leaves have non-null leaves
            ans.append([node.val for node in level]) # add list of current level's leaves' values to ans
            temp = []
            for node in level:
                temp.extend([node.left, node.right]) # list with all next level leaves (even null leaves)
            level = [leaf for leaf in temp if leaf] # list with non-null next level leaves
        return ans