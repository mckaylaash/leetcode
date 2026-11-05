class Solution:
    def calPoints(self, operations: list[str]) -> int:
        sum_list = []
        for item in operations:
            if item == 'C': sum_list.pop()
            elif item == 'D': sum_list.append(sum_list[-1] * 2)
            elif item == '+': sum_list.append(sum_list[-1] + sum_list[-2])
            else: sum_list.append(int(item))
        return sum(sum_list)

