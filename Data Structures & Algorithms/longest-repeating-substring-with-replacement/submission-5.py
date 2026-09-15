class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()
        l = 0
        max_l = 0 
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1 
                
                l += 1 
                
            max_l = max(max_l, r-l+1)
            
            
        return max_l

        