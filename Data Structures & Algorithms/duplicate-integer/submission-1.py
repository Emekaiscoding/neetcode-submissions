class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num) 
                
        return False

s = Solution()
s.hasDuplicate([1, 2, 3, 3])
#s.hasDuplicate([1, 2, 3, 4])