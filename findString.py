class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            
            result = haystack.index(needle)
            return(result)
        else:
            return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        


def main():
    solution_instance = Solution()
    solution_instance.strStr(haystack = "mississippi", needle = "issip")


if __name__ == '__main__':
    main()
    