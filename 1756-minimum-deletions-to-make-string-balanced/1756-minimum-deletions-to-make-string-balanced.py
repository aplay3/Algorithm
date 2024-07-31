class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans,cnt = 0,0
        for c in s:
            if c =='a':
                ans = min(ans+1,cnt)
            else:
                cnt+=1
        return ans