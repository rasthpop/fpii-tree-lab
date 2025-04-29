class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

def pre_order(node):
    res = []
    if node is None:
        return res
    
    if node.data not in res:
        res.append(node.data)
        
    res += (pre_order(node.left))
    res += (pre_order(node.right))
    
    return res


def in_order(node):
    res = []
    if node is None:
        return res
 
    res += (in_order(node.left))
    
    res.append(node.data)
    
    res += (in_order(node.right))
    
    return res

def post_order(node):
    res = []
    if node is None:
        return res
    
    res += (post_order(node.left))
    res += (post_order(node.right))
    res.append(node.data)
        
    
    return res


tree = Node(5, Node(10, Node(2), Node(3)), Node("leaf"))
in_order(tree)
