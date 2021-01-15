#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        seq0, seq1 = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq1 += 1
            else:
                res += min(seq0, seq1)
                seq0 = seq1
                seq1 = 1
        res += min(seq0, seq1)
        return res  
# @lc code=end

