package main

type MyStack struct {
	stack []int
}

func Constructor() MyStack {
	return MyStack{stack: []int{}}
}

func (this *MyStack) Push(x int) {
	this.stack = append(this.stack, x)
}

func (this *MyStack) Pop() int {
	// this.stack
}

func (this *MyStack) Top() int {

}

func (this *MyStack) Empty() bool {

}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
