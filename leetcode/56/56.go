package main

import "sort"

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][1]
	})
	prev := intervals[0]
	var output [][]int
	for i := 1; i < len(intervals); i++ {
		curr := intervals[i]
		if curr[0] <= prev[1] {
			if curr[1] > prev[1] {
				prev[1] = curr[1]
			}
		} else {
			output = append(output, prev)
			prev = curr
		}
	}
	output = append(output, prev)
	return output
}

func main() {

}
