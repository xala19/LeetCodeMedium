class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        array = []
        flag = False
        min_len = min(len(s) for s in strs)  # Находим минимальную длину строки
        for j in range(min_len):
            for i in range(len(strs) - 1):
                if strs[i][j] == strs[i + 1][j]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                array.append(strs[0][j])
            else:
                break

        result = ''.join(array)
        return result
        
def main():
    solution_instance = Solution()
    result = solution_instance.longestCommonPrefix(strs=["flower", "flow", "flight"])

if __name__ == '__main__':
    main()
