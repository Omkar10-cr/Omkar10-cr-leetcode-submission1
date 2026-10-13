class Solution(object):
    def finalPrices(self, prices):
        answer = prices[:]
        stack = []  # indices waiting for their discount

        for j, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                i = stack.pop()
                answer[i] = prices[i] - price
            stack.append(j)

        return answer
        