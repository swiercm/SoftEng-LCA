package main

import "testing"

func TestTableFindLCA(t *testing.T) {
	root := Node{4, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{6, nil, nil}
	root.left.left = &Node{1, nil, nil}
	root.left.right = &Node{3, nil, nil}
	root.right.left = &Node{5, nil, nil}
	root.right.right = &Node{7, nil, nil}

	var tests = []struct {
		input1   *Node
		input2   int
		input3   int
		expected int
	}{
		{&root, 4, 5, 4},
		{&root, 1, 2, 2},
		{&root, 3, 2, 2},
		{&root, 5, 7, 6},
		{&root, 4, 8, -1},
		{&root, 8, 4, -1},
	}

	for _, test := range tests {
		if output := findLCA(test.input1, test.input2, test.input3); output != test.expected {
			t.Error("Test Failed: ", test.input2, test.input3, "inputted,", test.expected, "expected, received:", output)
		}
	}
}
