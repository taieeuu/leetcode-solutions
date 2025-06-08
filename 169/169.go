package main

func majorityElement(nums []int) int {
	idx, cnt := 0, 1
	for i := 1; i < len(nums); i++ {
		if nums[idx] == nums[i] {
			cnt++
		} else {
			cnt--
			if cnt == 0 {
				idx = i
				cnt = 1
			}
		}
	}
	return nums[idx]
}
