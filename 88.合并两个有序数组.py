#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        a = m - 1
        b = n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1
# @lc code=end

