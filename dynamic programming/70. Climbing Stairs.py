class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # brute force
        # if n == 0 or n == 1:
        #     return 1
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        # dynamic programming
        # total = 0
        # a = 0
        # b = 1
        # for i in range(n):
        #     x = a + b
        #     print(x)
        #     b = a
        #     a = x

        #     if i == n - 1 or i == n - 2:
        #         total += x
        
        # return total

        # final
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
