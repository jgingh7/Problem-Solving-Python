# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #This is in preorder
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def build(node):
            if node:
                ans.append(str(node.val))
                build(node.left)
                build(node.right)
            else:
                ans.append('#')
            
        ans = []
        build(root)
        return ','.join(ans) # "1,2,#,#,3,4,#,#,5,#,#"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build():
            element = next(ans)
            if element == '#':
                return None
            node = TreeNode(int(element))
            node.left = build()
            node.right = build()
            return node
            
        ans = iter(data.split(',')) #makes an interative object of data split by ',' (split actually returns a list of Strings split by ',')
        return build()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))