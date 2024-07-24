class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        sol = []
        resol = []
        for num in nums:
            x = str(num)
            answer = []
            for i in x:
                y = mapping[int(i)]
                answer.append(str(y))
            example = ''.join(answer)
            sol.append(example)
        z = sorted(sol,key = lambda x : int(x))
        print(z)
        for s in z:
            re = []
            for i in str(s):
                x1 = mapping.index(int(i))
                re.append(str(x1))
            example = ''.join(re)
            resol.append(int(example))

        return resol