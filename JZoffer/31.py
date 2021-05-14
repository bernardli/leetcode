from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while len(stack) > 0 and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        while i < len(popped):
            num = stack.pop()
            if num != popped[i]:
                return False
            i += 1

        return True

    def run(self):
        print(self.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        print(self.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

        print(self.validateStackSequences([2, 1, 0], [1, 2, 0]))


foo = Solution()
foo.run()
