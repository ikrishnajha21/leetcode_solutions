class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if target == nums[x] + nums[y]:
                 return[x,y]
        return target        

        