class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            y = "".join(sorted(x))
            if y in dic:
                dic[y].append(x)
            else:
                dic[y] = [x]
        ans = list(dic.values())
        return ans