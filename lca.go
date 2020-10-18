package main

import "fmt"

type Node struct {
	val   int
	left  *Node
	right *Node
}

func find(root *Node, x int) bool {
	if root.val == x {
		return true
	} else if x < root.val && root.left != nil {
		return find(root.left, x)
	} else if x > root.val && root.right != nil {
		return find(root.right, x)
	}
	return false
}

func findLCA(root *Node, n1 int, n2 int) int {
	if !find(root, n1) || !find(root, n2) {
		return -1
	}

	if root == nil {
		return -1
	}

	if n1 > root.val && n2 > root.val {
		return findLCA(root.right, n1, n2)
	}

	if n1 < root.val && n2 < root.val {
		return findLCA(root.left, n1, n2)
	}

	return root.val
}

func main() {
	//            4
	//         /    \
	//        2      6
	//       / \    / \
	//      1   3  5   7

	root := Node{4, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{6, nil, nil}
	root.left.left = &Node{1, nil, nil}
	root.left.right = &Node{3, nil, nil}
	root.right.left = &Node{5, nil, nil}
	root.right.right = &Node{7, nil, nil}

	fmt.Println("LCA(4, 5) = ", findLCA(&root, 4, 5))
	fmt.Println("LCA(1, 2) = ", findLCA(&root, 1, 2))
	fmt.Println("LCA(3, 2) = ", findLCA(&root, 3, 2))
	fmt.Println("LCA(5, 7) = ", findLCA(&root, 5, 7))
}
