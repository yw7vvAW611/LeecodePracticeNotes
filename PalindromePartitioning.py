'''
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''


'''
Solution: Backtrack
Time Complexity O(2^n)
Space Complexity O(n)
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(lastStr, path):
        	#Path is different from res (Path 是存储Possible solution， res 是最后答案)
        	#Shallow Copy is important
        	#It is important to judge when to terminate the tree (当Iterate完整个String)
            if len(lastStr) == 0:
                res.append(path[:])
            for i in range(len(lastStr)):
                first = lastStr[:i+1]
                last = lastStr[i+1:]
                if isPalindrom(first):
                    path.append(first)
                    backtrack(last,path)
                    path.pop()

        def isPalindrom(s):
            i = 0
            j = len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        backtrack(s, [])
        return res