class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        k = m + n - 1
        i1, i2 = m-1, n-1

        while i1 >= 0 and i2 >=0:
            if nums1[i1] > nums2[i2]:
                nums1[k] = nums1[i1]
                nums1[i1] = 0
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                nums2[i2] = 0
                i2 -= 1
            k  -= 1

        if i1 == -1 and i2 == -1:
            pass
        elif i1 == -1:
            nums1[:n] = nums2[:n]
        # else:
        #     nums2[:m] = nums1[:m]
            
        return nums1
        