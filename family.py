class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d


def perfect(root, d, level=0):

    if (root is None):
        return True

    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (perfect(root.left, d, level + 1) and
            perfect(root.right, d, level + 1))


root = None
root = newNode("Steph")
root.left = newNode("Jorge")
root.right = newNode("Susi")
root.left.left = newNode("Jorge")
root.left.right = newNode("Sara")
root.right.left = newNode("Coralia")
#root.right.right = newNode("Manuel")

if (perfect(root, calculateDepth(root))):
    print("Este es un arbol binario perfecto")
else:
    print("Este NO es un arbol binario perfecto")