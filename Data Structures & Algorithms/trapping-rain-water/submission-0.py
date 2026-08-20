# T:O(n), S:O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0
        maxl, maxr, min_lr = [0]*l,[0]*l,[0]*l
        mx = mn = 0
        
        for i in range(1, len(height)):
            maxl[i] = max(maxl[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            maxr[i] = max(maxr[i+1], height[i+1])
        
        for i in range(len(height)):
            min_lr[i] = min(maxl[i], maxr[i])
        
        total = 0
        for i in range(len(height)):
            water = min_lr[i] - height[i]
            if water < 1:
                water = 0
            total += water
        
        return total

        