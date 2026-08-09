# T: O(s+t), S: O(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}
        
        for item in s:
            if item in dict_s:
                dict_s[item] += 1
            else:
                dict_s[item] = 1
        
        for item in t:
            if item in dict_t:
                dict_t[item] += 1
            else:
                dict_t[item] = 1
        
        for item in s:
            if item not in dict_t or dict_s[item] != dict_t[item]:
                return False
                
        return True        