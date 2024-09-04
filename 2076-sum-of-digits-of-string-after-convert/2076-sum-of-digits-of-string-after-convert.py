class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ''
        for i in s:
            
            x = str(ord(i) - 96)
            ans = ans + x
        print(ans)

        
        for i in range(k):
            sol = 0
            for j in ans:
                
                sol +=int(j)

            ans = str(sol)
            print(ans)

        return int(ans)