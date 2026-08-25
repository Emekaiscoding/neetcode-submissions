class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [3,4,5,6]
        # target = 7
        index = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
        return index

s = Solution()
s.twoSum([3,4,5,6], 7 )


        
                    
                
        