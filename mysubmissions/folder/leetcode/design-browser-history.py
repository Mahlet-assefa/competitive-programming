class BrowserHistory:

    def __init__(self, homepage: str):
        self.stk=[homepage]
        self.next=0

    def visit(self, url: str) -> None:
        self.stk=self.stk[:self.next+1]
        self.stk.append(url)
        self.next=len(self.stk)-1

    def back(self, steps: int) -> str:
        self.next=max(self.next-steps,0)
        return self.stk[self.next]

    def forward(self, steps: int) -> str:
        self.next=min(self.next+steps,len(self.stk)-1)
        return self.stk [self.next]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)