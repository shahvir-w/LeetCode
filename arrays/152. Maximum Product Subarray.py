class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for num in nums:
            if num == 0:
                currMax, currMin = 1, 1
                continue
            
            tmp = currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num * tmp, num * currMin, num)
            res = max(currMax, res)
        return res
