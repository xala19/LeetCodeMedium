class Solution:
    def romanToInt(self, s: str) -> int:
             rom_dic = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
             }
    
             total = 0
             prev_value = 0
             for num in reversed(s):
                  value = rom_dic[num]
                  if value < prev_value:
                     total  -= value
                  else:
                       total += value
                  prev_value = value
             return total  
                  
                
                      
                      



def main():
    solution_instance = Solution()
    result = solution_instance.romanToInt(s='IIIVI')
    print(result)


if __name__ == '__main__':
    main()
    