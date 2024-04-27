class Solution(object):
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)
        for i in range(0,len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
                
        return False


def main():
    solution_instance = Solution()
    solution_instance.containsDuplicate(nums=[1,2,3,1])


if __name__ == '__main__':
    main() 