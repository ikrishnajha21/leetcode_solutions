class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for num in reversed(nums):
            while num > 0:
                ans.append(num %10)
                num //= 10
            
        return ans[::-1]
        