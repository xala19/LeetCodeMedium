class Solution(object):
    def maxProfit(self, prices):
        prices_copy = prices
        get_min = min(prices_copy)
        min_index = prices_copy.index(get_min)
        
        for i in range(0, len(prices_copy) - 1) :
            if min_index == len(prices_copy) - 1 or prices_copy.index(max(prices_copy)) < min_index:
                prices_copy.pop(min_index)
                get_min = min(prices_copy)
                min_index = prices_copy.index(get_min)

            



        prices_copy = prices_copy[min_index:]
        return max(prices_copy) - get_min

def main():
    solution_instance = Solution()
    result = solution_instance.maxProfit(prices=[3,2,6,5,0,3])
    print(result)

if __name__ == '__main__':
    main()
