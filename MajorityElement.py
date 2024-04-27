class Solution(object):
    def majorityElement(self, nums):
        candidate = 1
        counter = 0

        for element in range(len(nums)):
            if counter == 0:
                candidate = nums[element]
            if nums[element] == candidate: 
                counter += 1
            else:
                counter -= 1
        return candidate
      
        
        
        


def main():
    solution_instance = Solution()
    res = solution_instance.majorityElement(nums = [ 1, 1, 1, 1, 2, 3, 4 ])
    print(res)

if __name__ == '__main__':
    main()