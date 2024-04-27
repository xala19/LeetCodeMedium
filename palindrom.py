from math import ceil
class Solution(object):
    def isPalindrome(self, x):
        flag = False
        conv_str = str(x)
        if len(conv_str) == 2:
            if conv_str[0] == conv_str[1]:
                flag = True

        if len(conv_str) % 2 == 0:
            delitel = int(len(conv_str) / 2)
            first_part = conv_str[:delitel]
            second_part = conv_str[delitel:]
            reversed_second_part = second_part[::-1]
            if first_part == reversed_second_part:
                flag = True
        else:
            delitel = int(len(conv_str) / 2)
            first_part = conv_str[:(ceil(delitel) + 1)]
            second_part = conv_str[ceil(delitel):]
            reversed_second_part = second_part[::-1]
            if first_part == reversed_second_part:
                flag = True

        return(flag)      



def main():
    solution_instance = Solution()
    solution_instance.isPalindrome(x=1000000001)


if __name__ == '__main__':
    main()
    