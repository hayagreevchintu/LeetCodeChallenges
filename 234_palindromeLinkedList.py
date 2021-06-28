# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        linkedList = []
        while True:
            try:
                linkedList.append(head.val)
                head = head.next
            except:
                break
        return linkedList == linkedList[::-1]