def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return 1
    elif root1 is None or root2 is None:
        return 0
    elif root1.data==root2.data:
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return 0