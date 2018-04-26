# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
    def invert(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        if root.left is not None:
            self.invert(root.left)
        if root.right is not None:
            self.invert(root.right)
