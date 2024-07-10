class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        x = []
        for i in logs:
            if i=="../":
                if len(x)!=0:
                    x.pop()
            elif i=="./":
                continue
            else:
                x.append(i)
        print()
        return len(x); 