class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = [] 

        for current_day, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                result[waiting_day] = current_day - waiting_day
            stack.append(current_day)

        return result