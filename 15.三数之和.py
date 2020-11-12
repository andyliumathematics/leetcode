# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (29.19%)
# Likes:    2666
# Dislikes: 0
# Total Accepted:    343.3K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for i ,numi in enumerate(nums):
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            for j ,numj in enumerate(nums):
                if(j<=i):
                    continue
                if(j!=0 and nums[j]==nums[j-1]):
                    continue
                for k,numk in enumerate(nums):
                    if(k<=j):
                        continue
                    if(k!=0 and nums[k]==nums[k-1]):
                        continue
                    if(numi+numj+numk == 0):
                        l.append([numi,numj,numk])
        return l

# @lc code=end

