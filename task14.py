# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def judge(current_node):
            if not current_node:
                return False
            left = judge(current_node.left)
            right = judge(current_node.right)
            mid = current_node == p or current_node == q
            if mid + right + left >= 2:
                self.result = current_node
            return mid or left or right

        judge(root)
        return self.result
