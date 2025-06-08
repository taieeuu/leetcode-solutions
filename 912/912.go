package main

func sortArray(nums []int) []int {
	if len(nums) < 2 {
		return nums
	}
	mid := len(nums) / 2
	left := sortArray(nums[:mid])
	right := sortArray(nums[mid:])

	return merge(left, right)
}

func merge(left []int, right []int) []int {
	merged := []int{}
	p, q := 0, 0
	for p < len(left) && q < len(right) {
		if left[p] < right[q] {
			merged = append(merged, left[p])
			p++
		} else {
			merged = append(merged, right[q])
			q++
		}
	}
	merged = append(merged, left[p:]...)
	merged = append(merged, right[q:]...)

	return merged
}
