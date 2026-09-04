class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_alnum = [ch.lower() for ch in s if ch.isalnum()]
        
        is_pali_so_far = True

        s = s_alnum.copy()

        i = 0
        while is_pali_so_far and i < len(s):
            # print(i, s[i],s[len(s)-i-1], s[i]==s[len(s)-i-1])
            is_pali_so_far = s[i]==s[len(s)-i-1]
            i += 1 

        return is_pali_so_far
        