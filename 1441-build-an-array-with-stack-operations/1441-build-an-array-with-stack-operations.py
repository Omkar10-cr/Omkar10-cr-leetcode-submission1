class Solution(object):
    def buildArray(self, target, n):
        res = []
        j = 0
        for num in range(1, n + 1):
            if j == len(target):
                break
            res.append("Push")
            if target[j] == num:
                j += 1
            else:
                res.append("Pop")
        return res