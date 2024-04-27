class Solution(object):
    def twoSum(self, nums, target):
        array = []
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j]== target:
                    array.append(i)
                    array.append(j)
                    break
        return(array)

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """



def main():
    solution_instance = Solution()
    solution_instance.twoSum(nums=[2,7,11,15],target=9)


if __name__ == '__main__':
    main()
    