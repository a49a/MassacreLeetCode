# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def __init__(self):
        self.min_depth = sys.maxsize
        self.max_depth = 0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        [_, isBalanced] = self.gen_depth(root, 0)
        return isBalanced
    def gen_depth(self, root, cur_depth):
        cur_depth += 1
        if root.left is None and root.right is None:
            return [cur_depth, True]
        left_depth = 0
        right_depth = 0
        if root.left is not None:
            [left_depth, isBalanced] = self.gen_depth(root.left, cur_depth)
        if root.right is not None:
            [right_depth, isBalanced] = self.gen_depth(root.right, cur_depth)
        if isBalanced is False:
            return [cur_depth, False]
        if abs(left_depth - right_depth) <= 1:
            return [cur_depth + max(left_depth, right_depth), True]
        else:
            return [cur_depth, False]