class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            b_index= half - m - 2

            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m + 1] if  (m + 1) < len(A) else float('inf')
            Bleft = B[b_index] if b_index >= 0 else float('-inf')
            Bright = B[b_index + 1] if (b_index + 1) < len(B) else float('inf')

            # found middle
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Bright, Aright))/ 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1
