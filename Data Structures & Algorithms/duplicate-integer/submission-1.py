class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for item in nums:
            if item in dict:
                return True
            else:
                dict[item] = item
        return False
        