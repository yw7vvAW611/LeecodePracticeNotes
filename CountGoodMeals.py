'''
Leecode 1711. Count Good Meals

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.




Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.


Constraints:

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 20

'''


'''
Solution 1: brute force
Time complexity O(N^2)
Exceeds the time limit
'''
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        for i in range(len(deliciousness)):
            for j in range(j+1, len(deliciousness)):
                tem = math.log2((i+j))
                if tem - math.floor(tem) == 0:
                    count+=1
        return count


'''
Solution 2: (Similar to two sum) HashtTable
Time Complexity O(N)
Space Complexity O(N)


The main idea is that the number of powers of 2 is at most 21, so this turns the problem to a classic find the number 
of pairs that sum to a certain value but for 21 values. 


Key point 1:
Why the range i from 0 to 21 instead of 20 (The constraint for the input number is 0 <= deliciousness[i] <= 20
It is because the largest number is 2^20, 2^20 + 2^20 = 2^21

Key point 2: 
Why do we need to module 10^9+7?
- It is just large enough to fit in an int data type 
- It should be a prime number


'''

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        dic = {}
        for i in deliciousness:
            for j in range(0,22):
                comp = 2 ** j - i
                if comp in dic:
                    count += dic[comp]
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return count%(10**9+7)