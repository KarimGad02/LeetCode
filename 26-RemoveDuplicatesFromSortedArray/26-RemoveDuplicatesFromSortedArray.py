# Last updated: 24/11/2025, 17:27:23
class Solution:
    def removeDuplicates(self, nums):
        l=0
        r=1
        k=0
        count = 0
        while r<len(nums):
            if nums[l]==nums[r]:
                nums[r]='_'
                r+=1
            elif nums[l]!=nums[r]:
                l=r
                r+=1
        for i in range(len(nums)):
            if nums[i] != '_':
                nums[count] = nums[i]
                k+=1
                count += 1
        while count < len(nums):
            nums[count] = '_'
            count += 1
    
        return k