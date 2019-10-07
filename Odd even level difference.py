def getLevelDiff(root):
    if root is None:
        return 0
    return root.data-getLevelDiff(root.left)-getLevelDiff(root.right)