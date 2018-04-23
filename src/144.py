# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.List = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traversal(root)
        return self.List
    def traversal(self, root):
        if root == None:
            return
        else:
            self.List.append(root.val)
            self.traversal(root.left)
            self.traversal(root.right)

solution = Solution()
print(solution.preorderTraversal(None))

    