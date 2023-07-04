# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level(root):
            l1=[]
            l=[]
            q=deque([(root)])
            while q:
                size =len(q)
                for i in range(size):
                    node=q.popleft()
                    if node:
                        l.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                l1.append(l)
                l=[]
            return l
        print(level(root))
