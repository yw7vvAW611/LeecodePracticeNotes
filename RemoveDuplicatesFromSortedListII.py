'''
82 Remove Dupliavtes from sorted list
 
Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]

'''


'''
Solution:双指针

Time Complexity O(n)
Space Complexity O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = q = dummy
        p = p.next
        if p == None:
            return None
        if p.next == None:
            return head
        while p!= None and p.next!= None:
            if p.val == p.next.val:
                p = p.next
                while p.next != None and p.val == p.next.val:
                    p = p.next
                  # The most important step, 只连q.next，不用改q
                q.next = p.next
            else:
                q = p
            p = p.next
        return dummy.next



   '''
也可以 内外指针
   '''


 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        if cur.next == None or cur.next.next == None:
            return head
        while cur.next != None and cur.next.next != None:
            temp = cur.next
            if temp.next.val == temp.val:
                while temp != None and temp.next!= None and temp.next.val == temp.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
           
        return dummy.next
                
 # The second solution 更快，因为只在需要的时候两个pointer 一起iterate