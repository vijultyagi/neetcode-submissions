# T:O(n), S:O(n)
# WITHOUT division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        post = [1]*n
        product = 1 
        for i in range(n):
            product *= nums[i]
            pre[i] = product
        
        productx = 1
        for i in range(n-1, -1, -1):
            productx *= nums[i]
            post[i] = productx
        
        res = [1]*n
        for i in range(n):
            if i==0:
                res[i] = post[i+1]
            elif i==n-1:
                res[i] = pre[i-1]
            else:
                res[i] = pre[i-1] * post[i+1]
        return res
            
