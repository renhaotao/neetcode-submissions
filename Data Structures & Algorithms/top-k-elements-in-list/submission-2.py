class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            
        threshold = sorted(counts.values())[-k]
        return [i for i in counts.keys() if counts[i] >= threshold]