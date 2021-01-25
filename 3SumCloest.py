'''

16 3Sum Cloest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

'''

'''
Solution
如果是Brute Force， Time Complexity O(N^3）

Two Pointer


复杂度分析

时间复杂度：O(N^2)O(N 
2
 )，其中 NN 是数组 \textit{nums}nums 的长度。我们首先需要 O(N \log N)O(NlogN) 的时间对数组进行排序，随后在枚举的过程中，使用一重循环 O(N)O(N) 枚举 aa，双指针 O(N)O(N) 枚举 bb 和 cc，故一共是 O(N^2)O(N 
2
 )。

空间复杂度：O(\log N)O(logN)。排序需要使用 O(\log N)O(logN) 的空间。然而我们修改了输入的数组 \textit{nums}nums，在实际情况下不一定允许，因此也可以看成使用了一个额外的数组存储了 \textit{nums}nums 的副本并进行排序，此时空间复杂度为 O(N)O(N)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


1. 先Sort
2.  固定 first。 two pointer --》 sum
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = target - (nums[0]+nums[1]+nums[n-1]) 
        for first in range(n - 2):
            t = target - nums[first]
            for second in range(first + 1, n - 1):
                third = n - 1
                d = t - nums[second]
                if second == third:
                    break
                while d < nums[third] and third > (second + 1):
                    third -= 1
                c1 = d - nums[third]
                if c1 == 0:
                    return target
                if third < n-1:
                    c2 = d - nums[third+1]
                    if min(abs(c1) , abs(c2)) < abs(diff):
                        if abs(c1) < abs(c2):
                            diff = c1
                        else:
                            diff = c2
                else:
                    if abs(c1) < abs(diff):
                        diff = c1
                # print(nums[first], nums[second], nums[third])
                # print(c1,diff)
        return target - diff