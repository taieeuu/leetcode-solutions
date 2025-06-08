package main

import "fmt"

func maxProfit(prices []int) int {
	minPrice := 10001
	profit := 0

	for _, price := range prices {
		minPrice = min(minPrice, price)
		profit = max(profit, price-minPrice)
	}
	return profit
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
