class Solution(object):
    def addBinary(self, a, b):
        # Преобразуем двоичные строки в целые числа
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Складываем числа
        result = int_a + int_b
        
        # Преобразуем результат обратно в двоичную строку
        binary_result = bin(result)[2:]  # [2:] удаляет префикс '0b'
        
        return(binary_result)

def main():
    solution_instance = Solution()
    result = solution_instance.addBinary(a="11", b="1")
    print(result)

if __name__ == '__main__':
    main()


def main():
    solution_instance = Solution()
    solution_instance.addBinary(a = "11", b = "1")


if __name__ == '__main__':
    main()