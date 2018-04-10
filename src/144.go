package main

import (
	"fmt"
)

func main() {
	t := TreeNode{1, nil, nil}
	t.Left = &TreeNode{2, nil, nil}
	t.Right = &TreeNode{3, nil, nil}
	var r []int
	r = preorderTraversal(&t)
	fmt.Println(r)
}

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func traversal(root *TreeNode, result []int) {
	result = append(result, root.Val)
	if root.Left != nil {
		traversal(root.Left, result)
	}
	if root.Right != nil {
		traversal(root.Right, result)
	}
}

func preorderTraversal(root *TreeNode) []int {
	var result []int
	traversal(root, result)
	return result
}