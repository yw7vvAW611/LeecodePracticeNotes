'''
String to Integer

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
Solution 1

比较繁

Tip： 要多观察Edge Case
比如“+-42”
“” empty string
“ ” 或者只有space的String
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        l = []
        s = s.lstrip()
        if len(s) == 0:
            return 0
        result = 0
        for i in range(0, 10):
            tem = str(i)
            l.append(tem)
        if s[0] == "+" or s[0] == "-":
            result = process(s , l)
        elif s[0] in l:
            result = process2(s , l)
        else:
            result = 0
        return result

def process(s , l):
    r = ''
    for i in range(1,len(s)):
        if s[1] not in l:
            return 0
        if s[i] in l:
            r+=s[i]
        else:
            break
    if len(r) == 0:
        return 0
    number = int(r)
    if isBoundary(number):
        if s[0] == '+':
            return number
        else:
            return number * -1
    else:
        if s[0] == '+':
            return 2**31-1
        else:
            return -2**31

def process2(s , l):
    r = ''
    for i in range(0,len(s)):
        if s[i] in l:
            r+=s[i]
        else:
            break
    number = int(r)
    if isBoundary(number):
        return number
    else:
        return 2**31-1


def isBoundary(n):
    if n < -2**31 or n > 2**31  - 1:
        return False
    else:
        return True