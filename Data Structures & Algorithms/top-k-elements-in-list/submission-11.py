class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        # print(freq)

        cnt_list = [[] for _ in range(0, len(nums)+1)]

        for (j_key, j_val) in freq.items():
            # print(j_key, j_val, cnt_list[j_val])
            cnt_list[j_val].append(j_key)
            # print(cnt_list)

        # print(cnt_list)

        n_most_freq = 0
        j = len(cnt_list) - 1
        return_list = []
        while n_most_freq < k and j >=0:
            if len(cnt_list[j]) > 0:
                return_list = return_list + (cnt_list[j])
                n_most_freq += len(cnt_list[j])
            j -= 1



        return return_list

        