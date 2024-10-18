class Solution:
    def maximumSwap(self, num: int) -> int:
        
        x  = str(num)
        n  = len(x)
        max_num = num

        for i in range(n):
            for j in range(i+1,n):
                num_list = list(x)
                num_list[i],num_list[j] = (num_list[j],num_list[i],)
                temp = int("".join(num_list))

                max_num = max(max_num,temp)

        return max_num
        
            