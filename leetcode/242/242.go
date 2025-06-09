package main

import "fmt"

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	sMap := map[rune]int{}
	for _, v := range s {
		sMap[v]++
	}
	for _, v := range t {
		sMap[v]--
		if sMap[v] < 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("aabb", "abab"))
}
