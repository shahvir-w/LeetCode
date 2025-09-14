class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currentTotal = 0

        for num in nums:
            if num > currentTotal and currentTotal <= 0:
                currentTotal = num
            else:
                currentTotal += num
            maximum = max(maximum, currentTotal)

        return maximum
