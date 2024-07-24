class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        sorted_dic = sorted(dic.items(),reverse=True)
        result = []
        for i in sorted_dic:
            result.append(i[1])
        return result
