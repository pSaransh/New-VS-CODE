from pip import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        k = len(s)
        numsL = list(s)
        numsL.sort()
        i=0
        for j in numsL:
            nums[i] = j
            i+=1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution();
k = s.removeDuplicates(nums)
print(nums[:k+1])