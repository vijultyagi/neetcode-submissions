# T:O(n), S:O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        product = 1
        
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                product *= n
        
        res = [0]*len(nums)
        if zeroCount >= 2:
            return res
        elif zeroCount == 1:
            for i,n in enumerate(nums):
                if n == 0:
                    res[i] = product
                else:
                    res[i] = 0
            return res
        else:
            for i,n in enumerate(nums):
                res[i] = int(product/n)
            return res


        