package main

func findLHS(nums []int) int {
	output := 0
	nums_set := make(map[int]int)
	for _, num := range nums {
		if _, exist := nums_set[num]; !exist {
			nums_set[num] = 0
		}
		nums_set[num]++
	}

	for k, count := range nums_set {
		if count2, exist := nums_set[k+1]; exist {
			output = max(output, count+count2)
		}
	}
	return output
}
