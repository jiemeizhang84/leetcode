class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        imin = 0
        imax = m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            
            imax_left = -math.inf if i == 0 else nums1[i - 1]
            imin_right = math.inf if i == m else nums1[i]
            jmax_left = -math.inf if j == 0 else nums2[j - 1]
            jmin_right = math.inf if j == n else nums2[j]
            
            if imax_left <= jmin_right and jmax_left <= imin_right:
                if (m + n) % 2 == 0:
                    return (max(imax_left, jmax_left) + min(imin_right, jmin_right)) / 2.0
                else:
                    return max(imax_left, jmax_left)
            elif imax_left > jmin_right:
                imax = i - 1
            else:
                imin = i + 1