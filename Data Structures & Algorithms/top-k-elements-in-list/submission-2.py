# T:O(n) S:O(n)
#BucketSort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create list of lists of size len(nums)
        buckets = [[] for i in range(len(nums)+1)] 

        count = defaultdict(int)
        for item in nums:
            count[item] += 1

        for key,value in count.items():
            buckets[value].append(key)
        
        result =[]
        #loop each item of bucket from last until result is of size k
        for i in range(len(buckets)-1, 0, -1):
            for item in buckets[i]:
                result.append(item)
                if len(result) == k:
                    return result