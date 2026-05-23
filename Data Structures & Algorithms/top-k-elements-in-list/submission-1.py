class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for num in nums:
            ans[num] = 1 + ans.get(num, 0)

        arr = []
        for num, value in ans.items():
            arr.append([value, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res 
