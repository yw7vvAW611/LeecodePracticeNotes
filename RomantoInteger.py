'''
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''



class Solution:

    #优化方法，因为 Roman numerals are usually written largest to smallest from left to right，所以如果前大后小的数，不用细分Case，直接相减即可
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        sum = 0
        while i < len(s):
            cur = s[i]
            if i < len(s) - 1:
                if cur == 'I' and s[i+1] == 'V':
                    sum += 4
                    i+=2
                elif cur == 'I' and s[i+1] == 'X':
                    sum += 9
                    i+=2
                elif cur == 'X' and s[i+1] == 'L':
                    sum += 40
                    i+=2
                elif cur == 'X' and s[i+1] == 'C':
                    sum += 90
                    i+=2
                elif cur == 'C' and s[i+1] == 'D':
                    sum += 400
                    i+=2
                elif cur == 'C' and s[i+1] == 'M':
                    sum += 900
                    i+=2
                else:
                    sum += dic[cur]
                    i+=1
            else:
                sum += dic[cur]
                i+=1
        return sum