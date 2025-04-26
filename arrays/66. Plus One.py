class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits) - 1, -1, -1):
            print(digits[i])
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits


        digits.insert(0, 1)
        return digits