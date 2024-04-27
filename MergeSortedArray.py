class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:n]
        nums1[:m] = nums1[:m] + nums2[:n]
        nums1.sort()
        return(nums1)

    

def main():
    solution_instance = Solution()
    solution_instance.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

if __name__ == '__main__':
    main()
