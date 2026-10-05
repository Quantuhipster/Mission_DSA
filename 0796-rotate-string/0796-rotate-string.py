class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and (s + s).find(goal) != -1