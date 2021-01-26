'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
Sp;ution 1 

Similar to 3 sum, 3 个 for loop，但time exceeding limit,brute force O(N^4)
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        answer = []
        for first in range(n - 3):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            for second  in range(first+1, n - 2):
                if second > (first+1) and nums[second - 1] == nums[second]:
                    continue                
                for third in range(second + 1, n - 1):
                    fourth = n - 1
                    s = nums[third]+nums[second]+nums[first]
                    if third > (second + 1) and nums[third] == nums[third - 1]:
                            continue
                    while (fourth > third) and ((s + nums[fourth]) >= target):
                        if s + nums[fourth] == target:
                            # print(first, second,third, fourth)
                            answer.append([nums[first],nums[second],nums[third], nums[fourth]])
                            break
                        fourth -= 1
        return answer



'''
Sp;ution 2 双指针

虽然两种Solution 都是
Time Complexity O(N^3),但第二种明显更快
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        answer = []
        for first in range(n - 3):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            for second  in range(first+1, n - 2):
                if second > (first+1) and nums[second - 1] == nums[second]:
                    continue
                third = second + 1
                fourth = n - 1
                s = nums[first] + nums[second]
                while third < fourth:
                    if s + nums[third]+nums[fourth] > target:
                        fourth -= 1
                    elif s + nums[third]+nums[fourth] < target:
                        third += 1
                    else:
                        answer.append([nums[first],nums[second],nums[third], nums[fourth]])
                        # 下面连个comparison的顺序很重要，先确定range，再比较Value，这个部分为去重
                        while third < fourth and nums[third] == nums[third+1]:
                            
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth-1]:
                            fourth -=1
                         #对于等于Target的，进行缩进
                        third += 1
                        fourth -= 1
        return answer