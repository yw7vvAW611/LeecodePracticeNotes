'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


'''
Solution 1

Time Complexity : O(m+n)
Space Complexity: O(1)

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for i in range(m):
            n = len(matrix[i])
            if target > matrix[i][n-1]:
                continue
            else:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                return False
        return False


 '''
Solution 2
Binary Search

Time Complexity O(log(M*N)) = O(Log(M)+Log(N))
 '''


 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n-1
        #// floor division operator
        while left <= right:
            mid = (right + left)//2
            row = mid //n
            col = mid % n 
            # print(mid,"mid")
            # print(matrix[row][col])
            # print(left,right)
            if target < matrix[row][col]:
                right = mid - 1
            elif target == matrix[row][col]:
                return True
            else:
                left = mid + 1
            # print(left,right,"after")
        return False