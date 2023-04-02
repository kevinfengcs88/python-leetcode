class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
        return nums + nums

        # the easiest way to append one list to another is to use the '+' operator
