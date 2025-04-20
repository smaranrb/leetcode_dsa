# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root: self.inorder(root, l)
        return l #done

    def inorder(self, root, l):
        if root.left: self.inorder(root.left, l)
        l.append(root.val)
        if root.right: self.inorder(root.right, l)