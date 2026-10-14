class Solution(object):
    def countStudents(self, students, sandwiches):
        count = [0, 0]
        for s in students:
            count[s] += 1

        for i, sw in enumerate(sandwiches):
            if count[sw] == 0:
                return len(sandwiches) - i
            count[sw] -= 1

        return 0
        