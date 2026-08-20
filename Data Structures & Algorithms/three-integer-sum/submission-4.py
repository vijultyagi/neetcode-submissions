# T:O(n^2), S:O(1)
#Two-pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = 0-n
            l,r = i+1, len(nums)-1

            while l<r:
                sum = nums[l] + nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
            

                    