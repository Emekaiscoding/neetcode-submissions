class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l, r = 0, len(i) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if i[m] < target:
                    l = m + 1
                elif i[m] > target :
                    r = m - 1
                else:
                    return True
        
        return False

s = Solution()
s.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)