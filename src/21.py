# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(None);
        cur_point = result;
        while True:
            if l1 == None:
                cur_point.next = l2
                return result.next
            if l2 == None:
                cur_point.next = l1
                return result.next
            if l1.val < l2.val:
                cur_point.next = ListNode(l1.val)
                cur_point = cur_point.next
                l1 = l1.next
            else:
                cur_point.next = ListNode(l2.val)
                cur_point = cur_point.next
                l2 = l2.next