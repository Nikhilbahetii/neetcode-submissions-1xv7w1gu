class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            ans = 1
            for i in range(len(s)):
                x = set()
                count = 0
                for j in range(i, len(s)):
                    y = s[j]
                    if y not in x:
                        x.add(y)
                        count += 1
                        ans = max(ans, count)
                    else:
                        break
            return ans


