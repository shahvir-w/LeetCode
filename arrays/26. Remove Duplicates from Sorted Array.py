class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0
        i = 0
        
        while i < len(nums):
            if nums.index(nums[i]) == i:
                k += 1
                i += 1
            else:
                nums.pop(i)

        return k
