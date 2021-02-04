'''

96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19



Solution: Dynmaic Programming

Time  Complexity: O(N^2)
Spce Complexity: O(N)
'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        # dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2,n + 1):
            for j in range(i):
                dp[i] += (dp[j] * dp[i-j-1])
        # print(dp)
        return dp[n]





'''
95. Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
'''





'''
Solution: Recursion

Time Complexity: this is related to Catlan Number

O(nGn) = O(4n / n^(1/2))

Space Complexity 


O(nGn) = O(4n / n^(1/2))


'''

#https://leetcode.wang/leetCode-95-Unique-Binary-Search-TreesII.html


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return generate(1,n)


def generate(start, end):
    ans = []
    if start > end:
        ans.append(None)
        return ans
    if start == end:
        r = TreeNode(start)
        ans.append(r)
        return ans
    for i in range(start, end+1):
        leftTree = generate(start, i - 1)
        rightTree = generate(i + 1, end)
        for left in leftTree:
            for right in rightTree:
                root = TreeNode(i)
                root.left = left
                root.right = right
                ans.append(root)
    return ans