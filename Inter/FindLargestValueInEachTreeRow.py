# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Time: O(n)
# Space: O(n) - size of rowNums and rowNumsNodes (n/2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        
        if not root:
            return ans
        
        rowNumNodes = [root]
        
        while rowNumNodes:
            
            rowNums = []

            for node in rowNumNodes:
                rowNums.append(node.val)
            maxOfRow = max(rowNums)
            ans.append(maxOfRow)

            cutter = 0
            
            maxLen = len(rowNumNodes)
            
            for i in range(maxLen):
                if rowNumNodes[i].left:
                    rowNumNodes.append(rowNumNodes[i].left)
                if rowNumNodes[i].right:
                    rowNumNodes.append(rowNumNodes[i].right)
                cutter += 1

            rowNumNodes = rowNumNodes[cutter:]
         
        return ans