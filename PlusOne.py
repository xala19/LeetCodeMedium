class Solution(object):
    def plusOne(self, digits):
        get_num = "".join(map(str, digits))
        res = int(get_num) + 1
        array = []
        for i in str(res):
            array.append(int(i))

        return(array)
        


def main():
    solution_instance = Solution()
    solution_instance.plusOne(digits = [1,2,3])


if __name__ == '__main__':
    main()
    