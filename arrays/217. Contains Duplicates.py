class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False

        # initial solution lol: 
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if not (i == j) and nums[i] == nums[j]:
        #             return True
            
        # return False