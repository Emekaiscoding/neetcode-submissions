class Solution:
    def topKFrequent(self, nums:list[int], k: int) ->list[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
         
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
            
        result = []
        
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                
                if len(result) == k:
                    return result
         
s = Solution()
s.topKFrequent(nums = [1,2,2,3,3,3], k = 3)