class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLCA(root, n1, n2):

    if root is None:
        return None

    if (n1 > root.key and n2 > root.key):
        return findLCA(root.right, n1, n2)

    if (n1 < root.key and n2 < root.key):
        return findLCA(root.left, n1, n2)

    return root.key



#           4
#         /   \
#        3      6
#       / \    / \
#      1   2  5   7

root = Node(4)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1) 
root.left.right = Node(2) 
root.right.left = Node(5) 
root.right.right = Node(7)


print ("LCA(4, 5) = %d" %findLCA(root, 4, 5))
print ("LCA(1, 2) = %d" %findLCA(root, 1, 2))
print ("LCA(3, 2) = %d" %findLCA(root, 3, 2))
print ("LCA(5, 7) = %d" %findLCA(root, 5, 7))
