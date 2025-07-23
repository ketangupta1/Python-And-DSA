'''Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        subsets = 1<<n
        for num in range(0,subsets):
            temp_list = []
            for i in range(0,n):
                if num & 1<<i:
                    temp_list.append(nums[i])
            ans.append(temp_list)
        return ans

