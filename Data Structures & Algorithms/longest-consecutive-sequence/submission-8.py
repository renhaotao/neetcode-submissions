class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        max_seq_length = 0
        i = 0
        while i < len(nums):
            # print(i)
            a = nums[i]

            if a-1 in ns:
                pass
            else:
                seq_length = 1
                while a+1 in ns:
                    seq_length += 1
                    a = a + 1

                max_seq_length = max(max_seq_length, seq_length)

            i += 1

        return max_seq_length
        