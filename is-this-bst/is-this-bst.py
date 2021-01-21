def check_binary_search_tree_(root):
    return checkBST(root, -1, 10001)

def checkBST(root, Min, Max):
    if not root:
        return True
    if root.data <= Min or root.data >= Max:
        return False
    return checkBST(root.left, Min, root.data) and checkBST(root.right, root.data, Max)
