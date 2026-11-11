class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = {}

        for i in s:
            s_counts[i] = s_counts.get(i,0) + 1

        for i in t:
            if i in s_counts:
                s_counts[i] -= 1
                if s_counts[i] == 0:
                    del s_counts[i]
            else:
                return False

        return len(s_counts) == 0
            
        