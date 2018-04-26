# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.gen_depth(root, 0)
        return self.depth
    def gen_depth(self, root, cur_depth):
        if root is None:
            return
        cur_depth += 1
        if root.left is None and root.right is None and cur_depth > self.depth:
            self.depth = cur_depth
            return
        if root.left is not None:
            self.gen_depth(root.left, cur_depth)
        if root.right is not None:
            self.gen_depth(root.right, cur_depth)