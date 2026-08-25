class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

s = Solution()
print(s.hasDuplicate([1,1,5,3,9,0]))
