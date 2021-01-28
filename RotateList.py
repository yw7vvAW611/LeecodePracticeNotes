'''
61. rotate list

Given the head of a linked list, rotate the list to the right by k places.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

'''
Solution 1: Brute Force
Rotate by 1 everytime, and repeat the step k times

Time Complexity O(N^2)
'''

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode: 
        if head == None:
            return None
        if head.next == None:
            return head
        for i in range(k):
            head = roateByOne(head)
        return head
    
def roateByOne(head):
    dummy = ListNode()
    dummy.next = head
    q = p = dummy
    q = q.next
    while q.next != None:
        q = q.next
        p = p.next
    q.next = head
    p.next = None
    return q


'''
Solution: 
double pointer


Time Complexity: O(N)
Space Complexity:O(1)
'''


   class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode: 
        #sepcial case [] or one element
        if head == None:
            return None
        if head.next == None:
            return head
        count = 1
        dummy = head
        while dummy.next != None:
            count +=1
            dummy = dummy.next
        k = k % count
        #Special case, mod == 0,则不变
        if k == 0:
            return head
        dummy = ListNode()
        dummy.next = head
        p = q = dummy
        for i in range(count - k):
            p = p.next
            q = q.next
        q = q.next
        dummy.next = q
        while q.next != None:
            q = q.next
        q.next = head
        p.next = None
        return dummy.next