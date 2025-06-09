package main

func sortColors(nums []int) {
	i, cur, j := 0, 0, len(nums)-1
	for cur < j {
		if nums[cur] == 0 {
			nums[cur], nums[i] = nums[i], nums[cur]
			cur++
			i++
		} else if nums[cur] == 2 {
			nums[j], nums[i] = nums[i], nums[j]
			j--
		} else if nums[cur] == 1 {
			i++
			cur++
		}
	}
}
