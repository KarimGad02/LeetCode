class Solution:
    def removeElement(self, nums, val):
        l=0
        r=len(nums)-1
        k=0
        if len(nums)==0:
            return 0
        else:
            while r!=l:
                if nums[l]==val:
                    nums[l], nums[r]=nums[r], nums[l]
                    r-=1
                else:
                    l+=1
            for i in nums:
                if i!=val:
                    k+=1
        return k