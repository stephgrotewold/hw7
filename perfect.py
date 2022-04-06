class newNode():

	def __init__(self, k):
		self.key = k
		self.right = self.left = None

def inorder(temp):

	if (not temp):
		return

	inorder(temp.left)
	print(temp.key,end = " ")
	inorder(temp.right)


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

def checker(root):
    if (perfect(root, calculateDepth(root))):
        print("\nThis is a perfect binary tree")
    else:
        print("\nThis is NOT a perfect binary tree")


def insert(temp,key):

	if not temp:
		root = newNode(key)
		return
	q = []
	q.append(temp)

	while (len(q)):
		temp = q[0]
		q.pop(0)

		if (not temp.left):
			temp.left = newNode(key)
			break
		else:
			q.append(temp.left)

		if (not temp.right):
			temp.right = newNode(key)
			break
		else:
			q.append(temp.right)
	
if __name__ == '__main__':
	root = newNode(11)
	root.left = newNode(8)
	root.left.left = newNode(7)
	root.right = newNode(14)
	root.right.left = newNode(13)
	root.right.right = newNode(20)

print("Tree before insertion:\n", end = " ")
inorder(root)

checker(root)
key = 9
insert(root, key)

print()
print("Tree after insertion:\n", end = " ")
inorder(root)

checker(root)

def deleteDeepest(root,d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
  

def deletion(root, key):
    if root == None :
        return None
    if root.left == None and root.right == None:
        if root.key == key :
            return None
        else :
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.key == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node :
        x = temp.key
        deleteDeepest(root,temp)
        key_node.key = x
    return root

print("\nThe tree before the deletion:")
inorder(root)
key = 14
root = deletion(root, key)
print()
print("\nThe tree after the deletion:")
inorder(root)