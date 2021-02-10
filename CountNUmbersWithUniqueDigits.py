'''
357. Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
 

Constraints:

0 <= n <= 8
'''

'''
Solution: recursion
'''


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #Edge Case n == 0
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            s = 9
            for i in range(2, n+1):
                s *= (11 - i)
            return s + self.countNumbersWithUniqueDigits(n-1)

'''
Solution: DP 可先储存
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            dp = [0] * 9
            dp[0] = 10
            dp[1] = 9
            result = 10
            for i in range(2, n+1):
                dp[i] = dp[i-1] * (11-i)
                result += dp[i]
            return result