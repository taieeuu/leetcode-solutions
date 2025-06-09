package main

func isValid(s string) bool {

	stack := []string{}

	pair := map[string]string{
		"}": "{",
		")": "(",
		"]": "[",
	}

	for _, c := range s {

		if open, exist := pair[c]; exist {
			if len(stack) < 0 || stack[:len(stack)-1] != open {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			// stack = append(s[c])
			stack = append(stack, open) // push
		}
	}
	return len(stack) == 0
}
func main() {

}
