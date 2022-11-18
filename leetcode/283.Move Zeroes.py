# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nz = []
        for i in range(l):
            if nums[i]!=0:
                nz.append(nums[i])
                
        nums[:] = nz + [0]*(l-len(nz))
        # nums = nz + [0]*(l-len(nz)) #not works
        # print(nums)
        
        
