# T:O(n), S:O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numdic = {}
        for i,n in enumerate(numbers):
            numdic[n] = i+1
        for i,n in enumerate(numbers):
            if target-n in numdic:
                return [i+1, numdic[target-n]]
                