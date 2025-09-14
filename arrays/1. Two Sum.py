class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # hash map method:
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashMap:
                return [i, hashMap[difference]]
            else:
                hashMap[num] = i
        