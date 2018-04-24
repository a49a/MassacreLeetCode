class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        temp = num
        while temp > 0:
            temp = temp >> 1
            mask = mask << 1
        return num ^ (mask - 1)
