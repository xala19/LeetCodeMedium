class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    print(False)
                    return False
            else:
                print(False)
                return False

        print(not stack)
        return not stack
                
        """
        :type s: str
        :rtype: bool
        """

def main():
    solution_instance = Solution()
    solution_instance.isValid('{[]}')


if __name__ == '__main__':
    main()
    