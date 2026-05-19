class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = collections.Counter(nums)
        dic = dict(sorted(ans.items(), key = lambda item: item[1], reverse= True))
        res = list(dic)
        return res[:k]