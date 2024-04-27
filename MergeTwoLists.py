
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            current = list1.val
            print(current)



def main():
    solution_instance = Solution()
    solution_instance.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])


if __name__ == '__main__':
    main()