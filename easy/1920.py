class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
        ans = [0]*len(nums)
        for i in range(0, len(nums)):
            ans[i] = nums[nums[i]]

        return ans

        # initialize a list of all 0s using the syntax
        # [0]*val where val is the length of the list filled with 0s
        # then simply fill in the list using the indexing provided in the problem description: nums[nums[i]]
