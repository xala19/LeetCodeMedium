class Tree():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(tree):
    if tree is None:
        return 0  # Возвращаем 0, если узел пуст
    print(tree.val)
    left_sum = pre_order_traversal(tree.left)
    right_sum = pre_order_traversal(tree.right)
    result_left = (tree.val + left_sum)
    result_right = (tree.val + right_sum)
    if 
    print(result_left)
    return result



def create_tree():
    tree = Tree(1)
    tree.left = Tree(2)
    tree.right = Tree(3)
    tree.left.left = Tree(4)
    tree.right.right = Tree(5)
    return tree

def main():

    tree = create_tree()
    pre_order_traversal(tree)
    

    



if __name__ == "__main__":
    main()