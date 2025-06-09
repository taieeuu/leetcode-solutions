package main

import "fmt"

func containsDuplicate(nums []int) bool {
	numsMap := map[int]int{}

	for _, v := range nums {
		_, exist := numsMap[v]
		if exist {
			return true
		} else {
			numsMap[v] = 1
		}
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}

// func containsDuplicate(nums []int) bool {
// 	set := make(map[int]struct{})
// 	for _, num := range nums {
// 		if _, hasNum := set[num]; hasNum {
// 			return true
// 		}
// 		set[num] = struct{}{}
// 	}
// 	return false
// }
