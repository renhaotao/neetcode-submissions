class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        si, ti = 0, 0

        while ti < len(t) and si != len(s):
            if s[si] == t[ti]:
                si += 1

            ti += 1

        return si == len(s)
        #     return True
        # else:
        #     return False

        # def helper(si, ti):

        #     if ti == len(t) and si < len(s):
        #         return False

        #     if si == len(s):
        #         return True

        #     if s[si] == t[ti]:
        #         return helper(si+1, ti+1)
        #     else:
        #         return helper(si, ti+1)


        # return helper(0, 0)
        