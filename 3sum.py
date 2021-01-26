'''
15. 3sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
Solution 1: Brute Force
Time Complexity O(N^3)
Space Complexity O(1)
'''

'''
Solution 2 double pointer

Tip 不可用set，set不能add以list 为unit 的element
=============================================
Key：no duplicate triplet ==> solution: sort
=============================================
降低复杂度，变two sum

Special Case
1. Empty or less than 3
2. [0,0,0,0]

Time Complexity
- SortO(nlogn)
-find the answer O(n^3)

Space Complexity 
O(1)





==============
此写法还是O（N^3），一个Loop + two pointer 才是O（N(^2），思路详见4Sum
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)
        for first in range(n):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            target = -nums[first]
            third = n-1
            for second in range(first+1, n):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                while second < third and nums[second] + nums[third] > target :
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    answer.append([nums[first],nums[second],nums[third]])
        return answer 

'''
Solution 3 可用一个For loop + Two Pointer， Similar to four sum.
'''