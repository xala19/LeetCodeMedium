

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_data(self):
        return self.val
    
    def get_next(self):
        return self.next
    
    def set_data(self,val):
        self.val = val
    
    def set_next(self,next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = ListNode(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next()  != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
    
    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output)
    
    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node != None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev


class Solution(object):
    def get_number(self, linked_list):
        cur_node = linked_list.head
        result_number = 0
        while cur_node is not None:
            result_number = result_number * 10 + cur_node.get_data()
            cur_node = cur_node.get_next()
        return result_number

    def addTwoNumbers(self, l1, l2):
        first_num = self.get_number(l1)
        second_num = self.get_number(l2)
        sum_num = first_num + second_num
        reversed_sum = str(sum_num)[::-1]
        str_number = str(reversed_sum)
        
        # Создание нового связанного списка
        result_list = LinkedList()
        current = result_list.head = ListNode(int(str_number[0]))

        # Добавление остальных узлов
        for digit in str_number[1:]:
            current.next = ListNode(int(digit))
            current = current.next

        return result_list




def main():
    my_list = LinkedList()

    my_list.append(2)
    my_list.append(4)
    my_list.append(3)
    # my_list.show()
    second_list = LinkedList()
    second_list.append(5)
    second_list.append(6)
    second_list.append(4)
    my_list.reverse()
    second_list.reverse()
    res = Solution()
    result_solution = res.addTwoNumbers(my_list, second_list)
    result_solution.show()
   

    
if __name__ == '__main__':
    main()
    