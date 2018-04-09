package main

import (
	"fmt"
)

func main() {
	words := []string{"gin", "zen", "gig", "msg"}
	var l int
	l = preorderTraversal()
	fmt.Println(l)
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
		traversal(root.Right, gitresult)
	}
}

func preorderTraversal(root *TreeNode) []int {
	var result []int
	return result
}