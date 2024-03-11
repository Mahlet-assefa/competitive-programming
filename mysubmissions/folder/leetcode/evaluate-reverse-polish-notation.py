class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for tok in tokens:
            if tok in "+-*/":
                n2 = stk.pop()
                n1 = stk.pop()
                if tok == "+":
                    stk.append(n1+n2)
                if tok == "-":
                    stk.append(n1-n2)
                if tok == "*":
                    stk.append(n1*n2)
                if tok == "/":
                    stk.append(int(n1/n2))
            else:
                stk.append(int(tok))
        return stk.pop()

       