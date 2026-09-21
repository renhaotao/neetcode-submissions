class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        max_seq_length = 0

        for a in ns:

            if a-1 not in ns:
                seq_length = 1
                
                cur = a 
                while cur+1 in ns:
                    seq_length += 1
                    cur = cur + 1

                max_seq_length = max(max_seq_length, seq_length)

        return max_seq_length
        