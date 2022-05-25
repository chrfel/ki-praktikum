from nltk.sem.logic import LogicParser, AndExpression, OrExpression, NegatedExpression, FunctionVariableExpression, ImpExpression, IffExpression, Expression, BinaryExpression
from nltk.sem import Model, Valuation, Assignment
from nltk.tree import Tree


# operatorreihenfolge:
# 1. -
# 2. &
# 3. |
# 4. ->
# 5. <->


class LogicCalculator:
    lp = LogicParser()

    def __init__(self, sentence):
        self.kb = self.lp.parse(sentence)

    def tell(self, sentence):
        self.kb = AndExpression(self.kb, self.lp.parse(sentence))

    def drawKb(self):
        # This is how we can create a Tree
        tree = self.tree_from_expression(self.kb)
        # and a tree can be drawn
        tree.draw()


    def tree_from_expression(self, e: Expression):
        if not isinstance(e, BinaryExpression):
            return Tree("%s" % e, [])

        # it should be a And/Orexpression. Unfortunately they don't have a superclass which getOp()
        label = e.getOp()

        chidlren = [
            self.tree_from_expression(e.first),
            self.tree_from_expression(e.second)
        ]

        return Tree(label, chidlren)

    def nltk_pl_true(self, model):
        model = model.items()

        val = Valuation(model)
        dom = val.domain
        g = Assignment(dom)
        m = Model(dom, val)

        # this is how you test whether the model is true for the expression(KB)
        return(m.satisfy(self.kb, g))

    def pl_true(self, model):
        return self.__pl_true__(self.kb, model)

    def __pl_true__(self, exp: Expression, model):
        # get boolean of leaf node variable
        if isinstance(exp, FunctionVariableExpression):
            return model[str(exp)]

        if isinstance(exp, NegatedExpression):
            return not self.__pl_true__(exp.term, model)

        if not isinstance(exp, BinaryExpression):
            raise Exception("Invalid Argument")

        left = self.__pl_true__(exp.first, model)
        right = self.__pl_true__(exp.second, model)

        if isinstance(exp, AndExpression):
            return left and right

        if isinstance(exp, OrExpression):
            return left or right

        if isinstance(exp, ImpExpression):
            return (not left) or right

        if isinstance(exp, IffExpression):
            return left == right

    def test_all_symbols(self, symbols, model):
        if not symbols:
            print(model)
            print(self.pl_true(model) == self.nltk_pl_true(model))
            return

        symbols_copy = symbols.copy()
        symbol = symbols_copy.pop()

        model[symbol] = False
        self.test_all_symbols(symbols_copy, model)

        model[symbol] = True
        self.test_all_symbols(symbols_copy, model)

    def get_all_symbols(self, exp: Expression):
        if isinstance(exp, FunctionVariableExpression):
            return set(str(exp))

        if isinstance(exp, NegatedExpression):
            return self.get_all_symbols(exp.term)

        if not isinstance(exp, BinaryExpression):
            raise Exception("Invalid Argument")

        return set.union(self.get_all_symbols(exp.first), self.get_all_symbols(exp.second))

    def tt_entails(self, alpha):
        alpha = self.lp.parse(alpha)
        symbols = list(set.union(self.get_all_symbols(self.kb), self.get_all_symbols(alpha)))

        return self.tt_check_all(alpha, symbols, {})

    def tt_check_all(self, alpha, symbols, model):
        if not symbols:
            if self.pl_true(model):
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



