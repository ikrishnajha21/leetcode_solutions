class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        insert_pos=0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
             nums[insert_pos], nums[i]=nums[i], nums[insert_pos]
             insert_pos += 1
        return nums

            

        