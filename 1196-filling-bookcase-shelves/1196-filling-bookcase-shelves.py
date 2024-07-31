class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [-1] * (n +1)

        def solve(index,books,width,dp):
            x = len(books)

            if index>=x:
                return 0
            if dp[index] != -1:
                return dp[index]
            
            maxy, w, ans = 0,0,float('inf')
            for i in range(index,x):
                if(w + books[i][0]) > width:
                    break
                w +=books[i][0]
                maxy = max(maxy,books[i][1])
                ans = min(ans,maxy+solve(i+1,books,width,dp))

            dp[index] = ans
            return dp[index]

        return solve(0,books,shelfWidth,dp)
