class Solution:
    def removeElements(nums:list, target:int)->int:
        v=0
        l = len(nums)
        i=0
        for i in range(l):
            if nums[i] != target:
                nums[v] = nums[i]
                v+=1
        return v
