'''
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

'''
需要考虑到Edge Case 比如Head 是None

审题，注意Constraint

Time Complexity O（N）
Space Complexity O（N）
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = q = head
        if head == None:
            return None
        p = p.next
        while p != None:
            while p!= None and p.val == q.val:
                p = p.next
            q.next = p
            q = q.next
        return head