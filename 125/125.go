package main

import (
	"fmt"
	"unicode"
)

func isPalindrome(s string) bool {
	var filtered []rune

	for _, ch := range s {
		if unicode.IsLetter(ch) || unicode.IsDigit(ch) {
			filtered = append(filtered, unicode.ToLower(ch))
		}
	}
	left, right := 0, len(filtered)-1

	for left < right {
		if filtered[left] != filtered[right] {
			return false
		}
		left++
		right--
	}

	return true
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("race a car"))
}
