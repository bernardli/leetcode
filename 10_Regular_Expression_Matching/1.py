'''
递归版本, 判定上比较啰嗦
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p.find('*') == -1:
            if len(s) != len(p):
                return False
            for i in range(len(s)):
                if s[i] != p[i] and p[i] != '.':
                    return False
            return True

        # 可拓展的长度
        self.remainLen = len(s) - (len(p) - p.count('*') * 2)
        if self.remainLen < 0:
            return False

        return self.check(s[0:], p[0:])

    def check(self, s, p):
        # 检查s和p
        if len(s) != 0 and len(p) == 0:
            return False
        if len(s) == 0 and len(p) != 0:
            if p.count('*') == -1:
                return False
            if len(p) - p.count('*') * 2 != 0:   # 这里没有考虑两个连续*的情况
                return False
            return True
        if len(s) == 0 and len(p) == 0:
            return True

        # 匹配
        if s[0] != p[0] and p[0] != '.':
            if len(p) > 1 and p[1] == '*':      # 不匹配时*必取0, 不消耗可拓展长度
                return self.check(s[0:], p[2:])
            else:
                return False
        else:
            if len(p) > 1 and p[1] == '*' and self.remainLen > 0:
                self.remainLen -= 1
                if self.check(s[1:], p[0:]):
                    return True
                else:
                    self.remainLen += 1  # 把前面多减的加回来
                    return self.check(s[0:], p[2:])
            # 没有剩余可拓展长度了, 此处的*必须取0
            elif len(p) > 1 and p[1] == '*' and self.remainLen == 0:
                return self.check(s[0:], p[2:])
            else:
                return self.check(s[1:], p[1:])         # 后面没有*, 直接单个匹配

    def run(self):
        print(self.isMatch('aa', 'a'))
        print(self.isMatch('aa', 'a*'))
        print(self.isMatch('ab', '.*'))
        print(self.isMatch('aab', 'c*a*b'))
        print(self.isMatch('mississippi', 'mis*is*p*.'))

        ######## 初次未通过的case #######
        print(self.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'))


# test
foo = Solution()
foo.run()

# s = "aasdfasdfasdfasdfas"
# p = "aasdf.*asdf.*asdf.*asdf.*s"
# print(len(s) - (len(p) - p.count('*') * 2))
