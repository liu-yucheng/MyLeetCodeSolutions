# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + \
            [root.val] + \
            self.inorderTraversal(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        inorderList = self.inorderTraversal(root)
        length = len(inorderList)
        if length <= 1:
            return True
        idx = 1
        while idx < length:
            if inorderList[idx - 1] >= inorderList[idx]:
                return False
            idx += 1
        return True
