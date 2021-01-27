'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


'''

'''
知识补充：
ListNode Pass by value or P

'''

'''
Solution: Brute Force

- 找到列表长度
- 删除从列表开头起的（L-n+1）个节点

Time Complexity O(N) (O(2N)-O(N))
but we iterate the list twice
Space Complexity O(1)

Key Dummy Node
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        count = 1
        cur = head
        while cur.next != None:
            count += 1
            cur = cur.next
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        for i in range(count - n):
            cur = cur.next
        cur.next= cur.next.next
        return dummy.next

'''
Solution 2

Follow up: Could you do this in one pass?

快慢指针
利用快慢指针的差，找出节点
第一个先走n步，然后两个指针一起走直到全部走完

Time Complexity：O（n）
Space Complexity：O（1）

Test Case：
1. 中间节点
2. 删去第一个或最后一个
'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        dummy = ListNode()
        dummy.next = head
        cur1 = dummy
        cur2 = dummy
        for i in range(n):
            cur1 = cur1.next
        while cur1.next != None:
            cur1 = cur1.next
            cur2 = cur2.next
        cur2.next= cur2.next.next
        return dummy.next