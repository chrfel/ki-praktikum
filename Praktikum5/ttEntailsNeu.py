from logiccalculator import LogicCalculator

class LogicCalculatorModified(LogicCalculator):

    def test_all_symbols(self, symbols, model):
        if not symbols:
            print(model)
            print(self.nltk_pl_true(model))
            return

        symbols_copy = symbols.copy()
        letterToCheck = symbols_copy.pop()

        model[letterToCheck] = False
        self.test_all_symbols(symbols_copy, model)

        model[letterToCheck] = True
        self.test_all_symbols(symbols_copy, model)

    def tt_check_all(self, alpha, symbols, model):
        if not symbols:
            print(model)
            if self.pl_true(model):
                print("Model TRUE!")
                if (self.__pl_true__(alpha, model)):
                    print("Aussage TRUE!")
                return self.__pl_true__(alpha, model)
            else:
                return True

        symbols_copy = symbols.copy()
        symbol = symbols_copy.pop()

        model[symbol] = False
        result1 = self.tt_check_all(alpha, symbols_copy, model)

        model[symbol] = True
        result2 = self.tt_check_all(alpha, symbols_copy, model)

        return result1 and result2

if __name__ == "__main__":
    a = "(A|B|C)&(A|B|-C)&(-A|B|C)&(A|B|-(-C))"
    b = "(A|B|C)&(A|B|-C)&(-A|B|C)&(-A|-B|C)"
    c = "(A|B|C)&(A|-C)&(-A|B|C|D)&(-A|-B|C)"
    d = "(A|B|C)&(A|-C)&(-A|B&C|D)&(-A|-B|C)"
    e = "(A|B|C)&(A|-C)&((A|B)&(C|D))|(-A|-B|C)"
    f = "(A|B|C)&(A|-C)&(((-A|B)&C)|D)&(-A|-B|C)"

    lc = LogicCalculatorModified(a)
    lc.tell(b)
    lc.tell(c)
    lc.tell(d)
    lc.tell(e)
    lc.tell(f)
    
    symbols = ["A", "B", "C", "D"]
    symbols.reverse()
    lc.test_all_symbols(symbols, {})

    print("A -> B -> C -> D")
    print(lc.tt_entails("A -> B -> C -> D"))

    print("A -> (B -> (C -> D))")
    print(lc.tt_entails("A -> (B -> (C -> D))"))
