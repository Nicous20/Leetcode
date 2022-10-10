class Solution(object):
    ls_sign = [['+'], ['-'], ['*'], ['']]
    ls_num = []
    target = 0
    ans = []

    def get_answer(self, ls):
        ans = 0
        mul_val = self.ls_num[0]
        sg = '+'
        i = 0
        while i < len(ls):
            if ls[i] == '':
                mul_val = mul_val * 10 + self.ls_num[i + 1]
                i += 1
            elif ls[i] == '*':
                tar = self.ls_num[i + 1]
                j = i + 1
                while j < len(ls) and ls[j] == '':
                    tar = tar * 10 + self.ls_num[j + 1]
                    j += 1
                mul_val *= tar
                i = j
            else:
                if sg == '+':
                    ans += mul_val
                else:
                    ans -= mul_val
                mul_val = self.ls_num[i+1]
                sg = ls[i]
                i += 1
        if sg == '+':
            return ans + mul_val
        else:
            return ans - mul_val

    def to_string(self, ls):
        ans = ""
        head_zero = 0
        if self.ls_num[0] == 0:
            head_zero = 1
        for i in range(len(self.ls_num) - 1):
            if self.ls_num[i] == 0 and head_zero == 0 :
                continue
            head_zero = 1
            ans += str(self.ls_num[i])
            ans += ls[i]
        ans += str(self.ls_num[-1])
        return ans

    def find(self, ls):
        if len(ls) == len(self.ls_num) - 1:
            num = self.ls_num[0]
            for i in range(len(self.ls_num) - 1):
                if self.ls_num[i] == 0 and ls[i] == '' and num == 0:
                    return None
                if ls[i] != '':
                    num = self.ls_num[i + 1]
            if self.get_answer(ls) == self.target:
                self.ans.append(self.to_string(ls))
            return None

        for i in range(4):
            self.find(ls + self.ls_sign[i])

    def addOperators(self, num, target):
        self.ls_num = []
        self.ans = []
        self.target = target
        for i in range(len(num)):
            self.ls_num.append(int(num[i]))

        self.find([])
        return self.ans


# a = Solution()
# print(a.addOperators("123456789", 45))
# print(a.addOperators("00", 0))
# print(a.addOperators("105", 5))
# print(a.addOperators("3456237490",9191))
# print(a.addOperators("1000000009",9))

