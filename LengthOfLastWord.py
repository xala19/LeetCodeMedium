class Solution(object):
    def lengthOfLastWord(self, s):
        array_of_worlds = s.split(' ')
        result_array = []
        for i in array_of_worlds:
            if i.isalpha():
                result_array.append(i)
        return(len(result_array[-1]))
      
        

def main():
    solution_instance = Solution()
    solution_instance.lengthOfLastWord(s='Hello World')


if __name__ == '__main__':
    main()
    