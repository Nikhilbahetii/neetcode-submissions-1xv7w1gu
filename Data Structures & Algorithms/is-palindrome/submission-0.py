class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ""
        for x in s:
            if x.isalnum():
                ch += x.lower()
        n = len(ch)
        i = 0
        j = n-1
        while i < j:
            if ch[i] != ch[j]:
                return False
            i += 1
            j -= 1
        return True