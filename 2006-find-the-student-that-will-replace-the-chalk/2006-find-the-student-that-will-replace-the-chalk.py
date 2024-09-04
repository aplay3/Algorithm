class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        x = sum(chalk)
        next_k = k % x
        print(next_k)
        if next_k ==0:
            return 0
        else:
            for i in range(len(chalk)):
                next_k = next_k - chalk[i]
                if next_k <0:
                    return i
        
            