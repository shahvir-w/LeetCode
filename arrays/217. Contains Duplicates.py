class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #hashset
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            else:
               numsSet.add(num)
        return False

        # sorting
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False

        # brute force: 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if not (i == j) and nums[i] == nums[j]:
                    return True
            
        return False