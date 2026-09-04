class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq = [ [] for i in range(len(nums)+1)]

        for val, cnt in counts.items():
            freq[cnt].append(val)


        if k > len(counts.values()):
            k = len(counts.values())

        # print(counts)
        # print(freq)
        # print("len(counts.values()", len(counts.values()))
        # print("k", k)

        counter = len(freq) - 1
        # print("counter", counter)
        num_k_largest = 0
        return_list = []
        while num_k_largest < k and counter >= 0:
            # print(counter, freq[counter])
            if len(freq[counter]) != 0:
                num_k_largest += len(freq[counter])
                return_list = return_list + freq[counter]

            counter = counter - 1
            
        return return_list
