from math import ceil
class Solution(object):
    def removeElement(self, nums, val):
        array = []
        for i in nums:
            if i != val:
                array.append(i)
        return(array)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        


def main():
    solution_instance = Solution()
    solution_instance.removeElement(nums = [3,2,2,3], val = 3)


if __name__ == '__main__':
    main()
    