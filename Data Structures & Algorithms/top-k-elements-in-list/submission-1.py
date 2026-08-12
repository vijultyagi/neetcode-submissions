# T:O(nlogn) S:O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for item in nums:
            count[item] += 1
        
        lst = []
        for key, value in count.items():
            lst.append([value, key])
        lst.sort()
        
        result = []
        for i in range(k):
            result.append(lst.pop()[1])
        return result
