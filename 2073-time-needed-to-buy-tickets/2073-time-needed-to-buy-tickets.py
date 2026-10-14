class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        total = 0
        for i, t in enumerate(tickets):
            if i <= k:
                total += min(t, tickets[k])
            else:
                total += min(t, tickets[k] - 1)
        return total
        