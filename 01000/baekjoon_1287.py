from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
class Calculator:
    def __init__(self, str):
        self.str = str
        self.idx = 0
        self.result = self.expression()
        if self.idx != len(self.str):
            raise
    def expression(self) -> int:
        if self.idx == len(self.str) or (not str.isdigit(self.str[self.idx]) and self.str[self.idx] != '('):
            raise
        Sum = self.term()
        while self.idx < len(self.str) and (self.str[self.idx] == '+' or self.str[self.idx] == '-'):
            operator = self.str[self.idx]
            self.idx += 1
            Sum += self.term() * [-1, 1][operator == '+']
        return Sum
    def term(self) -> int:
        if self.idx == len(self.str) or (not str.isdigit(self.str[self.idx]) and self.str[self.idx] != '('):
            raise
        mult = self.parenthesis()
        while self.idx < len(self.str) and (self.str[self.idx] == '*' or self.str[self.idx] == '/'):
            operator = self.str[self.idx]
            self.idx += 1
            t = self.parenthesis()
            if operator == '*':
                mult *= t
            else:
                mult //= t
        return mult
    def parenthesis(self) -> int:
        if self.idx == len(self.str):
            raise
        if str.isdigit(self.str[self.idx]):
            return self.number()
        if self.str[self.idx] == '(':
            self.idx += 1
            sub = self.expression()
            if self.idx < len(self.str) and self.str[self.idx] == ')':
                self.idx += 1
                return sub
        raise
    def number(self) -> int:
        begin = self.idx
        while self.idx < len(self.str) and str.isdigit(self.str[self.idx]):
            self.idx += 1
        if begin == self.idx:
            raise
        return int(self.str[begin:self.idx])
try:
    print(Calculator(input()).result)
except:
    print('ROCK')
