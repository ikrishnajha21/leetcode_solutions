class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,nums in enumerate( nums):
            digit_sum = sum(int(digit) for digit in str(abs(nums)))
            if digit_sum == i:
                return i
        return -1        

        