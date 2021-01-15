#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        lefts = 0
        for i, x in enumerate(nums):
            if lefts == s-lefts-x:
                return i
            lefts += x
        return -1
# @lc code=end

