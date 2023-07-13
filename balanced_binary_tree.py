# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node==None:
                return 0
            
            l=f(node.left)
            r=f(node.right)
            if l==-1:
                return -1
            elif r==-1:
                return -1
            elif abs(l-r)>1:
                return False
            else:
                return max(l,r)
            
            
        if f(root)!=-1:
            return True
        else:
            return False
s=Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.isBalanced(root))