class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices still waiting for a warmer day

        for j in range(n):
            while stack and temperatures[stack[-1]] < temperatures[j]:
                i = stack.pop()
                answer[i] = j - i
            stack.append(j)

        return answer