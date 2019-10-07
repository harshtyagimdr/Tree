def size(node):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        l=size(node.left)
        r=size(node.right)
        return l+r+1