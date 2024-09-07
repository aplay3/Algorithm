# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(head,root):
            if not head:
                return True
            if not root or head.val != root.val:
                return False
            return check(head.next,root.left) or check(head.next,root.right)
        if not root:
            return False
        if check(head,root):
            return True
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)