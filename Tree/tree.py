from collections import deque
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def create_tree_from_list(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        current_tree_node = queue.popleft()

        if arr[i] is not None:
            current_tree_node.left = TreeNode(arr[i])
            queue.append(current_tree_node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current_tree_node.right = TreeNode(arr[i])
            queue.append(current_tree_node.right)
        i += 1
    return root

tree_list = [3, 9, 20, None, None, 15, 7]
my_tree_root = create_tree_from_list(tree_list)
