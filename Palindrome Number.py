'''
9. Palindrome Number 回文题
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
‘’‘

’‘’
Solution

题目Easy，一次过，分一个Negative case
Time Complexity O(N)
Space Complexity O(N)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge Case
        if x < 0:
            return False
        num = str(x)
        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i+=1
            j-=1
        return True