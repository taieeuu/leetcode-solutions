/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	cur := head
	var prev *ListNode

	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
}

func printLinkList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, " -> ")
		head = head.Next
	}
	fmt.Println("nil")
}

func main() {
	head := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
	fmt.Println("orgin LinkList:")
	printLinkList(head)

	res := reverseList(head)
	fmt.Println("reverse LinkList:")
	printLinkList(res)
}
