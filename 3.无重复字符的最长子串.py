# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.82%)
# Likes:    4568
# Dislikes: 0
# Total Accepted:    719.7K
# Total Submissions: 2M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 不重复的第一个字符
        firsti = 0
        lasti = 0
        m = {}
        maxlen = 0
        for i, c in enumerate(s):
            # 无重复数据
            if(m.get(c) == None or m.get(c) < firsti):
                m[c] = i
            # 重复数据
            else:
                if(maxlen < i-firsti):
                    maxlen = i - firsti
                firsti = m.get(c)+1
                m[c]=i

        if(maxlen < len(s)-firsti):
            maxlen = len(s) - firsti

        return maxlen

        # @lc code=end
# 1. 重复的情况
#a. 字典里的数据位置大于等于firsti
# lasti换到i上
# 计算这次长度 并与最大长度比较 判断是否给最大长度赋值
# firsti变到m[c]的位置
# m[c]的值换到i上
#
# 2. 没重复的情况
#a. 字典里没有数据
#b. 字典里的数据比firsti要小
# lasti换到i上
