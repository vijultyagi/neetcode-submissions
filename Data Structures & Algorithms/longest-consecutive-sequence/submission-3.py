# T:O(n) S:O(n)
# find start of sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set = set(nums)

        res = 0

        for n in nums:
            if (n-1) not in nums_set:
                l = 1
                while n+l in nums_set:
                    l += 1
                res = max(res, l)
        return res
        


            


        