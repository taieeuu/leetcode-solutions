package main

func decrypt(code []int, k int) []int {
	n := len(code)
	res := make([]int, n)

	if k == 0 {
		return res
	} else if k < 0 {
		p := -k
		window := 0

		for _, v := range code[n-p:] {
			window += v
		}
		res[0] = window

		for i := 1; i < n; i++ {
			window = window - code[(i-1-p+n)%n] + code[(i-1+n)%n]
			res[i] = window
		}
	} else {
		window := 0

		for _, v := range code[1 : k+1] {
			window += v
		}
		res[0] = window

		for i := 1; i < n; i++ {
			window = window - code[i] + code[(i+k)%n]
			res[i] = window
		}
	}
	return res
}
