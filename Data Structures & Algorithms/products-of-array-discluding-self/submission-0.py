import math
class Solution:

    def prefix(self, nums: List[int]):
        x = math.prod(nums)
        return x

    def suffix(self, nums: List[int]):
        y = math.prod(nums)
        return y
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for num in range(n):
            ans.append(self.prefix(nums[0:num])*self.suffix(nums[num+1:n]))
        return ans

    