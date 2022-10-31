# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Given the root of a binary tree, invert the tree, and return its root.
# this means you take the  root  and invert the children
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #create our stop case
        if root == None:
            return None
        # temporary store root.left.value in a variable
        temp = root.left
        #then replace root.left with root.right
        root.left = root.right
        #then replace root.right with temp variable that has root.left value
        root.right = temp
        #we want to keep on doing this to the other subtrees by:
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        