class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        current_num = 0
        longest = 0

        for num in num_set:
            if num-1 not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest



s = Solution()
s.longestConsecutive([2,20,4,10,3,4,5])           



        