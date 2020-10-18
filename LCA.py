class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def find(self, x):
        if self.key == x:
            return True
        elif x < self.key and self.left:
            return self.left.find(x)
        elif x > self.key and self.right:
            return self.right.find(x)
        return False


def findLCA(root, n1, n2):

    if  not root.find(n1) or not root.find(n2):
        return None

    if root is None:
        return None

    if (n1 > root.key and n2 > root.key):
        return findLCA(root.right, n1, n2)

    if (n1 < root.key and n2 < root.key):
        return findLCA(root.left, n1, n2)

    return root.key



#           4
#         /   \
#        2      6
#       / \    / \
#      1   3  5   7

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1) 
root.left.right = Node(3) 
root.right.left = Node(5) 
root.right.right = Node(7)

print ("LCA(4, 5) = %d" %findLCA(root, 4, 5))
print ("LCA(1, 2) = %d" %findLCA(root, 1, 2))
print ("LCA(3, 2) = %d" %findLCA(root, 3, 2))
print ("LCA(5, 7) = %d" %findLCA(root, 5, 7))
