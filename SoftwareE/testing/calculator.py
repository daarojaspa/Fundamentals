class Calculator:
    def sum(self,a: int, b: int) -> int:
        return a + b

    def subst(self,a: int, b: int) -> int:
        return a - b

    def mult(self,a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("can´t divide by 0 ")
        return a / b
