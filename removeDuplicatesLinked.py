
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        if self.next is not None:
            return f"{self.val} -> {self.next}"
        else:
            return str(self.val)

class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        while temp != None and temp.next != None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
                continue
            temp = temp.next
        return (head)
    
if __name__ == '__main__':
    # Создаем узлы
    linked_list = ListNode(1)
    first = ListNode(1)
    second = ListNode(2)
    
    # Связываем узлы
    linked_list.next = first
    first.next = second

    # Выводим связанный список

    # # Создаем экземпляр Solution и вызываем метод deleteDuplicates
    get_solution = Solution()
    get_solution.deleteDuplicates(linked_list)


    
    

