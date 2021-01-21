'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



Solution:
此题一次通过，就是通过index 行数

Time Complexity O(n)
Space Complexity O(n)
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        for i in range(numRows):
            result.append([])
        i = 0
        rindex = 0
        flag = True
        while i < len(s):
            if flag:
                if rindex < numRows - 1:
                    result[rindex].append(s[i])
                    rindex +=1
                else:
                    flag = False
                    result[rindex].append(s[i])
                    rindex -= 1
            else:
                if rindex > 0:
                    result[rindex].append(s[i])  
                    rindex -=1
                else:
                    flag = True
                    result[rindex].append(s[i])
                    rindex +=1
            i+=1
        solution = ''
        for i in result:
            for j in i:
                solution += j
        return solution

        
