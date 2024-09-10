# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        while ans.next:
            
            

            x = ListNode()
            x.val = math.gcd(ans.val , ans.next.val)
            x.next = ans.next
            
            ans.next = x
            ans = ans.next.next
           


           
        return head