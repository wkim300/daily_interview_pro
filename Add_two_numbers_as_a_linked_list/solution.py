"""[summary]
Date: 2020/07/08
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    carry = 0
    res = ListNode(0)
    head = res
    while l1 or l2:
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        tot = n1 + n2 + carry
        carry = 0
        if tot > 9:
            tot %= 10
            carry = 1
        
        l1 = l1.next
        l2 = l2.next
        res.val = tot
        res.next = ListNode(carry) if l1 or l2 or carry > 0 else None
        res = res.next  
    return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val, end=" ")
  result = result.next
# 7 0 8