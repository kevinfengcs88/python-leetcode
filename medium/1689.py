class Solution:
    def minPartitions(self, n: str) -> int:
        # A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
        # Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
        nums = [int(character) for character in n]
        return max(nums)

        # this problem seems particularly difficult, especially when reading the entire LeetCode description
        # however, after just giving it a little thought, the complex definition of a deci-binary number means nothing in the context of this problem
        # simply check for the largest digit in the given string (there's a reason why it's a string input, and not an integer) and return it
        # in other words, if there is a 9 in the input number, then 9 deci-binary numbers are required to "add up" to that 9
        # the rest of the numbers will be accounted for in, at most, 9 numbers
