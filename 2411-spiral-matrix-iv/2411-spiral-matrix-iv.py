# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr = head
        row = 0
        col = 0
        d_p = 0
        x= [[-1 for col in range(n)]for row in range(m)]
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        while curr:
            x[row][col] = curr.val
            curr = curr.next
            next_r,next_c = row+d[d_p%4][0],col+d[d_p%4][1]
            if 0<=next_r<m and 0<=next_c<n and x[next_r][next_c]==-1:
                row,col=next_r,next_c
            else:
                d_p+=1
                row,col = row+d[d_p%4][0],col+d[d_p%4][1]
        return x



        