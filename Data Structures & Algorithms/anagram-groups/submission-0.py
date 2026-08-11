# T:O(m*nlogn) S:O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            sort_n = "".join(sorted(item))
            if sort_n in dict:
                dict[sort_n].append(item)
            else:
                dict[sort_n] = [item]
        result = []
        for item in dict.values():
            result.append(item)

        return result
        