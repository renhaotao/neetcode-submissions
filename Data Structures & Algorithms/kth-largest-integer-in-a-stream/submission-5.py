class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapq.heapify(self.h)

        # print(self.h)
        # print(len(self.h))

        n = len(self.h)

        for _ in range(n - self.k):
            heapq.heappop(self.h)
            # print(self.h)
            # print(len(self.h))
            # print()

        # print("kth largest is {}".format(self.h[0]))

    def add(self, val: int) -> int:
        print("trying to add {} to {}".format(val, self.h))
        if self.h:
            # if val > self.h[0]:
            heapq.heappush(self.h, val)
            while len(self.h) > self.k:
                _ = heapq.heappop(self.h)
        else:
            heapq.heappush(self.h, val)
        rst = self.h[0]

        return rst