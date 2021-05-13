from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['+', '-', '*', '/'])
        for i in tokens:
            if i not in operator:
                stack.append(i)
            else:
                num_1 = int(stack.pop())
                num_2 = int(stack.pop())
                if i == '+':
                    stack.append(num_2 + num_1)
                elif i == '-':
                    stack.append(num_2 - num_1)
                elif i == '*':
                    stack.append(num_2 * num_1)
                elif i == '/':
                    stack.append(int(num_2 / num_1))

        return int(stack[0])

    def run(self):
        print(self.evalRPN(["2", "1", "+", "3", "*"]))
        print(self.evalRPN(["4", "13", "5", "/", "+"]))
        print(self.evalRPN(["10", "6", "9", "3", "+",
                            "-11", "*", "/", "*", "17", "+", "5", "+"]))

foo =Solution()
foo.run()
