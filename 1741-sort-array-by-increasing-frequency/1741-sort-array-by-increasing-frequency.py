from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        print(freq)

        sort_num = sorted(nums, key=lambda x:(freq[x],-x))

        return sort_num
        
