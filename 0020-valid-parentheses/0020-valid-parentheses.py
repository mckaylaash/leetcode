class Solution:
    def isValid(self, s: str) -> bool:
        closed_bracket_order = [0]

        for item in s:
                if item == "(": closed_bracket_order.append(")")
                elif item == ")":
                    if closed_bracket_order[-1] == ")": closed_bracket_order.pop()
                    else: return False

                elif item == "[": closed_bracket_order.append("]")
                elif item == "]":
                    if closed_bracket_order[-1] == "]": closed_bracket_order.pop()
                    else: return False

                elif item == "{": closed_bracket_order.append("}")
                else:
                     if closed_bracket_order[-1] == "}": closed_bracket_order.pop()
                     else: return False

        return len(closed_bracket_order) == 1 and closed_bracket_order[0] == 0
        



        