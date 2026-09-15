class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        rst = True
        while i < j and rst:
            while not s[i].isalnum() and i<j:
                i += 1

            while not s[j].isalnum() and i<j:
                j -= 1

            rst = s[i].lower() == s[j].lower()

            i += 1
            j -= 1


        return rst

        

        