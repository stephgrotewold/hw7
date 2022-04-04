class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return 1


def perfect(root, d, level=0):

    if (root is None):
        return True

    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return 1


root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

if (perfect(root, calculateDepth(root))):
    print("Este es un arbol binario perfecto")
else:
    print("Este NO es un arbol binario perfecto")