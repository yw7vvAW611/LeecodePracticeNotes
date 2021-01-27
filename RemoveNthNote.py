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
ListNode Pass by value or Pass by reference

Python is pass by object reference
https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

Both the function and the caller refer to the same object in memory, 
so when the append function adds an extra item to the list, 
we see this in the caller too! They’re different names for the same thing; 
different boxes containing the same object. 
This is what is meant by passing the object references by value - the function and caller use the same object in memory,
 but accessed through different variables. 
 This means that the same object is being stored in multiple different boxes, 
and the metaphor kind of breaks down. Pretend it’s quantum or something.

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