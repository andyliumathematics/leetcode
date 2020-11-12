#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (38.06%)
# Likes:    4775
# Dislikes: 0
# Total Accepted:    520.5K
# Total Submissions: 1.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 遍历的遍历器
        l1temp = l1
        l2temp = l2
        result = None
        iteratori = None
        i10 = 0
        while(l1temp!=None or l2temp!=None):
            if(l1temp==None):
                l1temp = ListNode(0)
            if(l2temp==None):
                l2temp = ListNode(0)

            if(iteratori == None):
                iteratori = ListNode(int((l1temp.val +l2temp.val +i10)%10))
                result = iteratori
            else:
                iteratori.next = ListNode(int((l1temp.val +l2temp.val +i10)%10))
                iteratori = iteratori.next
            i10 = int((l1temp.val+l2temp.val+i10)/10)
            l1temp= l1temp.next
            l2temp= l2temp.next
        if(i10>0):
            iteratori.next = ListNode(i10)
            
        return result

# @lc code=end
