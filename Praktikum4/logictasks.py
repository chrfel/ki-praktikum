from logicwrapper import LogicWrapper

# aufgabe 14
def do14() :
    kb = LogicWrapper("((A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C))")
    kb.drawKb()

# aufgabe 15
def do15():
    kb = prepareKb()
    kb.drawKb()

# aufgabe 16
# This is how to create a Model
# TTFT and TTTT works
# https://web.stanford.edu/class/cs103/tools/truth-table-tool/
# ((A&&C) -> (B||D)) && ((A&&C) <-> (B||D)) && ((A->C) <-> (B->D)) && ((A&&D) || (C->D)) && ((D->C) && A)
def do16():
    kb = prepareKb()
    v = {"A": True, "B": False, "C": True, "D": True}
    print(kb.pl_true(v))

# aufgabe 17
def do17():
    kb = prepareKb()
    symbols = ["A", "B", "C", "D"]
    symbols.reverse()
    kb.test_all_symbols(symbols, {})

# aufgabe 18
def do18():
    kb = prepareKb()
    print(kb.tt_entails("(A & B & C & D) | (A & -B & C & D)"))

def prepareKb():
    kb = LogicWrapper("(A&C) -> (B|D)")
    kb.tell("(A&C) <-> (B|D)")
    kb.tell("(A->C) <-> (B->D)")
    kb.tell("(A&D) | (C->D)")
    kb.tell("(D->C) & A")
    return kb

def doTests():
    #Bindung zeigen
    #kb = LogicWrapper("A & -B")
    kb = LogicWrapper("A & B | -C -> D <-> E")
    kb.drawKb()




if __name__ == '__main__':
    #do14()
    #do15()
    #do16()
    #do17()
    #do18()
    doTests()
