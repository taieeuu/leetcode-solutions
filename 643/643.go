package main

func findMaxAverage(nums []int, k int) float64 {
	window_sum := 0
	for _, num := range nums[:k] {
		window_sum += num
	}
	max_sum := window_sum
	for i := k; i < len(nums); i++ {
		window_sum += nums[i] - nums[i-k]
		max_sum = max(max_sum, window_sum)
	}
	return float64(max_sum) / float64(k)
}
