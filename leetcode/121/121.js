/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let low = prices[0]
    let high = 0
    prices.forEach((price, indx) => {
      low = Math.min(low, price)
      high = Math.max(high, price-low)
    })
    return high
};
res = maxProfit([7, 1, 5, 3, 6, 4])
console.log(res)