class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Используем два указателя для изменения массива на месте
        slow_pointer = 0

        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]

        # slow_pointer теперь указывает на последний уникальный элемент
        unique_length = slow_pointer + 1

        return(unique_length)
        


if __name__ == '__main__':
    main()
    
