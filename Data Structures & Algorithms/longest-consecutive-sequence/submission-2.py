# T:O(nlogn) S:O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        res = l = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] == nums[i] + 1:
                l += 1
            else:
                l = 1
            res = max(res, l)
        return res
                
        