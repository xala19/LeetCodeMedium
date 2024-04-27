class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return(0)
        if target in nums:
            return(nums.index(target))
        
        if target > nums[-1]:
            return(nums.index(nums[-1]) + 1)
        else:
            for i in range(len(nums) - 1):
                if (target < nums[i + 1] and target > nums[i]):
                    return(i + 1)
                    



def main():
    solution_instance = Solution()
    solution_instance.searchInsert(nums = [1,3,5,6], target = 7)


if __name__ == '__main__':
    main()
    