class Solution(object):

    def addTwoNumbers(self, l1, l2):
        current_l1 = l1.head
        current_l2 = l2.head
        result_list = LinkedList()
        while current_l1 != None or current_l2 != None :
            value_l1 = current_l1.get_data()
            value_l2 = current_l2.get_data()
            total_sum =  value_l1 + value_l2
            if current_l1:
                current_l1 = current_l1.get_next()
            if current_l2:
                current_l2 = current_l2.get_next()
            result_list.append(total_sum)
        
        return(result_list)
    

class Node(object):
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self,data):
        self.data = data
    
    def set_next(self,next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    

    def append(self,data):
        new_node = Node(data)
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
    # second_list.show()

    res = Solution()
    result_solution = res.addTwoNumbers(my_list, second_list)
    result_solution.show()
    

    
    # solution_instance = Solution()
    # solution_instance.strStr(haystack = "mississippi", needle = "issip")


if __name__ == '__main__':
    main()
    