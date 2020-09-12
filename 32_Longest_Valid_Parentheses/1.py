class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = list()
        maxLen = 0
        flag = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and len(stack) != 0:
                left_i = stack.pop()
                flag[left_i] = 1
                flag[i] = 1

        left = -1
        for i in range(len(flag)):
            if flag[i] == 1 and maxLen < i - left:
                maxLen = i - left
            elif flag[i] == 0:
                left = i

        return maxLen

    def run(self):
        print(self.longestValidParentheses('(()'))
        print(self.longestValidParentheses(')()())'))

foo = Solution()
foo.run()