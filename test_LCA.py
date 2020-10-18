import unittest
import LCA

class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        root = LCA.Node(4)
        root.left = LCA.Node(2)
        root.right = LCA.Node(6)
        root.left.left = LCA.Node(1) 
        root.left.right = LCA.Node(3) 
        root.right.left = LCA.Node(5) 
        root.right.right = LCA.Node(7)

        self.assertEqual(LCA.findLCA(root, 4, 5), 4, "LCA(4, 5) should be 4")
        self.assertEqual(LCA.findLCA(root, 1, 2), 2, "LCA(1, 2) should be 2")
        self.assertEqual(LCA.findLCA(root, 3, 2), 2, "LCA(3, 4) should be 2")
        self.assertEqual(LCA.findLCA(root, 5, 7), 6, "LCA(5, 7) should be 6")

        self.assertEqual(LCA.findLCA(root, 4, 8), None, "LCA(4, 5) should be None")
        self.assertEqual(LCA.findLCA(root, 8, 4), None, "LCA(8, 4) should be None")

if __name__ == '__main__':
    unittest.main()