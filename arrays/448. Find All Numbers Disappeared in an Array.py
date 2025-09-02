class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        newList = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                newList.append(i)

        return newList
