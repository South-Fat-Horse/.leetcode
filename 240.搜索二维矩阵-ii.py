#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
            
        raws = len(matrix)
        cols = len(matrix[0])

        raw = 0
        col = cols - 1 

        while 0 <= raw < raws and 0 <= col < cols:
            if matrix[raw][col] < target:
                raw += 1
            elif  matrix[raw][col] > target:
                col -= 1
            else:
                return True
        return False
# @lc code=end

