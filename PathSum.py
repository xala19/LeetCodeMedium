class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root.left is None and root.right is None:
            return root.val == targetSum  # Возвращаем 0, если узел пуст
        print(root.val)
        left_sum = self.hasPathSum(root.left,targetSum - root.val)
        right_sum = self.hasPathSum(root.right,targetSum - root.val)  
      # if result_left == targetSum:
        #     return result_left
        # elif result_right == targetSum:
        #     return result_right
        return left_sum or right_sum
        

def main():
    solution = Solution()
    so

if __name__ == '__main__':
    main()