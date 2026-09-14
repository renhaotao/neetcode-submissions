class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_L = 0
        existing = set()
        # print("existing", existing)

        for R in range(len(s)):
            while s[R] in existing:
                existing.remove(s[L])
                L += 1

            existing.add(s[R])
            max_L = max(max_L, R-L+1)
            # print(L, R, existing, max_L)

        return max_L