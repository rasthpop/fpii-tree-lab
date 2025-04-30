# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        cur_node = root
        prev_node = None

        while cur_node and cur_node.val != key:
            prev_node = cur_node
            if key < cur_node.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        if cur_node is None:
            return root

        if cur_node.left is None and cur_node.right is None:
            if prev_node is None:
                return None
            if prev_node.left == cur_node:
                prev_node.left = None
            else:
                prev_node.right = None

        elif cur_node.right is None:
            if prev_node is None:
                return cur_node.left
            if prev_node.left == cur_node:
                prev_node.left = cur_node.left
            else:
                prev_node.right = cur_node.left

        elif cur_node.left is None:
            if prev_node is None:
                return cur_node.right
            if prev_node.left == cur_node:
                prev_node.left = cur_node.right
            else:
                prev_node.right = cur_node.right

        else:
            succ = cur_node.right
            succ_parent = cur_node
            while succ.left:
                succ_parent = succ
                succ = succ.left

            cur_node.val = succ.val

            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

        return root