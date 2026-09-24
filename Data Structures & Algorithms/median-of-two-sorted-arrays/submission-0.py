class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        merged = []

        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                merged.append(nums1[n1])
                n1 += 1
            else:
                merged.append(nums2[n2])
                n2 += 1
        if n1 < len(nums1):
            merged.extend(nums1[n1:])

        if n2 < len(nums2):
            merged.extend(nums2[n2:])

        if len(merged) == 0:
            return 0

        if len(merged) == 1:
            return merged[0]

        if len(merged) % 2 == 0:
            m = len(merged) // 2
            n1, n2 = m - 1, m 
            return (merged[n1] + merged[n2]) / 2
        else:
            return merged[len(merged)//2]
        