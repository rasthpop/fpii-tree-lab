class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.right = right
        self.left = left

def tree_by_levels(node):
    if node is None:
        return []

    res = [node.value]
    
    to_visit = []

    if node.left is not None:
        to_visit.append(node.left)

    if node.right is not None:
        to_visit.append(node.right)

    while to_visit:
        cur_node = to_visit.pop(0)
        res.append(cur_node.value)

        if cur_node.left is not None:
            to_visit.append(cur_node.left)

        if cur_node.right is not None:
            to_visit.append(cur_node.right)

    return res


tree = Node(5, Node(10, Node(2), Node(3, Node(4))), Node("leaf"))
tree_by_levels(tree)
