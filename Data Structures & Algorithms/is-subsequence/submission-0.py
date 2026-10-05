class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        def helper(si, ti):

            if ti == len(t) and si < len(s):
                return False

            if si == len(s):
                return True

            if s[si] == t[ti]:
                return helper(si+1, ti+1)
            else:
                return helper(si, ti+1)


        return helper(0, 0)
        