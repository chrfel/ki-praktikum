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
        # Knowledgebase parsen und setzen
        self.kb = self.lp.parse(sentence)

    def tell(self, sentence):
        # Und Verknüpfung aus alter KB und aktuellem Satz
        self.kb = AndExpression(self.kb, self.lp.parse(sentence))

    def drawKb(self):
        tree = self.tree_from_expression(self.kb)
        tree.draw()

    def tree_from_expression(self, e: Expression):
        # Abbruchbedingung, wenn keine Kinder mehr da sind --> Keine BinaryExpression, sondern z.B. FunctionVariableExpression A
        if not isinstance(e, BinaryExpression):
            # Erster Parameter: Expression als String, Zweiter: Children, also keine, weil wir beim Kindknoten sind
            return Tree("%s" % e, [])

        # Zeichen ausgeben, z.B. &
        operator = e.getOp()

        # Kinder auswerten
        children = [
            self.tree_from_expression(e.first),
            self.tree_from_expression(e.second)
        ]
        # Baum rekursiv hochgeben
        return Tree(operator, children)

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
        # Wenn Buchstabe, z.B. A
        if isinstance(exp, FunctionVariableExpression):
            return model[str(exp)]

        # Negative Expression, z.B. -C
        if isinstance(exp, NegatedExpression):
            return not self.__pl_true__(exp.term, model)

        # Kein Buchstabe und keine BinaryExpression, also z.B. & oder |
        if not isinstance(exp, BinaryExpression):
            raise Exception("Invalid Argument")

        linkerTeilbaum = self.__pl_true__(exp.first, model)
        rechterTeilbaum = self.__pl_true__(exp.second, model)

        if isinstance(exp, AndExpression):
            return linkerTeilbaum and rechterTeilbaum

        if isinstance(exp, OrExpression):
            return linkerTeilbaum or rechterTeilbaum

        if isinstance(exp, ImpExpression):
            return (not linkerTeilbaum) or rechterTeilbaum

        if isinstance(exp, IffExpression):
            return linkerTeilbaum == rechterTeilbaum

    def test_all_symbols(self, symbols, model):
        if not symbols:
            print(model)
            print(self.pl_true(model) == self.nltk_pl_true(model))
            return

        symbols_copy = symbols.copy()
        letterToCheck = symbols_copy.pop()

        model[letterToCheck] = False
        self.test_all_symbols(symbols_copy, model)

        model[letterToCheck] = True
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
        # Input Ausdruck
        alpha = self.lp.parse(alpha)
        # Alle Symbole aus der Knowledgebase und dem Ausdruck sammeln
        symbols = list(set.union(self.get_all_symbols(self.kb), self.get_all_symbols(alpha)))
        # Rein da
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



