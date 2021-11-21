class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held, sold, reset = -math.inf, -math.inf, 0
        for price in prices:
            prev_sold = sold
            held = max(held, reset - price)
            sold = held + price
            reset = max(reset, prev_sold)
        return max(sold, reset)