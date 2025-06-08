package main

import (
	"container/heap"
	"fmt"
)

// Letter 表示堆中一個字母及其剩餘可用次數
type Letter struct {
	ch    byte
	count int
}

// MaxHeap 實作 container/heap.Interface，用於 Letter 的最大堆
type MaxHeap []Letter

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i].count > h[j].count }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(Letter)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// longestHappyString 回傳符合條件的最長快樂字串
func longestHappyString(a, b, c int) string {
	// 初始化最大堆，只加入 count > 0 的字母
	h := &MaxHeap{}
	heap.Init(h)
	if a > 0 {
		heap.Push(h, Letter{'a', a})
	}
	if b > 0 {
		heap.Push(h, Letter{'b', b})
	}
	if c > 0 {
		heap.Push(h, Letter{'c', c})
	}

	res := make([]byte, 0, a+b+c)

	for h.Len() > 0 {
		first := heap.Pop(h).(Letter)
		n := len(res)
		// 若尾端已連續兩個 first.ch，則不能再放
		if n >= 2 && res[n-1] == first.ch && res[n-2] == first.ch {
			if h.Len() == 0 {
				break // 無其他字母可插，結束
			}
			second := heap.Pop(h).(Letter)
			// 插入次頂字母
			res = append(res, second.ch)
			second.count--
			// 次頂用完就不推回
			if second.count > 0 {
				heap.Push(h, second)
			}
			// 把原本的 first 推回堆，待下次使用
			heap.Push(h, first)
		} else {
			// 可以安全插入 first
			res = append(res, first.ch)
			first.count--
			if first.count > 0 {
				heap.Push(h, first)
			}
		}
	}

	return string(res)
}

func main() {
	fmt.Println(longestHappyString(1, 1, 1)) // 可能輸出 "abc"
	fmt.Println(longestHappyString(7, 1, 0)) // 輸出 "aabaa"
	fmt.Println(longestHappyString(3, 3, 3)) // 可能輸出 "aabbccaabbcc"
}
