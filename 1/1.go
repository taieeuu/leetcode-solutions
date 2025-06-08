package main

import "fmt"

func twoSum(nums []int, target int) []int {
	numsMap := map[int]int{}
	for indx, value := range nums {
		complement := target - value
		if complementIndx, exist := numsMap[complement]; exist {
			return []int{complementIndx, indx}
		}
		numsMap[value] = indx
	}
	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	result := twoSum(nums, target)
	fmt.Println(result)

}
