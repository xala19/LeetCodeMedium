# Определение узла бинарного дерева
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Класс решения с методами для работы с деревом
class Solution(object):
    
    def __init__(self):
        self.root = None
    
    # Метод для вставки в корень или создания нового дерева
    def norm_insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert(self.root, value)

    # Метод рекурсивной вставки
    def insert(self, current, value):
        if value < current.val:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self.insert(current.left, value)  # Исправленная вставка в левое поддерево
        elif value > current.val:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self.insert(current.right, value)  # Исправленная вставка в правое поддерево
    
    # Метод обхода дерева в порядке симметрии
    def inorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            print(root.val, end=" ")  # Используем val вместо value
            self.inorderTraversal(root.right)

def main():
    # Создаем объект класса Solution
    tree = Solution()
    values = [7, 4, 9, 1, 6, 8, 10]

    # Вставляем значения в дерево
    for value in values:
        tree.norm_insert(value)

    # Обходим дерево в порядке симметрии
    print("In-order traversal:")
    tree.inorderTraversal(tree.root)  # Исправленный вызов метода

# Запускаем основную функцию
if __name__ == '__main__':
    main()
