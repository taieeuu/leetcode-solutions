package main

import (
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	if len(intervals) <= 0 {
		return 0
	}
	sort.Slice(intervals, func(a, b int) bool {
		return intervals[a][1] < intervals[b][1]
	})

	c := 0
	prev := intervals[0]
	for i := 1; i < len(intervals); i++ {
		current := intervals[i]
		if current[0] < prev[1] {
			c++
		} else {
			prev = current
		}

	}
	return c
}
