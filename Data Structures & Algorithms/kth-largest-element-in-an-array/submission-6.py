class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # heapify

        return heapq.nlargest(k, nums)[-1]


        # for i in range(len(nums) - k + 1):
        #     a = heapq.heappop(nums) # pop the smallest
        #     # print(a)

        # return a 