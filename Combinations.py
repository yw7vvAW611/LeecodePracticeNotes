'''
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''


'''
思路：
Backtracking is a general algorithm for finding all solutions to some computational problems, notably constraint
satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the
candidate cannot possibly be completed to a valid solution. 


Time Complexity O((n k)*k)
Space Complexity O(k)
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ##明显用回溯法:
        res = []

        def backtrace(curr_res,index):
            # print("curr_res:",curr_res)
            if len(curr_res)==k:
            	#most by deep copy because python pass by object reference
                res.append(curr_res[:]) ##浅拷贝，这一步很重要
                return 

            for i in range(index,n+1):
                curr_res.append(i)
                # print(curr_res, 'after append')
                backtrace(curr_res,i+1)
                # print(curr_res, 'before pop')
                curr_res.pop()
                # print(curr_res, 'after pop')

        # ##特殊情况处理 (d但constraint已经帮助排除)
        # if n==0 or k==0:
        #     return res

        backtrace([],1)
        return res

